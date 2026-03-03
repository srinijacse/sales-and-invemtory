import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="FMCG Sales Dashboard", layout="wide")

st.title("📊 Sales & Inventory Analytics Dashboard")

df = pd.read_csv("sales_data.csv")

df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

# Sidebar filters
st.sidebar.header("Filters")
region_filter = st.sidebar.multiselect("Select Region", df["Region"].unique(), default=df["Region"].unique())
category_filter = st.sidebar.multiselect("Select Category", df["Category"].unique(), default=df["Category"].unique())

filtered_df = df[(df["Region"].isin(region_filter)) & (df["Category"].isin(category_filter))]

# KPIs
total_revenue = filtered_df["Revenue"].sum()
top_product = filtered_df.groupby("Product")["Revenue"].sum().idxmax()
low_stock = filtered_df[filtered_df["Stock_Available"] < 100]

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹ {total_revenue:,.0f}")
col2.metric("Top Product", top_product)
col3.metric("Low Stock Items", len(low_stock))

st.subheader("📈 Monthly Revenue Trend")
filtered_df["Date"] = pd.to_datetime(filtered_df["Date"])
monthly = filtered_df.groupby(filtered_df["Date"].dt.month)["Revenue"].sum()

fig, ax = plt.subplots()
monthly.plot(kind="bar", ax=ax)
ax.set_ylabel("Revenue")
st.pyplot(fig)

st.subheader("⚠ Low Stock Products")
st.dataframe(low_stock[["Product", "Region", "Stock_Available"]])