from faker import Faker
import csv
import random
from datetime import datetime, timedelta

fake = Faker()
rows = 10000
start_date = datetime(2024, 1, 1)
products = [f"PROD_{i:03d}" for i in range(1, 101)]  # 100 products: PROD_001 to PROD_100
stores = [f"STORE_{i:02d}" for i in range(1, 21)]    # 20 stores: STORE_01 to STORE_20

with open('retail_sales_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['product_id', 'date', 'sales_amount', 'store_id'])
    for _ in range(rows):
        date = start_date + timedelta(days=random.randint(0, 364))
        writer.writerow([
            random.choice(products),
            date.strftime('%Y-%m-%d'),
            round(random.uniform(10.0, 500.0), 2),
            random.choice(stores)
        ])

print("Generated retail_sales_data.csv with 10,000 rows.")