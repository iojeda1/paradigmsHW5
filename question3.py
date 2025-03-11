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
    def __init__(self, name, member_id, email, courses_assisting):
        self.courses_assisting = []
    def get_role(self):
        "TA"