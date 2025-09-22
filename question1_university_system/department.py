class Course: # Represents a course in the university
    def __init__(self, code, title, credits, prerequisites=None,limit=30): # prerequisites is a list of course codes
        self.code = code
        self.title = title
        self.credits = credits
        self.enrolled_students = [] # List of student IDs
        self.prerequisites = prerequisites if prerequisites else [] # List of prerequisite course codes
        self.limit = limit

    def check_prerequisites(self, student): # Check if a student meets the prerequisites
        return all(prereq in student.courses for prereq in self.prerequisites)


class Department: # Represents a department in the university
    def __init__(self, name: str):
        self.name = name
        self.courses: List[Course] = []
        self.faculty: List[str] = []  # Specify type of faculty, e.g., List[str] for faculty names

    def add_course(self, course: Course): # Add a course to the department
        self.courses.append(course)

    def add_faculty(self, faculty: str): # Add a faculty member to the department
        self.faculty.append(faculty)
