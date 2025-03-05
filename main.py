from Teacher import Teacher
from Student import Student
from Enrollment import Enrollment
from Course import Course

if __name__ == "__main__":
    teacher1 = Teacher("王老師")
    teacher2 = Teacher("李老師")

    course1 = Course("CSE101", "數學", teacher1, "Monday", 1, "必修")
    course2 = Course("CSE102", "英文", teacher2, "Tuesday", 2, "選修")

    student1 = Student("小明")
    student2 = Student("小華")

    enrollment_system = Enrollment()

    enrollment_system.enroll_student(student1, course1)
    enrollment_system.enroll_student(student2, course2)
    enrollment_system.enroll_student(student1, course2)

    enrollment_system.show_enrollments()