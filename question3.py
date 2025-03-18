# Isabel Ojeda
# HW5 Q3

from abc import ABC, abstractmethod
class UniversityMember(ABC):
    num_members = 0 # static attribute 
    def __init__(self, name, member_id, email):
        self. name = name
        self.member_id = member_id 
        self.email = email
        UniversityMember.num_members += 1
    
    @abstractmethod
    def get_role(self):
        pass

class Student(UniversityMember):
    def __init__(self, name, member_id, email, major):
        super().__init__(name, member_id, email)
        self.major = major
    def get_role(self):
        "Student"
    def __str__(self):
        return f"{self.name} ({self.email}) - Major: {self.major}"

class Professor(UniversityMember):
    def __init__(self, name, member_id, email, department):
        super().__init__(name, member_id, email)
        self.departnment = department
    def get_role(self):
        "Professor"
    def __str__(self):
        last_name = self.name.split()[-1] 
        return f"Prof {last_name} ({self.email})"
    
class TA(UniversityMember):
    def __init__(self, name, member_id, email):
        super().__init__(name, member_id, email)
        self.courses_assisting = [] # attribute 
    def get_role(self):
        "TA"
    # method that takes as input a course and add to the field courses_assisting.
    def assign_to_courses(self, course):
        self.courses_assisting.append(course)
    def __str__(self):
        courses_list = ", ".join([c.name for c in self.courses_assisting])
        return f"{self.name} ({self.email}) TA for courses: {courses_list}"

# does not inherit from university member 
class Course: 
    def __init__(self, name, code):
        # instructors and students are added in methods 
        self.name = name
        self.code = code
        self.enrolled_students = []
        self.instructor = None 
    def add_student(self, student):
        # check if student belongs to Student class 
        if isinstance(student, Student):
            self.enrolled_students.append(student)
    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
    def add_instructor(self, professor):
        if isinstance(professor, Professor):
            self.instructor = professor
    def remove_instructor(self, professor):
        self.instructor = None 
    def __str__(self):
        students_list = ", ".join([s.name for s in self.enrolled_students])
        return f"Course: {self.name} ({self.code})\n Instructor: {self.instructor}\n Students: {students_list}\n TAs: {tas_list}"