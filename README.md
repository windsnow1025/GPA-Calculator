# GPA Calculator and Visualizer

This project provides a simple GPA calculator and visualizer based on a given Excel file containing course grades and
credits.

## Features

* **Calculates GPA:** Converts letter grades to GPA based on a 4.0 or 4.5 scale.
* **Weighted Averages:** Calculates weighted average grades and GPAs based on course credits.
* **Semester-wise Analysis:** Breaks down GPA and grade averages by semester.
* **Visualization:** Generates a plot showing the trend of average scores and GPAs over semesters.

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
