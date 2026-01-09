# Python Assignment

This repository contains small Python scripts demonstrating problem-solving skills and basic automation tasks. Each script is self-contained and can be run independently.

## Scripts
### 1. Reverse words in a string (`reverse_string.py`)

- **Purpose:** Reverses words and numbers of a string, ignoring spaces and punctuation.
- **Functionality:**
  - Attempts to reverse strings using simple stacks:
    - `tries to maintain at least O(n) time complexity`  
  - Tests:
    - `contains a small and simple test suite that outputs to the terminal for clarity`
- **Usage Example:**
  ```bash
  python reverse_string.py


### 2. Version Updater (`version_no_update.py`)

- **Purpose:** Automatically updates version numbers in project files as part of a build process.
- **Functionality:**
  - Reads environment variables:
    - `SourcePath` – root folder of the project containing the files
    - `BuildNum` – new build version number
  - Updates:
    - `SConstruct` → changes `point=<number>`
    - `VERSION` → changes `ADLMSDK_VERSION_POINT=<number>`
  - Ensures safe updates and prints a confirmation of changes.
- **Usage Example:**
  ```bash
  export SourcePath=/path/to/project
  export BuildNum=123
  python test_part_2.py
