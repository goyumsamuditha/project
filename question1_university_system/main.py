# main.py
from person import Staff
from student import Undergraduate, Graduate
from faculty import Professor, Lecturer, TA
from department import Department, Course

def main():
    # Create a department
    department_d1 = Department("Computer Science") # Department for CS courses

    # Create courses
    course_c01 = Course("PR100", "Introduction to Programming", 2) # Programming course
    course_c02 = Course("ML200", "Machine Learning", 2, prerequisites=["PR100"]) # ML course with PR100 as prerequisite

    # Assign courses to department
    department_d1.add_course(course_c01) # Add PR100 course to CS department
    department_d1.add_course(course_c02) # Add ML200 course to CS department

    # Create faculty
    lecturer_l001 = Lecturer("Nimal Perera", "MSc in Programming", 3) # Lecturer for PR100 course
    lecturer_l002 = Professor("Lihini Fernando", "PhD in Data Science", 2) # Professor for ML200 course
    teaching_assistant_ta001 = TA("Thilan Jayasinghe", "BSc in Data Science", 1) # TA for PR100 course
    staff_st001 = Staff("Kaushal Mendis") # Staff member

    # Assign faculty to department
    department_d1.add_faculty(lecturer_l001) # Add Lecturer to CS department
    department_d1.add_faculty(lecturer_l002) # Add Professor to CS department


    # Create students
    student_s001 = Undergraduate("Mihin Jayathilake", "CS001", "CS") # Undergraduate student in CS
    student_s002 = Graduate("Dilini Perera", "CS002", "CS") # Graduate student in CS

    print("\n--- Course Enrollment ---")
    # Enroll students in courses
    student_s001.enroll_course(course_c01) # should succeed
    student_s001.enroll_course(course_c02)  # prerequisite check

    student_s002.enroll_course(course_c02)  # should fail due to missing prerequisite


    # Set GPA
    student_s001.set_gpa(3.8)
    student_s002.set_gpa(2.0)


    # Show academic status
    print("\n--- Academic Status ---")
    print(f"{student_s001.name}: GPA: {student_s001.calculate_gpa()}, Status: {student_s001.get_academic_status()}") # Show academic status
    print(f"{student_s002.name}: GPA: {student_s002.calculate_gpa()}, Status: {student_s002.get_academic_status()}") # Show academic status


    print("\n--- Responsibilities ---")
    # Show responsibilities
    people = [lecturer_l001,lecturer_l002, student_s001, student_s002, teaching_assistant_ta001, staff_st001] # List of all people
    for person in people:
        print(f"{person.name}: {person.get_responsibilities()}") # Print responsibilities of each person

if __name__ == "__main__":
    main()
