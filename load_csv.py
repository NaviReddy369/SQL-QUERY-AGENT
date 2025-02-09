import pandas as pd
import pymysql
from sqlalchemy import create_engine
from tqdm import tqdm

# Database Connection Details
HOST = "127.0.0.1"
USER = "root"
PASSWORD = "navi1399"
DATABASE = "orders_db"

# Create SQLAlchemy engine for MySQL
engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}")

# Load CSV into Pandas DataFrame
csv_file = "food_orders.csv"
df = pd.read_csv(csv_file)

# Convert `rating` to string to avoid datatype issues
df["rating"] = df["rating"].astype(str)

# Insert Data into MySQL
print("🚀 Uploading data to MySQL...")

try:
    df.to_sql('orders', con=engine, if_exists='append', index=False)
    print("✅ Data successfully inserted into MySQL!")
except Exception as e:
    print(f"❌ Data insertion failed: {e}")
