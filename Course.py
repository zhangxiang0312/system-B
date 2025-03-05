class Course:
    def __init__(self, course_id, name, teacher, day_of_week, period, course_type):
        self.course_id = course_id
        self.name = name
        self.teacher = teacher
        self.day_of_week = day_of_week
        self.period = period
        self.course_type = course_type

    def getName(self):
        return self.name

    def getTeacher(self):
        return self.teacher.getName()
    
    def getCourseInfo(self):
        return f"課程代號: {self.course_id}, 課程名稱: {self.name}, 授課老師: {self.teacher.getName()}, 禮拜: {self.day_of_week}, 第{self.period}節, 類型: {self.course_type}"


