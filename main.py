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


def plot_averages(semesters, averages):
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
    plt.title('Average Scores and GPAs')

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

    # Calculate averages for each semester
    averages = calculate_semester_averages(semesters_courses, scale)

    # Print semester averages
    for i, avg in enumerate(averages):
        print(f"Semester {semesters[i]}: {avg}")

    # Calculate overall average
    overall_average = calculate_overall_average(semesters_courses, scale)
    print(f"Overall Average: {overall_average}")

    # Plot the averages
    plot_averages(semesters, averages)


if __name__ == "__main__":
    main()