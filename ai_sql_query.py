import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import pymysql
from pymysql.cursors import DictCursor

# Load API Key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize AI Model
llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)

# Database Connection with Error Handling
try:
    conn = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="navi1399",
        database="orders_db",
        cursorclass=DictCursor  # Returns results as dictionaries
    )
    cursor = conn.cursor()
    print("✅ Database connection successful!")
except Exception as e:
    print(f"❌ Database connection failed: {e}")
    exit(1)

def generate_sql_query(prompt):
    sql_prompt = f"""
    Given the following user request, generate a SQL query for the `orders` table.
    Important: Ensure the query is safe and well-formed.
    User Request: "{prompt}"
    
    Use only the following column names:
    - `restaurant_name` (Name of the restaurant)
    - `cuisine_type` (Type of cuisine)
    - `cost_of_the_order` (Cost of each order)
    - `day_of_the_week` (Weekday of the order)
    - `rating` (Customer rating)
    - `food_preparation_time` (Time to prepare the food)
    - `delivery_time` (Time taken for delivery)

    Rules:
    - Use only valid SQL syntax.
    - Do NOT reference non-existent columns like `restaurant_id`.
    - Return only the SQL query.
    - No explanations or additional text.
    """
    response = llm.invoke(sql_prompt)
    return response.content.strip("`").strip()  # Ensure proper formatting



def execute_sql(query):
    cursor.execute(query)
    return cursor.fetchall()

def display_results(results):
    if not results:
        print("No results found.")
        return
    
    # Print column headers
    headers = results[0].keys()
    print("\n" + "-" * (15 * len(headers)))
    for header in headers:
        print(f"{header:<15}", end='')
    print("\n" + "-" * (15 * len(headers)))
    
    # Print rows
    for row in results:
        for value in row.values():
            print(f"{str(value):<15}", end='')
        print()
    print("\n" + "-" * (15 * len(headers)))

# User Interaction Loop
print("\n🤖 SQL Assistant Ready! Type 'exit' to quit.\n")

while True:
    try:
        user_prompt = input("\n🔍 Ask your question: ").strip()
        if user_prompt.lower() == "exit":
            break
        if not user_prompt:
            print("Please enter a valid question.")
            continue
            
        print("\n🤔 Generating SQL query...")
        sql_query = generate_sql_query(user_prompt)
        
        if not sql_query:
            print("❌ AI failed to generate a SQL query. Please try again.")
            continue

        print(f"\n📝 Generated SQL Query:\n{sql_query}\n")
        
        print("⚡ Executing query...")
        results = execute_sql(sql_query)
        print("\n📊 Results:")
        display_results(results)
        
    except Exception as e:
        print(f"❌ Error: {e}")

# Clean up
cursor.close()
conn.close()
print("\n👋 Thank you for using SQL Assistant!")
