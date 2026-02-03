# GPA Calculator and Visualizer

A simple GPA calculator and visualizer based on a given Excel file containing course grades and credits.

## Features

* **Excel Input:** Reads course data from Excel files with semester, course name, credits, grades, and major indicators
* **Configurable GPA Scales:** Supports multiple GPA scale systems (4.0, 4.5, WES) defined in JSON
* **GPA Calculation:**
  * Weighted GPA calculation based on course credits
  * Overall, semester-wise, and major-specific GPA analysis
  * Multiple GPA scale support for grade conversion
* **Visualization:** Dual-axis plots showing scores and GPA trends across semesters

## Development

### Python uv

1. Install uv: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Install Python in uv: `uv python install 3.12`; upgrade Python in uv: `uv python upgrade 3.12`
3. Configure requirements:
  ```bash
  uv sync --refresh
  ```

### Pycharm

1. Add New Interpreter >> Add Local Interpreter
  - Environment: Select existing
  - Type: uv
2. Add New Configuration >> uv run >> script: `app.py`

## Usage

Create an Excel file `data/sign_score.xlsx`

 | semester | course        | credit | grade | major |
 |----------|---------------|--------|-------|-------|
 | 1-1      | Math 101      | 3      | 88    | y     |
 | 1-1      | Physics 101   | 4      | 92    | y     |
 | 1-2      | Chemistry 101 | 3      | 85    | y     |
 | ...      | ...           | ...    | ...   | ...   |
