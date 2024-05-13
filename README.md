# Student-Database-Management-Program

## Overview
This Python program provides a menu-driven interface for managing a student database using MySQL. Users can perform various operations such as creating tables, inserting rows, displaying student details, updating stipends, and deleting records.

## Prerequisites
- MySQL server running and accessible
- MySQL connector installed (`mysql-connector-python`)

## Setup
1. Ensure that the MySQL server is running.
2. Install the MySQL connector:
3. Update the connection details (`host`, `user`, `password`) in the script to match your MySQL server configuration.

## Functions

### `creating_table()`
- **Description**: Creates a table named `student` with columns for student details.

### `insert_rows()`
- **Description**: Inserts multiple rows into the `student` table based on user input.

### `new_row()`
- **Description**: Inserts a single row into the `student` table based on user input.

### `display_commerce()`
- **Description**: Displays details of all students in the `Commerce` stream.

### `display_entered_stream()`
- **Description**: Displays details of students belonging to a user-entered stream.

### `All_Students_Increating_table_Class_12()`
- **Description**: Lists the names of students who are in grade 12.

### `Details_All_Students_desc_order()`
- **Description**: Lists the details of all students sorted by average marks in descending order.

### `Stipend_notnull()`
- **Description**: Displays a report listing the name, stream, and annual stipend of students receiving a stipend.

### `Count_C_Grade()`
- **Description**: Counts the number of students with a grade of 'C'.

### `Name_start()`
- **Description**: Lists the names of students whose names start with 'V'.

### `update_stipend_300()`
- **Description**: Updates the stipend of medical students by 300 and displays the updated details.

### `Anil()`
- **Description**: Deletes the record of the student named 'Anil' and displays the remaining records.

## Menu Options

1. **Create the Table Student**:
- Creates the `student` table in the database.

2. **Insert Rows into the Table**:
- Prompts the user to input multiple rows and inserts them into the `student` table.

3. **Add a New Row to the Table**:
- Prompts the user to input a single row and inserts it into the `student` table.

4. **Display Details of Commerce Stream Students**:
- Displays the details of all students in the `Commerce` stream.

5. **Display Details of Students in a User-Entered Stream**:
- Prompts the user to input a stream and displays the details of students in that stream.

6. **List Names of Students in Grade 12**:
- Displays the names of students who are in grade 12.

7. **List Details of All Students Sorted by Average Marks in Descending Order**:
- Displays the details of all students sorted by average marks in descending order.

8. **Display Report of Name, Stream, and Annual Stipend**:
- Displays the name, stream, and annual stipend of students receiving a stipend.

9. **Count Students with Grade 'C'**:
- Counts and displays the number of students with a grade of 'C'.

10. **Display Names of Students Starting with 'V'**:
 - Displays the names of students whose names start with 'V'.

11. **Update Stipend of Medical Students by 300**:
 - Updates the stipend of medical students by 300 and displays the updated details.

12. **Delete the Record of Student Named 'Anil'**:
 - Deletes the record of the student named 'Anil' and displays the remaining records.

13. **Exit the Program**:
 - Exits the program.

## How to Run the Program

1. Run the script.
2. Follow the on-screen menu options.
3. Enter your choice (1-13) and input the required values as prompted.
4. The program will continue to prompt for input until you choose to exit by entering 13.
