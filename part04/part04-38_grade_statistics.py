stats = []
points_sum = 0
passed = 0
grade_counts = [0, 0, 0, 0, 0, 0]

while True:
    user_input = input("Exam points and exercises completed: ")
    
    if user_input == "":
        break

    # Extract the exam points and exercises completed by splitting input inline
    exam_pts, exercises = user_input.split()
    stats.append([int(exam_pts), int(exercises)])

def exercise_points(exercises: int):
    return exercises // 10

def calculate_grade(exam_pts, exercise_pts):
    if exam_pts < 10:
        return 0
    
    total_pts = exam_pts + exercise_pts

    if total_pts <= 14:
        return 0
    elif total_pts <= 17:
        return 1
    elif total_pts <= 20:
        return 2
    elif total_pts <= 23:
        return 3
    elif total_pts <= 27:
        return 4
    else:
        return 5
    
def grade_distribution(grades):
    for grade in range(5, -1, -1):
        print(f"{grade}: {'*' * grades[grade]}")

for exam_points, exercises in stats:
    exercise_pts = exercise_points(exercises)
    total_pts = exam_points + exercise_pts
    grade = calculate_grade(exam_points, exercise_pts)
    
    points_sum = points_sum + total_pts

    if grade > 0:
        passed += 1

    grade_counts[grade] += 1

average = points_sum / len(stats)
pass_pct = passed / len(stats) * 100

print("Statistics:")
print(f"Points average: {average:.1f}")
print(f"Pass percentage: {pass_pct:.1f}")
print("Grade distribution:")
grade_distribution(grade_counts)
