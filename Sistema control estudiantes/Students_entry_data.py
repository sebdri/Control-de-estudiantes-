def add_student():

    name = input("Add the students name: ")
    section = input("Add students sectiomn ")

    while True:
        try:
            spanish = int(input("Please add the spanish score: "))
            if 0 <= spanish <= 100:
                break
            else:
                print("The score needs to be between 0 & 100.")
        except ValueError:
            print("Inavalid data.")

    while True:
        try:
            english = int(input("Please add the english score: "))
            if 0 <= english <= 100:
                break
            else:
                print("The score needs to be between 0 & 100.")
        except ValueError:
            print("Inavalid data.")

    while True:
        try:
            social_studies = int(input("Please add the social studies score: "))
            if 0 <= social_studies <= 100:
                break
            else:
                print("The score needs to be between 0 & 100.")
        except ValueError:
            print("Inavalid data.")

    while True:
        try:
            science = int(input("Please add the science score: "))
            if 0 <= science <= 100:
                break
            else:
                print("The score needs to be between 0 & 100.")
        except ValueError:
            print("Inavalid data.")

    average = (spanish + english + social_studies + science) / 4

    student = {
        "student": name,
        "section": section,
        "spanish": spanish,
        "english": english,
        "social_studies": social_studies,
        "science": science,
        "average": average
    }

    return student


def show_students_data(students):
    if len(students) == 0:
        print("No students added yet.")
        return

    for student in students:
        print("\n----------------------------")
        print(f'student: {student["student"]}')
        print(f'section: {student["section"]}')
        print(f'spanish: {student["spanish"]}')
        print(f'english: {student["english"]}')
        print(f'social_studies: {student["social_studies"]}')
        print(f'science: {student["science"]}')
        print(f'average: {student["average"]}')

    


def student_top_three(students):
    if len(students) == 0:
        print("No students registered.")
        return

    top_three = sorted(
        students,
        key=lambda student:student["average"],
        reverse=True
    )

    print("\nTop 3 students")

    for student in top_three[:3]:
        print(f'{student["student"]} - Average: {student["average"]}')


def obtain_all_average(students):
    average = 0

    if len(students)==0:
        print ("You'll have to add data before been able to use this functionality 😞")
        return
    
    all_students = 0

    for student in students:
        all_students+= (student["average"])
    
    general_avarage = all_students / len(students)

    print(f'The general avarage is:{general_avarage}')