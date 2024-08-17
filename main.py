import matplotlib.pyplot as plt
import pandas as pd

from gpa_calculator import calculate_weighted_averages

# Load the Excel file
excel_file = 'data/sign_score.xlsx'  # Replace with your Excel file path
df = pd.read_excel(excel_file)

scale = 4.5
semesters = ['1-1', '1-2', '2-1', '2-2', '3-1', '3-2', '4-1', '4-2']
selected_semesters = semesters[:-2]

semesters_courses = []
for semester in selected_semesters:
    semesters_courses.append(df[df['semester'] == semester].to_dict(orient='records'))

averages = []
for i in range(len(semesters_courses)):
    averages.append(calculate_weighted_averages(semesters_courses[i], scale))
for i in range(len(averages)):
    print(averages[i])

courses = []
for semester_courses in semesters_courses:
    courses += semester_courses
average = calculate_weighted_averages(courses, scale)
print(average)

# Extract the average_score and average_gpa values
average_scores = [item['average_grade'] for item in averages]
average_gpas = [item['average_gpa'] for item in averages]

# Plotting the data
fig, ax1 = plt.subplots(figsize=(10, 5))

# Plot average scores on the primary y-axis
ax1.plot(selected_semesters, average_scores, label='Average Score', marker='o', color='b')
ax1.set_xlabel('Semester')
ax1.set_ylabel('Average Score', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Create a second y-axis for the average GPAs
ax2 = ax1.twinx()
ax2.plot(selected_semesters, average_gpas, label='Average GPA', marker='s', color='g')
ax2.set_ylabel('Average GPA', color='g')
ax2.tick_params(axis='y', labelcolor='g')

# Adding titles and labels
plt.title('Average Scores and GPAs')

# Adding a legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.show()