import matplotlib.pyplot as plt
import pandas as pd

import gpa_calculator


def load_and_process_data(file_path, scales):
    """Load and process all data, returning calculated results"""
    df = pd.read_excel(file_path)
    semesters = sorted(df['semester'].unique())
    semesters_courses = [df[df['semester'] == semester].to_dict(orient='records') for semester in semesters]

    # Calculate semester averages for all courses
    semester_results = []
    for semester_courses in semesters_courses:
        semester_avg = {}
        for scale_name, scale_data in scales.items():
            avg = gpa_calculator.calculate_weighted_averages(semester_courses, scale_data)
            semester_avg[scale_name] = avg
        semester_results.append(semester_avg)

    # Calculate overall averages for all courses
    overall_averages = {}
    all_courses = [course for semester in semesters_courses for course in semester]
    for scale_name, scale_data in scales.items():
        overall_avg = gpa_calculator.calculate_weighted_averages(all_courses, scale_data)
        overall_averages[scale_name] = overall_avg

    # Calculate major course averages
    major_courses = [[course for course in semester if course['major'] == 'y']
                     for semester in semesters_courses]
    major_overall = {}
    all_major_courses = [course for semester in major_courses for course in semester]
    for scale_name, scale_data in scales.items():
        major_avg = gpa_calculator.calculate_weighted_averages(all_major_courses, scale_data)
        major_overall[scale_name] = major_avg

    return {
        'semesters': semesters,
        'semester_results': semester_results,
        'overall_averages': overall_averages,
        'major_overall': major_overall
    }


def display_results(results, scales):
    """Display all calculated results"""
    # Display semester results
    print("\nAll Courses:")
    for semester, semester_avg in zip(results['semesters'], results['semester_results']):
        print(f"\nSemester {semester}:")
        first_scale = list(semester_avg.keys())[0]
        print(f"Average Score: {semester_avg[first_scale]['average_grade']:.4f}")
        for scale_name, avg in semester_avg.items():
            print(f"GPA ({scale_name}): {avg['average_gpa']:.4f}")

    # Display overall averages
    print("\nOverall Averages (All Courses):")
    first_scale = list(results['overall_averages'].keys())[0]
    print(f"Average Score: {results['overall_averages'][first_scale]['average_grade']:.4f}")
    for scale_name, avg in results['overall_averages'].items():
        print(f"GPA ({scale_name}): {avg['average_gpa']:.4f}")

    # Display major course averages
    print("\nOverall Averages (Major Courses):")
    first_scale = list(results['major_overall'].keys())[0]
    print(f"Average Score: {results['major_overall'][first_scale]['average_grade']:.4f}")
    for scale_name, avg in results['major_overall'].items():
        print(f"GPA ({scale_name}): {avg['average_gpa']:.4f}")


def plot_results(results, scales):
    """Plot the visualization of results"""
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Prepare data for plotting
    semesters = results['semesters']
    first_scale = list(scales.keys())[0]

    # Primary y-axis: average scores
    avg_scores = [sem[first_scale]['average_grade'] for sem in results['semester_results']]
    ax1.plot(semesters, avg_scores, label='Average Score', marker='o', color='b')
    ax1.set_xlabel('Semester')
    ax1.set_ylabel('Average Score', color='b')
    ax1.tick_params(axis='y', labelcolor='b')

    # Secondary y-axis: GPAs
    ax2 = ax1.twinx()
    colors = ['g', 'r', 'purple', 'orange']
    for (scale_name, _), color in zip(scales.items(), colors):
        gpas = [sem[scale_name]['average_gpa'] for sem in results['semester_results']]
        ax2.plot(semesters, gpas, label=f'GPA ({scale_name})', marker='s', color=color)

    ax2.set_ylabel('GPA', color='g')
    ax2.tick_params(axis='y', labelcolor='g')

    plt.title("Average Scores and GPAs (All Courses)")
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

    plt.tight_layout()
    plt.show()


def main():
    excel_file = 'data/sign_score.xlsx'
    scales = gpa_calculator.load_gpa_scales()

    # Calculate all results
    results = load_and_process_data(excel_file, scales)

    # Display results
    display_results(results, scales)

    # Plot results
    plot_results(results, scales)


if __name__ == "__main__":
    main()