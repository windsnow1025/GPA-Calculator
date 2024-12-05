import pandas as pd

from gpa_calculator import SemesterCourses, Courses, Semesters


def load_excel_data(file_path: str) -> tuple[Semesters, SemesterCourses]:
    """
    Load data from Excel file and organize it by semesters

    Returns:
        tuple containing:
        - list of semester names
        - list of course lists for each semester
    """
    df = pd.read_excel(file_path)
    semesters = sorted(df['semester'].unique())
    semesters_courses = [df[df['semester'] == semester].to_dict(orient='records') for semester in semesters]

    return semesters, semesters_courses


def get_major_semester_courses(semesters_courses: SemesterCourses) -> SemesterCourses:
    """Extract major courses from all courses"""
    return [[course for course in semester if course['major'] == 'y'] for semester in semesters_courses]


def get_all_courses(semesters_courses: SemesterCourses) -> Courses:
    """Flatten semester courses into a single list"""
    return [course for semester in semesters_courses for course in semester]
