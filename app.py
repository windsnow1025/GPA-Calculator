from typing import Any

import matplotlib.pyplot as plt

import course_data_loader
import gpa_calculator
from gpa_calculator import GPAScales, SemesterCourses, Semesters


def process_data(
        semesters: Semesters,
        semesters_courses: SemesterCourses,
        scales: GPAScales
) -> dict[str, Any]:
    """Process data and calculate all averages"""
    # Semester
    semester_avgs = []
    for semester_courses in semesters_courses:
        semester_avg = {}
        for scale_name, scale_rules in scales.items():
            semester_avg[scale_name] = gpa_calculator.calculate_weighted_averages(
                semester_courses, scale_rules)
        semester_avgs.append(semester_avg)

    # Overall
    overall_avgs = {}
    all_courses = course_data_loader.get_all_courses(semesters_courses)
    for scale_name, scale_rules in scales.items():
        overall_avgs[scale_name] = gpa_calculator.calculate_weighted_averages(all_courses, scale_rules)

    # Major
    major_courses = course_data_loader.get_major_semester_courses(semesters_courses)
    major_avgs = {}
    all_major_courses = course_data_loader.get_all_courses(major_courses)
    for scale_name, scale_rules in scales.items():
        major_avgs[scale_name] = gpa_calculator.calculate_weighted_averages(all_major_courses, scale_rules)

    return {
        'semesters': semesters,
        'semester_avgs': semester_avgs,
        'overall_avgs': overall_avgs,
        'major_avgs': major_avgs
    }


def display_results(results) -> None:
    """Display all calculated results"""
    # Semester
    print("\nAll Courses:")
    for semester, semester_avg in zip(results['semesters'], results['semester_avgs']):
        print(f"\nSemester {semester}:")
        first_scale = list(semester_avg.keys())[0]
        print(f"Average Score: {semester_avg[first_scale]['avg_score']:.4f}")
        for scale_name, avg in semester_avg.items():
            print(f"GPA ({scale_name}): {avg['avg_gpa']:.4f}")

    # Overall
    print("\nOverall Averages:")
    first_scale = list(results['overall_avgs'].keys())[0]
    print(f"Average Score: {results['overall_avgs'][first_scale]['avg_score']:.4f}")
    for scale_name, avg in results['overall_avgs'].items():
        print(f"GPA ({scale_name}): {avg['avg_gpa']:.4f}")

    # Major
    print("\nMajor Averages:")
    first_scale = list(results['major_avgs'].keys())[0]
    print(f"Average Score: {results['major_avgs'][first_scale]['avg_score']:.4f}")
    for scale_name, avg in results['major_avgs'].items():
        print(f"GPA ({scale_name}): {avg['avg_gpa']:.4f}")


def plot_results(results, scales) -> None:
    """Plot the visualization of results with adjusted axis limits"""
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Prepare data for plotting
    semesters = results['semesters']
    first_scale = list(scales.keys())[0]

    # Primary y-axis: average scores
    avg_scores = [sem[first_scale]['avg_score'] for sem in results['semester_avgs']]

    # Calculate min and max for average scores (steps of 5)
    score_min = min(avg_scores)
    score_max = max(avg_scores)
    score_min_adjusted = (score_min // 5) * 5  # Round down to nearest 5
    score_max_adjusted = ((score_max // 5) + 1) * 5  # Round up to nearest 5

    ax1.plot(semesters, avg_scores, label='Average Score', marker='o', color='b')
    ax1.set_xlabel('Semester')
    ax1.set_ylabel('Average Score', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.set_ylim(score_min_adjusted, score_max_adjusted)

    # Secondary y-axis: GPAs
    ax2 = ax1.twinx()
    colors = ['g', 'r', 'purple', 'orange']

    # Get all GPA values to determine overall min and max
    all_gpas = []
    for scale_name, _ in scales.items():
        gpas = [sem[scale_name]['avg_gpa'] for sem in results['semester_avgs']]
        all_gpas.extend(gpas)

    # Calculate min and max for GPAs (steps of 0.5)
    gpa_min = min(all_gpas)
    gpa_max = max(all_gpas)
    gpa_min_adjusted = (gpa_min // 0.5) * 0.5  # Round down to nearest 0.5
    gpa_max_adjusted = ((gpa_max // 0.5) + 1) * 0.5  # Round up to nearest 0.5

    for (scale_name, _), color in zip(scales.items(), colors):
        gpas = [sem[scale_name]['avg_gpa'] for sem in results['semester_avgs']]
        ax2.plot(semesters, gpas, label=f'GPA ({scale_name})', marker='s', color=color)

    ax2.set_ylabel('GPA', color='g')
    ax2.tick_params(axis='y', labelcolor='g')
    ax2.set_ylim(gpa_min_adjusted, gpa_max_adjusted)

    plt.title("Average Scores and GPAs (All Courses)")
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

    plt.tight_layout()
    plt.show()


def main():
    file_path = 'data/sign_score.xlsx'
    scales = gpa_calculator.load_gpa_scales()

    # Load data
    semesters, semesters_courses = course_data_loader.load_excel_data(file_path)

    # Process data
    results = process_data(semesters, semesters_courses, scales)

    # Display results
    display_results(results)

    # Plot results
    plot_results(results, scales)


if __name__ == "__main__":
    main()
