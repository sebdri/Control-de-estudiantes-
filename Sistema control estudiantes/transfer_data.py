import csv
import csv
            


def export_data(file_path, students):
    if len(students)==0:
        print('Error,There is no data')
        return
    
    with open(file_path , "w", encoding='utf-8', newline='') as file:
        headers = students[0].keys()
        
        writer = csv.DictWriter(file, fieldnames= headers)

        writer.writeheader()

        writer.writerows(students)

        print("Data successfully exported.")



def import_data(file_path, students):
    try:
        with open(file_path, "r", encoding="utf-8", newline="") as file:

            reader = csv.DictReader(file)

            students.clear()

            for student in reader:
                student["spanish"] = int(student["spanish"])
                student["english"] = int(student["english"])
                student["social_studies"] = int(student["social_studies"])
                student["science"] = int(student["science"])
                student["average"] = float(student["average"])

                students.append(student)

        print("Data successfully imported.")
        return students

    except FileNotFoundError:
        print("No data has been previously exported.")
        return students