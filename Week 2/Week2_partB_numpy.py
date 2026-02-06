import numpy as np
scores = np.array([
[55, 62, 71, 68],
[78, 85, 88, 90],
[45, 50, 48, 52],
[90, 92, 94, 96],
[60, 65, 70, 75]
])

print(scores.shape)
print("number of students", scores.shape[0])
print("number of assessments", scores.shape[1])

# Task 2 – Average Performance
# 1. Calculate the average score per student

avg_per_student = np.mean(scores, axis=1)
print("Average score per student:", avg_per_student)

# 2. Calculate the average score per assessment

avg_per_assessment = np.mean(scores, axis=0)
print("Average score per assessment:", avg_per_assessment)

# Task 3 – Pass / Fail Analysis


pass_mark = 40

# 1. Identify which students passed all assessments
# We check if each student's scores are all >= 40 using np.all() along axis=1 (checking each row).
passed_all_assessments = np.all(scores >= pass_mark, axis=1)
print("Students who passed all assessments:", passed_all_assessments)

# 2. Count how many students passed all assessments
# We count how many True values are in passed_all_assessments, since True = passed all assessments
num_students_passed_all = np.sum(passed_all_assessments)
print("Number of students who passed all assessments:", num_students_passed_all)

# Task 4 – High Performers


distinction_mark = 70


avg_per_student = np.mean(scores, axis=1)


distinction_students = avg_per_student >= distinction_mark
print("Students who achieved a distinction on average:", distinction_students)

# 2. Print their average scores
# Filter the average scores of the students who achieved a distinction
distinction_avg_scores = avg_per_student[distinction_students]
print("Average scores of distinction students:", distinction_avg_scores)

# Task 5 – Normalisation

# Calculate the minimum and maximum values in the entire scores array
min_score = np.min(scores)
max_score = np.max(scores)

# Normalise the scores using min-max normalisation
normalised_scores = (scores - min_score) / (max_score - min_score)

print("normalised scores (between 0 and 1):")
print(normalised_scores)

# Task 6 – Data Filtering

overall_mean = np.mean(scores)

# Extract all scores above the overall mean
scores_above_mean = scores[scores > overall_mean]
print("Scores above the overall mean:", scores_above_mean)

# 2. Count how many such scores exist
num_scores_above_mean = scores_above_mean.size
print("Number of scores above the overall mean:", num_scores_above_mean)

# Task 7 – Reflection

# 1. Why is NumPy more suitable than Python lists here?
# NumPy is more suitable than Python lists for this case because:
# - **Performance**: NumPy arrays are implemented in C, making operations like summing, averaging, and applying mathematical functions much faster than Python lists.
# - **Efficiency**: NumPy stores data in contiguous memory blocks, allowing for more efficient use of memory and faster access compared to Python lists.
# - **Ease of use**: NumPy provides powerful built-in functions (`np.mean`, `np.sum`, `np.min`, `np.max`, etc.) for easy and efficient computation across arrays, while with Python lists, you'd have to manually write loops to achieve the same functionality.
# - **Vectorized operations**: NumPy supports vectorized operations, meaning you can perform element-wise operations on entire arrays without needing explicit loops. For example, checking which scores are greater than the mean or normalizing scores across an entire array is straightforward with NumPy, while it would require complex loops with Python lists.



# 2. Which task would be hardest without NumPy?
# The task that would be hardest without NumPy is **Task 5 – Normalisation**.
# - Without NumPy, you'd have to manually loop over the entire array to find the minimum and maximum values, and then apply the normalisation formula to each element individually.
# - NumPy provides a straightforward, efficient way to perform the min-max normalisation with vectorized operations (i.e., `np.min()`, `np.max()`, and direct element-wise arithmetic).
# - Without NumPy, the process would require nested loops and a more complex implementation, which would be significantly slower and harder to read.
