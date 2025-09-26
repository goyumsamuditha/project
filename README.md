# project
This repository related to course work of PROGRAMMING FOR DATA SCIENCE 2025.1 BATCH
# University  Management System

This is an object-oriented model of a University management system implemented in Python. It demonstrates concepts like **inheritance**, **polymorphism**, and **encapsulation** to manage different entities within a university, such as **Courses**, **Departments**, **Students**, and **Faculty**.

## Project Structure

The system is organized into several Python files:

* **`person.py`**: Defines the base `Person` class and the `Staff` class.
* **`student.py`**: Defines the abstract `Student` class and concrete subclasses like `Undergraduate` and `Graduate`. Includes logic for course enrollment, dropping courses, and calculating academic status based on a **GPA** attribute.
* **`faculty.py`**: Defines the abstract `Faculty` class and concrete subclasses like `Professor`, `Lecturer`, and `TA`.
* **`department.py`**: Defines the `Department` and `Course` classes. The `Course` class includes logic for **prerequisite checking** and **enrollment limits**.
* **`main.py`**: The entry point of the application. It demonstrates the creation and interaction of all the core entities (Departments, Courses, Faculty, and Students).

## Key Features

* **Inheritance**: `Student`, `Faculty`, and `Staff` inherit from the base `Person` class.
* **Polymorphism**: The `get_responsibilities()` method is overridden in various subclasses to define specific roles.
* **Encapsulation**: The `__gpa` attribute in the `Student` class is kept private.
* **Business Logic**: Includes checks for course prerequisites and enrollment capacity.

## How to Run

### Prerequisites

* Python 3.9+

### Execution

1.  Ensure all Python files (`person.py`, `student.py`, `faculty.py`, `department.py`, `main.py`) are in the same directory.
2.  Open your terminal or command prompt.
3.  Navigate to the directory containing the files.
4.  Run the main script using the Python interpreter:

    ```bash
    python main.py
    ```

### Expected Output

The script will demonstrate the system's functionality, including:
* Successful and failed course enrollment attempts (due to prerequisites/capacity).
* The calculated GPA and resulting academic status for students.
* The specific responsibilities for each person type (Professor, Undergraduate, Staff, etc.).