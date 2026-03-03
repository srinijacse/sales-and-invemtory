import pandas as pd
import random
from datetime import datetime, timedelta

products = [
    ("Nescafe", "Beverages", 10),
    ("Maggi", "Food", 5),
    ("KitKat", "Snacks", 8),
    ("Milkmaid", "Dairy", 12),
    ("Cerelac", "Baby Food", 15)
]

regions = ["North", "South", "East", "West"]

data = []

start_date = datetime(2025, 1, 1)

for i in range(120):
    date = start_date + timedelta(days=i)
    product = random.choice(products)
    units_sold = random.randint(50, 300)
    stock = random.randint(50, 500)

    data.append([
        date.strftime("%Y-%m-%d"),
        product[0],
        product[1],
        units_sold,
        product[2],
        random.choice(regions),
        stock
    ])

df = pd.DataFrame(data, columns=[
    "Date", "Product", "Category",
    "Units_Sold", "Unit_Price",
    "Region", "Stock_Available"
])

df.to_csv("sales_data.csv", index=False)
print("Dataset Created!")