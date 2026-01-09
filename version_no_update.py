import os
import re
import sys
from pathlib import Path

def update_file_version(file_path: Path, pattern: str, replacement: str):
    """
    Update version number in a file by replacing pattern with replacement.
    :param file_path: Path to the file to update.
    :param pattern: Regex pattern to search for.
    :param replacement: Replacement string.
    """
    if not file_path.exists():
        print(f"Error: File {file_path} does not exist.", file=sys.stderr)
        return

    # Make file writable
    file_path.chmod(0o755)

    content_changed = False
    lines = []

    with file_path.open('r') as fin:
        for line in fin:
            new_line = re.sub(pattern, replacement, line)
            if new_line != line:
                content_changed = True
            lines.append(new_line)

    if content_changed:
        with file_path.open('w') as fout:
            fout.writelines(lines)
        print(f"Updated version in {file_path}")
    else:
        print(f"No changes made to {file_path}")


def main():
    # Fetch environment variables
    source_path = os.environ.get("SourcePath")
    build_num = os.environ.get("BuildNum")

    if not source_path or not build_num:
        print("Error: Both 'SourcePath' and 'BuildNum' environment variables must be set.", file=sys.stderr)
        sys.exit(1)

    src_dir = Path(source_path) / "develop" / "global" / "src"

    # Files to update
    files_to_update = [
        (src_dir / "SConstruct", r"point=\d+", f"point={build_num}"),
        (src_dir / "VERSION", r"ADLMSDK_VERSION_POINT=\d+", f"ADLMSDK_VERSION_POINT={build_num}")
    ]

    for file_path, pattern, replacement in files_to_update:
        update_file_version(file_path, pattern, replacement)

if __name__ == "__main__":
    main()