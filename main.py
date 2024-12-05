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


def plot_averages(semesters, averages_by_scale, title):
    """
    Plot the average scores and GPAs for each semester for all scales.
    """
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot average scores on the primary y-axis
    ax1.plot(semesters, [item['average_grade'] for item in averages_by_scale[list(averages_by_scale.keys())[0]]],
             label='Average Score', marker='o', color='b')
    ax1.set_xlabel('Semester')
    ax1.set_ylabel('Average Score', color='b')
    ax1.tick_params(axis='y', labelcolor='b')

    # Create a second y-axis for the GPAs
    ax2 = ax1.twinx()
    colors = ['g', 'r', 'purple', 'orange']  # Add more colors if needed
    for (scale_name, averages), color in zip(averages_by_scale.items(), colors):
        ax2.plot(semesters, [item['average_gpa'] for item in averages],
                 label=f'GPA ({scale_name})', marker='s', color=color)

    ax2.set_ylabel('GPA', color='g')
    ax2.tick_params(axis='y', labelcolor='g')

    plt.title(title)

    # Combine legends from both axes
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

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
    print("\nAll Courses:")
    for i, semester in enumerate(semesters):
        semester_averages = {}
        for scale_name, scale_data in scales.items():
            semester_courses = semesters_courses[i]
            avg = calculate_weighted_averages(semester_courses, scale_data['rules'])
            semester_averages[scale_data['name']] = avg

        # Print semester averages for all courses
        print(f"\nSemester {semester}:")
        print(f"Average Score: {semester_averages[list(semester_averages.keys())[0]]['average_grade']:.4f}")
        for scale_name, avg in semester_averages.items():
            print(f"GPA ({scale_name}): {avg['average_gpa']:.4f}")

        # Store averages for plotting
        for scale_name, avg in semester_averages.items():
            if scale_name not in all_averages_by_scale:
                all_averages_by_scale[scale_name] = []
            all_averages_by_scale[scale_name].append(avg)

    # Print overall averages for all courses
    print("\nOverall Averages (All Courses):")
    overall_all_averages = {}
    for scale_name, scale_data in scales.items():
        overall_avg = calculate_overall_average(semesters_courses, scale_data['rules'])
        overall_all_averages[scale_data['name']] = overall_avg

    print(f"Average Score: {overall_all_averages[list(overall_all_averages.keys())[0]]['average_grade']:.4f}")
    for scale_name, avg in overall_all_averages.items():
        print(f"GPA ({scale_name}): {avg['average_gpa']:.4f}")

    # Filter major courses and calculate overall averages
    major_courses = filter_major_courses(semesters_courses)

    # Print overall averages for major courses only
    print("\nOverall Averages (Major Courses):")
    overall_major_averages = {}
    for scale_name, scale_data in scales.items():
        overall_avg = calculate_overall_average(major_courses, scale_data['rules'])
        overall_major_averages[scale_data['name']] = overall_avg

    print(f"Average Score: {overall_major_averages[list(overall_major_averages.keys())[0]]['average_grade']:.4f}")
    for scale_name, avg in overall_major_averages.items():
        print(f"GPA ({scale_name}): {avg['average_gpa']:.4f}")

    # Plot the averages for all courses only
    plot_averages(semesters, all_averages_by_scale, "Average Scores and GPAs (All Courses)")


if __name__ == "__main__":
    main()
