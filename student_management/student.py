class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        # here we have made grades as private/protected variable because we don't want users to provide random values to grades like "Eighty" or "Broken" which are not valid grades. So making it private forces user to provide or access it in a certain way and prevents from direct tampering.
        self.__grades = {}

    # here we have two parameters 'course_name' and 'grade' because we want to store grades as key-value pair so key=course_name and value=grade
    def add_grade(self, course_name, grade):
        self.__grades[course_name] = grade

    def get_grades(self):
        return self.__grades
    
    def get_average_grade(self):
        if self.__grades:
            return sum(self.__grades.values() / len(self.__grades))
        return 0
    
    def display_info(self):
        print(f"Student: {self.name} (ID: {self.student_id})")
        for course, grade in self.__grades.items():
            print(f" {course}: {grade}")
        print(f"Average: {self.get_average_grade():.}")