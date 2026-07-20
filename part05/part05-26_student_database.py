def add_student(students: dict, name: str):
    students[name] = []

def print_student(students: dict, name: str):
    if name in students:
        curr_grade = 0

        print(f"{name}:")

        if len(students[name]) == 0:
            print(" no completed courses")
        else:
            print(f" {len(students[name])} completed courses:")
            for course, grade in students[name]:
                curr_grade += grade
                print(f"  {course} {grade}")

            if len(students[name]) == 0:
                print(f" average grade {0.0}")
            else:
                print(f" average grade {curr_grade / len(students[name])}")
    else:
        print(f"{name}: no such person in the database")

def add_course(students: dict, name: str, course: tuple):
    course_name, course_grade = course

    if course_grade == 0:
        return
    
    for index in range(len(students[name])):
        completed_name, completed_grade = students[name][index]

        if course_name == completed_name:
            if course_grade > completed_grade:
                students[name][index] = (course_name, course_grade)
            return
        
    students[name].append(course)

def summary(students: dict):
    print(f"students {len(students)}")

    most_courses = 0
    student_with_most_courses = ""

    best_average = 0
    student_with_best_average = ""

    for student in students:
        total_grade = 0

        if len(students[student]) > most_courses:
            most_courses = len(students[student])
            student_with_most_courses = student

        for course, grade in students[student]:
            total_grade += grade
        
        if len(students[student]) > 0:
            average = total_grade / len(students[student])

            if average > best_average:
                best_average = average
                student_with_best_average = student

    print(f"most courses completed {most_courses} {student_with_most_courses}")
    print(f"best average grade {best_average} {student_with_best_average}")