from person import Person


class Faculty(Person):  # Abstract base class for faculty
    def __init__(self, name, qualification, workload):
        super().__init__(name)
        self.qualification = qualification
        self.workload = workload

    def calculate_workload(self):  # return workload
        return f"Workload: {self.workload} courses"

    def get_responsibilities(self):  # override to specify faculty responsibilities
        return "Teach courses, mentor students"


class Professor(Faculty):  # Concrete class for professors
    def get_responsibilities(self):  # override to specify professor responsibilities
        return "Conduct research, teach advanced courses, mentor graduate students"


class Lecturer(Faculty):  # Concrete class for lecturers
    def get_responsibilities(self):  # override to specify lecturer responsibilities
        return "Teach undergraduate courses, develop curriculum"


class TA(Faculty):  # Concrete class for teaching assistants
    def get_responsibilities(self):  # override to specify TA responsibilities
        return "Assist in teaching, grade assignments, hold office hours"

