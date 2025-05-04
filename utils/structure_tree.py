import os
import sys

# Blacklist
EXCLUDED = {
    "__pycache__", ".venv", ".idea", ".git", ".mypy_cache",
    ".pytest_cache", ".DS_Store", "venv", ".env", ".coverage"
}


def build_tree(root_path: str, prefix: str = ""):
    try:
        entries = [
            e for e in os.listdir(root_path)
            if e not in EXCLUDED and not e.startswith(".")
        ]
    except PermissionError:
        return

    entries = sorted(
        entries, key=lambda e: (not os.path.isdir(os.path.join(root_path, e)), e.lower())
    )
    count = len(entries)

    for index, name in enumerate(entries):
        path = os.path.join(root_path, name)
        is_last = (index == count - 1)
        branch = "└── " if is_last else "├── "
        print(prefix + branch + name, end="")

        print()

        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            build_tree(path, prefix + extension)


if __name__ == "__main__":
    project_root = str(input("Enter project root path: "))
    print(os.path.abspath(project_root))
    build_tree(project_root)
