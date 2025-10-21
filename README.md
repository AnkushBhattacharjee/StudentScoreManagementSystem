Student Score Management System
A Python-based student score management system that uses SQLite database to store and analyze student records.
Features

Store student information (ID, Name, Age, Grade, Marks)
View all student records in a formatted table
Calculate and display data insights:

Average marks of all students
Highest marks achieved
Lowest marks achieved


SQLite database integration for persistent storage
Pandas DataFrame for efficient data manipulation

Technologies Used

Python 3.x
SQLite3 - Database management
Pandas - Data analysis and manipulation

Project Structure
StudentScoreManagementSystem/
│
├── student_system.py    # Main script to add student records
├── view_data.py        # Script to view and analyze student data
├── students.db         # SQLite database file
└── README.md          # Project documentation
Installation

Clone this repository:

bashgit clone https://github.com/AnkushBhattacharjee/StudentScoreManagementSystem.git
cd StudentScoreManagementSystem

Install required dependencies:

bashpip install pandas
Usage
Adding Student Records
Run student_system.py to add student information to the database:
bashpython student_system.py
Viewing Student Data
Run view_data.py to view all records and get data insights:
bashpython view_data.py
This will display:

All student records in table format
Average marks
Highest marks
Lowest marks

Database Schema
The students table contains the following columns:
ColumnTypeDescriptionidINTEGERPrimary KeynameTEXTStudent NameageINTEGERStudent AgegradeTEXTStudent Grade/ClassmarksINTEGERStudent Marks
Example Output
📊 Student Records in Table Format:

   id    name  age grade  marks
0   1   John   20     A     85
1   2   Jane   22     B     92
2   3   Doe    21     A     78

📈 Data Insights:

Average Marks: 85.00
Highest Marks: 92
Lowest Marks: 78
Future Enhancements

Add GUI interface using Tkinter
Implement update and delete operations
Add search functionality
Export data to CSV/Excel
Add data visualization with charts

Author
Ankush Bhattacharjee

Email: 2024ci_ankushbhattacharjee_@nie.ac.in
GitHub: @AnkushBhattacharjee

License
This project is open source and available for educational purposes.