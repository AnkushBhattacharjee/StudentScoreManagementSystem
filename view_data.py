import sqlite3
import pandas as pd

# Connect to your existing database
conn = sqlite3.connect('students.db')

# Read the data into a Pandas DataFrame
df = pd.read_sql_query("SELECT * FROM students", conn)

print("\n📊 Student Records in Table Format:\n")
print("\n📈 Data Insights:")
print(df)
print(f"Average Marks: {df['marks'].mean():.2f}")
print(f"Highest Marks: {df['marks'].max()}")
print(f"Lowest Marks: {df['marks'].min()}")

conn.close()
