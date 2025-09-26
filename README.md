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






#  Data Analysis: E-commerce Data Analysis Project

This project implements a **complete data pipeline** for book data — starting from **web scraping**, followed by **data cleaning**, **Exploratory Data Analysis (EDA)**, and **data visualization** to uncover actionable insights.

---

##  Features

- **Web Scraping:**  
  Scrapes book details such as title, price, rating, category, and availability from a target website.

- **Modular Design:**  
  Includes separate modules for different scraping tasks: `BookScraper`, `DemoScraper`, and `RSSItem`.

- **Data Cleaning:**  
  Notebook to handle missing values, format data types, and prepare the dataset for analysis.

- **Exploratory Data Analysis (EDA):**  
  Notebook to analyze book prices, ratings, and availability, and generate statistical summaries.

- **Data Visualization:**  
  Notebook to create informative plots — histograms, bar charts, scatter plots — for key variables.

---

##  Project Structure

| File/Directory           | Description |
|------------------------|-------------|
| **main.py**            | Main execution script. Runs all scrapers and saves raw data into CSV files. |
| **data_scraping.py**   | Contains the `BookScraper` class for scraping book data, including fetching page details. |
| **clean_books_data.ipynb** | Jupyter Notebook for cleaning and preprocessing `books_data.csv`. Saves cleaned data to `cleaned_books_data.csv`. |
| **EDA_Analysis.ipynb** | Jupyter Notebook for exploratory data analysis (EDA) on cleaned data. |
| **plots_vsulization.ipynb** | Jupyter Notebook for visualizing the cleaned data. |
| **books_data.csv**     | Output: Raw data scraped from the book website. |
| **cleaned_books_data.csv** | Output: Cleaned and preprocessed book dataset. |

---

## ⚙️ Getting Started

### Prerequisites
- **Python 3.9** installed on your system  

## How to Run

### 1. Web Scraping
Execute the main script to run the scrapers and generate the raw data CSV files (`books_data.csv`, `demo_data.csv`).

```bash
python main.py
```
(The BookScraper in main.py is configured to scrape 50 pages by default.)

## Data Cleaning and Analysis

After scraping the raw data, proceed with the data cleaning and analysis steps by opening the Jupyter notebooks in order:

### Clean the Data
Open and run all cells in the `clean_books_data.ipynb` notebook.  
This step generates the `cleaned_books_data.csv` file.

```bash
jupyter notebook clean_books_data.ipynb
```
### Perform EDA 

Open and run all cells in the EDA_Analysis.ipynb notebook.

### Visualize Data

Open and run all cells in the plots_vsulization.ipynb notebook to see the data visualizations.

