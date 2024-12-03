import matplotlib.pyplot as plt
import pandas as pd
from gpa_calculator import calculate_weighted_averages


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


def plot_averages(semesters, averages, title):
    """
    Plot the average scores and GPAs for each semester.
    """
    # Extract the average_score and average_gpa values
    average_scores = [item['average_grade'] for item in averages]
    average_gpas = [item['average_gpa'] for item in averages]

    # Plotting the data
    fig, ax1 = plt.subplots(figsize=(10, 5))

    # Plot average scores on the primary y-axis
    ax1.plot(semesters, average_scores, label='Average Score', marker='o', color='b')
    ax1.set_xlabel('Semester')
    ax1.set_ylabel('Average Score', color='b')
    ax1.tick_params(axis='y', labelcolor='b')

    # Create a second y-axis for the average GPAs
    ax2 = ax1.twinx()
    ax2.plot(semesters, average_gpas, label='Average GPA', marker='s', color='g')
    ax2.set_ylabel('Average GPA', color='g')
    ax2.tick_params(axis='y', labelcolor='g')

    # Adding titles and labels
    plt.title(title)

    # Adding a legend
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Show the plot
    plt.show()


def main():
    # File path to the Excel file
    excel_file = 'data/sign_score.xlsx'
    scale = 4.5

    # Load the data
    df = load_data(excel_file)

    # Get semesters and courses grouped by semester
    semesters, semesters_courses = get_semester_courses(df)

    # Calculate averages for all courses
    all_averages = calculate_semester_averages(semesters_courses, scale)

    # Print semester averages for all courses
    print("All Courses:")
    for i, avg in enumerate(all_averages):
        print(f"Semester {semesters[i]}: {avg}")

    # Calculate overall average for all courses
    overall_all_average = calculate_overall_average(semesters_courses, scale)
    print(f"Overall Average (All Courses): {overall_all_average}")

    # Filter major courses
    major_courses = filter_major_courses(semesters_courses)

    # Calculate averages for major courses
    major_averages = calculate_semester_averages(major_courses, scale)

    # Print semester averages for major courses
    print("\nMajor Courses:")
    for i, avg in enumerate(major_averages):
        print(f"Semester {semesters[i]}: {avg}")

    # Calculate overall average for major courses
    overall_major_average = calculate_overall_average(major_courses, scale)
    print(f"Overall Average (Major Courses): {overall_major_average}")

    # Plot the averages for all courses
    plot_averages(semesters, all_averages, "Average Scores and GPAs (All Courses)")

    # Plot the averages for major courses
    plot_averages(semesters, major_averages, "Average Scores and GPAs (Major Courses)")


if __name__ == "__main__":
    main()