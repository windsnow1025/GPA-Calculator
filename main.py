import matplotlib.pyplot as plt
import pandas as pd
from gpa_calculator import *


def load_data(file_path):
    """
    Load the Excel file and return the DataFrame.
    """
    return pd.read_excel(file_path)


def get_semester_courses(df):
    """
    Extract unique semesters and group courses by semester.
    """
    semesters = sorted(df['semester'].unique())
    semesters_courses = [df[df['semester'] == semester].to_dict(orient='records') for semester in semesters]
    return semesters, semesters_courses


def filter_major_courses(semesters_courses):
    """
    Filter courses to include only major courses (where 'major' == 'y').
    """
    return [[course for course in semester_courses if course['major'] == 'y'] for semester_courses in semesters_courses]


def calculate_semester_averages(semesters_courses, scale):
    """
    Calculate weighted averages for each semester.
    """
    return [calculate_weighted_averages(semester_courses, scale) for semester_courses in semesters_courses]


def calculate_overall_average(semesters_courses, scale):
    """
    Calculate the overall weighted average across all semesters.
    """
    all_courses = [course for semester_courses in semesters_courses for course in semester_courses]
    return calculate_weighted_averages(all_courses, scale)


def plot_averages_all_scales(semesters, averages_by_scale):
    """
    Plot the average scores and GPAs for each semester for all scales.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Plot average scores
    ax1.plot(semesters, [item['average_grade'] for item in averages_by_scale[list(averages_by_scale.keys())[0]]],
             label='Average Score', marker='o')
    ax1.set_xlabel('Semester')
    ax1.set_ylabel('Average Score')
    ax1.set_title('Average Scores')
    ax1.legend()

    # Plot GPAs for each scale
    for scale_name, averages in averages_by_scale.items():
        ax2.plot(semesters, [item['average_gpa'] for item in averages],
                 label=f'GPA ({scale_name})', marker='o')

    ax2.set_xlabel('Semester')
    ax2.set_ylabel('GPA')
    ax2.set_title('GPAs by Scale')
    ax2.legend()

    plt.tight_layout()
    plt.show()


def main():
    # File path to the Excel file
    excel_file = 'data/sign_score.xlsx'

    # Load GPA scales
    scales = load_gpa_scales()

    # Load the data
    df = load_data(excel_file)

    # Get semesters and courses grouped by semester
    semesters, semesters_courses = get_semester_courses(df)

    # Calculate averages for all courses for each scale
    all_averages_by_scale = {}
    for scale_name, scale_data in scales.items():
        all_averages = calculate_semester_averages(semesters_courses, scale_data['rules'])
        all_averages_by_scale[scale_data['name']] = all_averages

        # Print semester averages for all courses
        print(f"\nAll Courses ({scale_data['name']}):")
        for i, avg in enumerate(all_averages):
            print(f"Semester {semesters[i]}: {avg}")

        # Calculate overall average for all courses
        overall_all_average = calculate_overall_average(semesters_courses, scale_data['rules'])
        print(f"Overall Average (All Courses - {scale_data['name']}): {overall_all_average}")

    # Filter major courses
    major_courses = filter_major_courses(semesters_courses)

    # Calculate averages for major courses for each scale
    major_averages_by_scale = {}
    for scale_name, scale_data in scales.items():
        major_averages = calculate_semester_averages(major_courses, scale_data['rules'])
        major_averages_by_scale[scale_data['name']] = major_averages

        # Print semester averages for major courses
        print(f"\nMajor Courses ({scale_data['name']}):")
        for i, avg in enumerate(major_averages):
            print(f"Semester {semesters[i]}: {avg}")

        # Calculate overall average for major courses
        overall_major_average = calculate_overall_average(major_courses, scale_data['rules'])
        print(f"Overall Average (Major Courses - {scale_data['name']}): {overall_major_average}")

    # Plot the averages for all courses
    plot_averages_all_scales(semesters, all_averages_by_scale)

    # Plot the averages for major courses
    plot_averages_all_scales(semesters, major_averages_by_scale)


if __name__ == "__main__":
    main()
