from New_menu import show_menu
from Students_entry_data import add_student, show_students_data, student_top_three, obtain_all_average
import transfer_data

def main():
    students = []

    while True:
        option = show_menu()

        if option == 1:
            student = add_student()
            students.append(student)
            
            print("\nStudent successfully added\n")

        elif option == 2:
            show_students_data(students)
            

        elif option == 3:
            student_top_three(students) 
         

        elif option == 4:
            obtain_all_average(students)

        elif option == 5:
            transfer_data("export.csv",students)

        elif option == 6:
            
            students = transfer_data("export.csv", students)
            show_students_data(students)

        elif option == 7:
            print("Thanks for using our sistem")
            break


if __name__ == "__main__":
    main()

