class Student:
    def __init__(self,student_id,name):
        self.student_id= student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grade(self, grade):
        if not isinstance(grade, (int, float)):
            print("Error: Grade must be numeric.")
            return False

        if grade < 0 or grade > 100:
            print("Error: Grade must be between 0 and 100.")
            return False

        self.grades.append(grade)
        return True

    def calculate_average(self):
        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"

    def check_passed(self):
        self.is_passed = self.calculate_average() >= 60
        return self.is_passed

    def check_honor(self):
        self.honor = self.calculate_average() >= 90
        return self.honor

    def delete_grade(self, index):
        if index < 0 or index >= len(self.grades):
            print("Error: Invalid grade index.")
            return False

        del self.grades[index]
        return True

    def report(self):
        average = self.calculate_average()
        letter = self.get_letter_grade()
        passed = self.check_passed()
        honor = self.check_honor()

        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Grades Count:", len(self.grades))
        print("Average:", round(average, 2))
        print("Letter Grade:", letter)
        print("Status:", "Passed" if passed else "Failed")
        print("Honor Roll:", "Yes" if honor else "No")


def main():
    student = Student("S001", "Steven")

    student.add_grade(95)
    student.add_grade(92)
    student.add_grade(90)

    student.delete_grade(2)

    student.report()


if __name__ == "__main__":
    main()