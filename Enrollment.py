class Enrollment:
    def __init__(self):
        self.enrollments = []

    def enroll_student(self, student, course):
        student.enroll(course)
        self.enrollments.append((student, course))

    def show_enrollments(self):
        print("選課記錄：")
        for student, course in self.enrollments:
            print(f"{student.getName()} 選擇了課程: {course.getCourseInfo()}")
