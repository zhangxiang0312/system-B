class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def getName(self):
        return self.name

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} 選擇了課程: {course.getName()}")