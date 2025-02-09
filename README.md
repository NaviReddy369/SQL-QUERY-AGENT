📌 Project Title: AI-Powered SQL Data Pipeline & Query Automation
📁 Project Structure (Current)
bash
Copy
Edit
/codespaces-blank/
│── food_orders.csv       # Raw dataset (2000+ records)
│── load_csv.py           # Python script to load CSV into MySQL
│── python_mysql.py       # Script to test MySQL connection
│── settings.json         # VS Code settings
│── README.md             # Documentation (to be created)
│── .vscode/              # VS Code configurations
✅ Step 1: Setting Up MySQL Database
1️⃣ Installed MySQL Server & Started It
sh
Copy
Edit
sudo apt update
sudo apt install mysql-server
sudo service mysql start
2️⃣ Created MySQL User & Database
sql
Copy
Edit
CREATE DATABASE orders_db;
USE orders_db;
3️⃣ Created orders Table Schema
sql
Copy
Edit
CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,
    customer_id INT,
    restaurant_name VARCHAR(100),
    cuisine_type VARCHAR(50),
    cost_of_the_order DECIMAL(10,2),
    day_of_the_week VARCHAR(20),
    rating VARCHAR(20),   -- Fixed datatype issue (VARCHAR instead of INT)
    food_preparation_time INT,
    delivery_time INT
);
✅ Step 2: Installed Python & Dependencies
sh
Copy
Edit
pip install pandas pymysql sqlalchemy tqdm langchain openai
Python Libraries Used
Library	Purpose
pandas	Handling CSV data
pymysql	Connecting Python to MySQL
sqlalchemy	Handling SQL queries efficiently
tqdm	Progress tracking for large files
langchain	AI-powered query automation
openai	GPT-powered natural language SQL generation
✅ Step 3: Connected Python to MySQL
1️⃣ Python Script: python_mysql.py
python
Copy
Edit
import pymysql

HOST = "127.0.0.1"
USER = "root"
PASSWORD = "navi1399"
DATABASE = "orders_db"

try:
    conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    print("✅ MySQL Connection Successful!")
except pymysql.MySQLError as e:
    print(f"❌ MySQL Connection Failed: {e}")
✔ Run this to check connection:

sh
Copy
Edit
python python_mysql.py
✅ Step 4: Loaded CSV Data into MySQL
1️⃣ Python Script: load_csv.py
python
Copy
Edit
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# MySQL Connection
HOST = "127.0.0.1"
USER = "root"
PASSWORD = "navi1399"
DATABASE = "orders_db"

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}")

# Load CSV into Pandas DataFrame
csv_file = "food_orders.csv"
df = pd.read_csv(csv_file)

# Fixing Data Types
df["rating"] = df["rating"].astype(str)  # Ensure 'rating' is stored as text

# Insert Data into MySQL
df.to_sql('orders', con=engine, if_exists='append', index=False)

print("✅ Data successfully inserted into MySQL!")
✔ Run this to insert CSV data:

sh
Copy
Edit
python load_csv.py
✅ Step 5: Verified Data in MySQL
1️⃣ Check Row Count
sql
Copy
Edit
SELECT COUNT(*) FROM orders;
2️⃣ Preview Data
sql
Copy
Edit
SELECT * FROM orders LIMIT 10;
✔ Expected output: Sample data from the orders table.

🎯 Next Steps: Automating SQL Queries with LangChain
📌 Goal: Use AI to Generate SQL Queries from Natural Language
Integrate LangChain with MySQL 📡
Use OpenAI API to convert English to SQL queries 🤖
Create an AI-powered SQL Query Agent 🧠