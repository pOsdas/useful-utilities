RETRY_ATTEMPTS = 10
RETRY_DELAY = 2.0


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    try:
        await db_helper.create_db_if_not_exists()
    except Exception as e:
        print("create_db_if_not_exists error:", e)

    db_ready = False
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        try:
            if await db_helper.ping():
                db_ready = True
                break
        except Exception as e:
            print(f"DB ping failed (attempt {attempt}/{RETRY_ATTEMPTS}): {e}")
        await asyncio.sleep(RETRY_DELAY)

    if not db_ready:
        raise RuntimeError("Database is not available after retries")

    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield
    # shutdown
    await db_helper.dispose()