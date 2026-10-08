class Student:
    def __init__(self,student_id,name):
        self.student_id= student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        total = 0

        for grade in self.grades:
            total += grade

        return total / len(self.grades)

    def check_honor(self):
        if self.calculate_average() >= 90:
            self.honor = True

    def delete_grade(self, index):
        del self.grades[index]

    def report(self):
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Grades Count:", len(self.grades))


def main():
    student = Student("x", "")

    student.add_grade(100)
    student.add_grade(50)

    student.calculate_average()
    student.check_honor()

    student.delete_grade(1)
    student.report()


if __name__ == "__main__":
    main()