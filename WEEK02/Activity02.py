import numpy as np

# Student scores array
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

# 1. Calculate the student average score for each student (Cross horizontal axis = 1)
student_averages = np.mean(scores, axis=1)
print("Average score for each student:", student_averages)

# print the average score the each student 
for index, average in enumerate(student_averages):
    print(f"Student {index + 1} - {average:.2f}")
print("-" * 30)

# 2. Calculate the average subject score (Cross vertical axis = 0)
subject_averages = np.mean(scores, axis=0)
print("Average score for each subject:", subject_averages)

# print the average score for the each subject 
for index, average in enumerate(subject_averages):
    print(f"Subject {index + 1} - {average:.2f}")
print("-" * 30)


# 3. Identify the student (row index) with the highest total score
total_scores = np.sum(scores, axis=1)
# Returns the index of the maximum values along an score.
highest_score_student_index = np.argmax(total_scores)
print(f"Row index of the student's highest total score: {highest_score_student_index}")
# Row index is 0-based. Student number would be index + 1.
print(f"This corresponds to Student {highest_score_student_index + 1} with a total score of {total_scores[highest_score_student_index]}")
print("-" * 30)
