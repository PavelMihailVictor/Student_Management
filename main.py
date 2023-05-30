


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            print("Student List:")
            for student in self.students:
                print("-" * 30)
                student.display_info()

    def main():
        sms = StudentManagementSystem()

        while True:
            print("\nStudent Management System")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter the student's name: ")
                age = int(input("Enter the student's age: "))
                grade = input("Enter the student's grade: ")
                student = Student(name, age, grade)
                sms.add_student(student)
                print("Student added successfully!")
            elif choice == "2":
                sms.display_students()
            elif choice == "3":
                print("Exiting Student Management System...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()