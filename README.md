# GPA Calculator and Visualizer

This project provides a simple GPA calculator and visualizer based on a given Excel file containing course grades and credits.

## Features

* **Calculates GPA:** Converts letter grades to GPA based on a 4.0 or 4.5 scale.
* **Weighted Averages:** Calculates weighted average grades and GPAs based on course credits.
* **Semester-wise Analysis:** Breaks down GPA and grade averages by semester.
* **Visualization:** Generates a plot showing the trend of average scores and GPAs over semesters.

## Requirements

* Python 3
* Libraries:
    * matplotlib
    * pandas

You can install these libraries using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. **Prepare your data:**
   * Create an Excel file (e.g., `sign_score.xlsx`) with the following columns:
     * `semester`: Semester identifier (e.g., "1-1", "1-2", etc.)
     * `course`: Course name
     * `credit`: Course credits
     * `grade`: Numerical grade (e.g., 85, 92, etc.)
2. **Update the file path:**
   * In `main.py`, modify the `excel_file` variable to point to your Excel file:
     ```python
     excel_file = 'data/sign_score.xlsx'  # Replace with your Excel file path
     ```
3. **Run the script:**
   ```bash
   python app.py
   ```

## Output

* The script will print the average grade and GPA for each selected semester.
* It will also print the overall average grade and GPA.
* Finally, it will display a plot showing the average scores and GPAs over the selected semesters.

## Example Data (sign_score.xlsx)

| semester | course        | credit | grade |
|----------|---------------|--------|-------|
| 1-1      | Math 101      | 3      | 88    |
| 1-1      | Physics 101   | 4      | 92    |
| 1-2      | Chemistry 101 | 3      | 85    |
| ...      | ...           | ...    | ...   |

## Todo

- Add typing
- Improve Encapsulation
