# Isabel Ojeda
# HW5 Q3 

from question3 import Student, Professor, TA, Course
if __name__ == '__main__': 
    # course object
    course = Course("Programming Paradigms", "CSE30332")
    
    # professor object
    professor = Professor("Prof. Santos", "100", "jdasilv2@nd.edu", "CSE")
    course.add_instructor(professor)
    
    # TA objects
    ta1 = TA("Micah Brody", "T1", "mbrody@nd.edu")
    ta1.assign_to_course(course)
    ta2 = TA("Sahil Khandelwal", "T2", "skhandel@nd.edu")
    ta2.assign_to_course(course)
    ta3 = TA("Kaixiang Zhao", "T3", "kzhao5@nd.edu")
    ta3.assign_to_course(course)
    ta4 = TA("Ella Gerzack", "T4", "egerczak@nd.edu")
    ta4.assign_to_course(course)
    
    # student objects
    student1 = Student("Isabel Ojeda", "S1", "iojeda@nd.edu", "CSE")
    course.add_student(student1)
    student2 = Student("Phoebe Huang", "S2", "phuang@nd.edu", "CSE")
    course.add_student(student2)
    student3 = Student("Sofia Rexach", "S3", "srexach@nd.edu", "CPEG")
    course.add_student(student3)

    print("\n")
    print(course)
    print("\n")
    print(professor)
    print("\n")
    print("TAS:")
    for ta in [ta1, ta2, ta3, ta4]:
        print(ta)
    print("\nStudents:")
    for s in [student1, student2, student3]:
        print(s)