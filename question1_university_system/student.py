from person import Person

class Student(Person):  # Abstract base class for students
	def __init__(self, name, student_id, department):
		super().__init__(name)
		self.student_id = student_id
		self.department = department
		self.courses = []
		self.__gpa = 0.0  # private attribute

	def enroll_course(self, course):  # enroll in a course if prerequisites are met and capacity allows
		if course.check_prerequisites(self):    # check if prerequisites are met
			if len(course.enrolled_students) < course.limit:  # check capacity
				self.courses.append(course.code)
				course.enrolled_students.append(self)
				print(f"{self.name} enrolled in {course.code}")  # successful enrollment
			else:
				print(f"Cannot enroll {self.name}: course {course.code} is full")  # course full
		else:
			print(f"Cannot enroll {self.name}: prerequisites not met for {course.code}")  # prerequisites not met

	def drop_course(self, course):  # drop a course
		if course.code in self.courses:  # check if enrolled
			self.courses.remove(course.code)
			course.enrolled_students.remove(self)
			print(f"{self.name} dropped {course.code}")

	def set_gpa(self, gpa):  # set GPA with validation
		if 0.0 <= gpa <= 4.0:
			self.__gpa = gpa
		else:
			raise ValueError("GPA must be between 0.0 and 4.0")  # validate GPA

	def calculate_gpa(self):  # return current GPA
		return self.__gpa

	def get_academic_status(self):  # determine academic status based on GPA (Dean's List, Probation, Good Standing)
		if self.__gpa >= 3.7:
			return "Dean's List"
		elif self.__gpa < 2.0:
			return "Probation"
		return "Good Standing"

	def get_responsibilities(self):  # override to specify student responsibilities
		return "Attend classes, complete assignments"

class Undergraduate(Student):  # Concrete class for undergraduate students
	def get_responsibilities(self):  # override to specify undergraduate responsibilities
		return "Attend lectures, participate in labs, complete assignments"

class Graduate(Student):  # Concrete class for graduate students
	def get_responsibilities(self):  # override to specify graduate responsibilities
		return "Conduct research, attend seminars, complete assignments"