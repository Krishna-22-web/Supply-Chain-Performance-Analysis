# ============================================================
# Project  : Supply Chain Performance Analysis
# Script   : eda_analysis.py
# Purpose  : EDA, KPI Summary, and Chart Generation
# Author   : Krishna S R
# Date     : 2026
# Tools    : Python 3, MySQL, Matplotlib, Seaborn, VS Code
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import os
import sys

# ============================================================
# CONFIGURATION
# Only change values in this section
# ============================================================

MYSQL_USER     = 'root'
MYSQL_PASSWORD = 'root@123'         # Your MySQL password
MYSQL_HOST     = 'localhost'
MYSQL_DB       = 'supply_chain_db'
TABLE_NAME     = 'supply_chain_data'
OUTPUT_DIR     = 'outputs'

# Chart settings
STYLE          = 'darkgrid'
DPI            = 150
COLOR_GREEN    = '#1D9E75'
COLOR_RED      = '#E24B4A'
COLOR_BLUE     = '#378ADD'
COLOR_ORANGE   = '#EF9F27'
COLORS_4       = ['#E24B4A', '#1D9E75', '#378ADD', '#EF9F27']

# ============================================================
# STEP 1 — CONNECT TO MYSQL AND LOAD DATA
# ============================================================

print("=" * 60)
print("  SUPPLY CHAIN PERFORMANCE ANALYSIS — EDA")
print("=" * 60)

print("\n[STEP 1] Connecting to MySQL and loading data...")

try:
    connection_str = (
        f"mysql+mysqlconnector://{MYSQL_USER}:{quote_plus(MYSQL_PASSWORD)}"
        f"@{MYSQL_HOST}/{MYSQL_DB}"
    )
    engine = create_engine(connection_str)
    df     = pd.read_sql(f"SELECT * FROM {TABLE_NAME}", engine)
    print(f"[INFO]  Data loaded        : {df.shape[0]:,} rows | {df.shape[1]} columns")

except Exception as e:
    print(f"[ERROR] Failed to load data : {e}")
    print("[INFO]  Make sure MySQL is running and load_data.py was executed first")
    sys.exit(1)

# ============================================================
# STEP 2 — PREPARE DATE COLUMNS
# ============================================================

print("\n[STEP 2] Preparing date columns...")

date_col = 'order date (DateOrders)'
if date_col in df.columns:
    df[date_col]      = pd.to_datetime(df[date_col], format='mixed', errors='coerce')
    df['Order Month'] = df[date_col].dt.to_period('M')
    df['Order Year']  = df[date_col].dt.year
    print("[INFO]  Date columns prepared : Order Month, Order Year created")

# ============================================================
# STEP 3 — KPI SUMMARY
# ============================================================

print("\n[STEP 3] Calculating KPIs...")

total_orders    = df['Order Id'].nunique()
total_revenue   = df['Sales'].sum()
total_profit    = df['Order Profit Per Order'].sum()
avg_ship_days   = df['Days for shipping (real)'].mean()
total_products  = df['Product Name'].nunique()
total_customers = df['Customer Id'].nunique()
total_markets   = df['Market'].nunique()
late_pct        = (df['Delivery Status'] == 'Late delivery').sum() / len(df) * 100
profit_margin   = (total_profit / total_revenue) * 100

print("\n" + "=" * 48)
print("  KEY PERFORMANCE INDICATORS")
print("=" * 48)
print(f"  Total Orders       : {total_orders:,}")
print(f"  Total Revenue      : ${total_revenue:,.2f}")
print(f"  Total Profit       : ${total_profit:,.2f}")
print(f"  Profit Margin      : {profit_margin:.2f}%")
print(f"  Avg Shipping Days  : {avg_ship_days:.1f} days")
print(f"  Total Products     : {total_products}")
print(f"  Total Customers    : {total_customers:,}")
print(f"  Markets Covered    : {total_markets}")
print(f"  Late Delivery Rate : {late_pct:.2f}%")
print("=" * 48)

# ============================================================
# STEP 4 — CREATE OUTPUT FOLDER
# ============================================================

os.makedirs(OUTPUT_DIR, exist_ok=True)
sns.set_style(STYLE)
print(f"\n[STEP 4] Output folder ready : {OUTPUT_DIR}/")

# ============================================================
# STEP 5 — CHART 1 : DELIVERY STATUS DISTRIBUTION
# ============================================================

print("\n[STEP 5] Generating Chart 1 — Delivery Status Distribution...")

delivery_counts = df['Delivery Status'].value_counts()

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(
    delivery_counts.index,
    delivery_counts.values,
    color=COLORS_4,
    edgecolor='white',
    linewidth=0.8
)

for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 500,
        f'{int(height):,}',
        ha='center', va='bottom',
        fontsize=10, fontweight='bold'
    )

ax.set_title('Order Delivery Status Distribution', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Delivery Status', fontsize=11)
ax.set_ylabel('Number of Orders', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
ax.tick_params(axis='x', rotation=15)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart1_delivery_status.png', dpi=DPI)
plt.close()
print(f"[INFO]  Saved : {OUTPUT_DIR}/chart1_delivery_status.png")

# ============================================================
# STEP 6 — CHART 2 : LATE DELIVERY BY SHIPPING MODE
# ============================================================

print("\n[STEP 6] Generating Chart 2 — Late Delivery by Shipping Mode...")

late_by_mode = (
    df.groupby('Shipping Mode')['Delivery Status']
    .apply(lambda x: (x == 'Late delivery').sum() / len(x) * 100)
    .reset_index()
)
late_by_mode.columns = ['Shipping Mode', 'Late Delivery %']
late_by_mode = late_by_mode.sort_values('Late Delivery %', ascending=False)

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(
    late_by_mode['Shipping Mode'],
    late_by_mode['Late Delivery %'],
    color=COLOR_RED,
    edgecolor='white',
    linewidth=0.8
)

for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f'{width:.2f}%',
        va='center', fontsize=10, fontweight='bold'
    )

ax.set_title('Late Delivery Rate by Shipping Mode', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Late Delivery %', fontsize=11)
ax.set_ylabel('Shipping Mode', fontsize=11)
ax.set_xlim(0, 110)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart2_late_shipping.png', dpi=DPI)
plt.close()
print(f"[INFO]  Saved : {OUTPUT_DIR}/chart2_late_shipping.png")

# ============================================================
# STEP 7 — CHART 3 : TOP 10 CATEGORIES BY PROFIT
# ============================================================

print("\n[STEP 7] Generating Chart 3 — Top 10 Categories by Profit...")

top_categories = (
    df.groupby('Category Name')['Order Profit Per Order']
    .sum()
    .nlargest(10)
    .reset_index()
)
top_categories.columns = ['Category', 'Total Profit']
top_categories = top_categories.sort_values('Total Profit', ascending=True)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(
    top_categories['Category'],
    top_categories['Total Profit'],
    color=COLOR_GREEN,
    edgecolor='white',
    linewidth=0.8
)

for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 2000,
        bar.get_y() + bar.get_height() / 2,
        f'${width:,.0f}',
        va='center', fontsize=9, fontweight='bold'
    )

ax.set_title('Top 10 Product Categories by Total Profit', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Total Profit ($)', fontsize=11)
ax.set_ylabel('Category', fontsize=11)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${int(x):,}'))
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart3_top_categories.png', dpi=DPI)
plt.close()
print(f"[INFO]  Saved : {OUTPUT_DIR}/chart3_top_categories.png")

# ============================================================
# STEP 8 — CHART 4 : MONTHLY REVENUE TREND
# ============================================================

print("\n[STEP 8] Generating Chart 4 — Monthly Revenue Trend...")

monthly_revenue = (
    df.groupby('Order Month')['Sales']
    .sum()
    .reset_index()
)
monthly_revenue['Order Month'] = monthly_revenue['Order Month'].astype(str)

fig, ax = plt.subplots(figsize=(13, 5))
ax.plot(
    monthly_revenue['Order Month'],
    monthly_revenue['Sales'],
    marker='o', color=COLOR_BLUE,
    linewidth=2, markersize=5
)
ax.fill_between(
    monthly_revenue['Order Month'],
    monthly_revenue['Sales'],
    alpha=0.1, color=COLOR_BLUE
)

ax.set_title('Monthly Revenue Trend (2015 - 2018)', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Month', fontsize=11)
ax.set_ylabel('Revenue ($)', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x/1e6:.1f}M'))
ax.tick_params(axis='x', rotation=90)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart4_monthly_trend.png', dpi=DPI)
plt.close()
print(f"[INFO]  Saved : {OUTPUT_DIR}/chart4_monthly_trend.png")

# ============================================================
# STEP 9 — CHART 5 : TOP 10 REGIONS BY REVENUE
# ============================================================

print("\n[STEP 9] Generating Chart 5 — Top 10 Regions by Revenue...")

top_regions = (
    df.groupby('Order Region')['Sales']
    .sum()
    .nlargest(10)
    .reset_index()
)
top_regions.columns = ['Region', 'Total Revenue']
top_regions = top_regions.sort_values('Total Revenue', ascending=True)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(
    top_regions['Region'],
    top_regions['Total Revenue'],
    color=COLOR_BLUE,
    edgecolor='white',
    linewidth=0.8
)

for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 10000,
        bar.get_y() + bar.get_height() / 2,
        f'${width/1e6:.2f}M',
        va='center', fontsize=9, fontweight='bold'
    )

ax.set_title('Top 10 Regions by Total Revenue', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Total Revenue ($)', fontsize=11)
ax.set_ylabel('Region', fontsize=11)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x/1e6:.1f}M'))
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart5_regional.png', dpi=DPI)
plt.close()
print(f"[INFO]  Saved : {OUTPUT_DIR}/chart5_regional.png")

# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("  EDA COMPLETE — SUMMARY")
print("=" * 60)
print(f"  Charts generated   : 5")
print(f"  Output folder      : {OUTPUT_DIR}/")
print(f"  chart1             : Delivery Status Distribution")
print(f"  chart2             : Late Delivery by Shipping Mode")
print(f"  chart3             : Top 10 Categories by Profit")
print(f"  chart4             : Monthly Revenue Trend")
print(f"  chart5             : Top 10 Regions by Revenue")
print("=" * 60)
print("\n[DONE] All charts saved. Ready for Power BI dashboard.")
