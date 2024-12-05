# GPA Calculator and Visualizer

This project provides a simple GPA calculator and visualizer based on a given Excel file containing course grades and
credits.

## Features

* **Excel Input:** Reads course data from Excel files with semester, course name, credits, grades, and major indicators
* **Configurable GPA Scales:** Supports multiple GPA scale systems (4.0, 4.5, WES) defined in JSON
* **GPA Calculation:**
  * Weighted GPA calculation based on course credits
  * Overall, semester-wise, and major-specific GPA analysis
  * Multiple GPA scale support for grade conversion
* **Visualization:** Dual-axis plots showing scores and GPA trends across semesters

## Requirements

* Python 3.12

```bash
pip install -r requirements.txt
```

## Usage

1. **Prepare your data:**
    * Create an Excel file `data/sign_score.xlsx`

   | semester | course        | credit | grade | major |
   |----------|---------------|--------|-------|-------|
   | 1-1      | Math 101      | 3      | 88    | y     |
   | 1-1      | Physics 101   | 4      | 92    | y     |
   | 1-2      | Chemistry 101 | 3      | 85    | y     |
   | ...      | ...           | ...    | ...   | ...   |

2. **Run the script:**
   ```bash
   python app.py
   ```
