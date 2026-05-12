# ============================================================
# Project  : Supply Chain Performance Analysis
# Script   : load_data.py
# Purpose  : Load raw CSV -> Clean -> Save to MySQL + CSV
# Author   : Krishna S R
# Date     : 2026
# Tools    : Python 3, MySQL, VS Code
# ============================================================

import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import os
import sys

# ============================================================
# CONFIGURATION
# Only change values in this section
# ============================================================

CSV_PATH       = 'data/supply_chain_data.csv'
CLEANED_PATH   = 'data/supply_chain_cleaned.csv'
MYSQL_USER     = 'root'
MYSQL_PASSWORD = 'root@123'         # Your MySQL password
MYSQL_HOST     = 'localhost'
MYSQL_DB       = 'supply_chain_db'
TABLE_NAME     = 'supply_chain_data'
CHUNK_SIZE     = 500

# ============================================================
# STEP 1 — LOAD RAW CSV
# ============================================================

print("=" * 60)
print("  SUPPLY CHAIN PERFORMANCE ANALYSIS — Data Loader")
print("=" * 60)

print("\n[STEP 1] Loading raw CSV file...")

if not os.path.exists(CSV_PATH):
    print(f"[ERROR] File not found : {CSV_PATH}")
    print("[INFO]  Place supply_chain_data.csv inside the data/ folder")
    sys.exit(1)

df = pd.read_csv(CSV_PATH, encoding='unicode_escape')
print(f"[INFO]  Raw data loaded    : {df.shape[0]:,} rows | {df.shape[1]} columns")

# ============================================================
# STEP 2 — DATA CLEANING
# ============================================================

print("\n[STEP 2] Cleaning data...")

# 2a. Drop unnecessary columns
cols_to_drop = [
    'Customer Email',
    'Customer Password',
    'Product Description',
    'Product Image'
]
existing_cols = [c for c in cols_to_drop if c in df.columns]
df.drop(columns=existing_cols, inplace=True)
print(f"[INFO]  Columns dropped    : {len(existing_cols)} unnecessary columns removed")

# 2b. Fix date columns
date_cols = [
    'order date (DateOrders)',
    'shipping date (DateOrders)'
]
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], format='mixed', errors='coerce')
print("[INFO]  Date columns fixed  : format standardized")

# 2c. Fill missing values
if 'Order Zipcode' in df.columns:
    missing_zip = df['Order Zipcode'].isna().sum()
    df['Order Zipcode'] = df['Order Zipcode'].fillna('Unknown')
    print(f"[INFO]  Missing zipcodes   : {missing_zip:,} filled with 'Unknown'")

if 'Customer Lname' in df.columns:
    missing_name = df['Customer Lname'].isna().sum()
    df['Customer Lname'] = df['Customer Lname'].fillna('Unknown')
    print(f"[INFO]  Missing last names : {missing_name:,} filled with 'Unknown'")

# 2d. Remove duplicate rows
rows_before = len(df)
df.drop_duplicates(inplace=True)
rows_after  = len(df)
duplicates  = rows_before - rows_after
print(f"[INFO]  Duplicates removed  : {duplicates:,} rows dropped")

print(f"[INFO]  Cleaning complete   : {df.shape[0]:,} rows | {df.shape[1]} columns")

# ============================================================
# STEP 3 — SAVE CLEANED CSV
# ============================================================

print("\n[STEP 3] Saving cleaned CSV for Power BI...")

os.makedirs('data', exist_ok=True)

try:
    df.to_csv(CLEANED_PATH, index=False)
    print(f"[INFO]  Cleaned CSV saved   : {CLEANED_PATH}")
except Exception as e:
    print(f"[ERROR] Failed to save CSV : {e}")
    sys.exit(1)

# ============================================================
# STEP 4 — CONNECT TO MYSQL
# ============================================================

print("\n[STEP 4] Connecting to MySQL...")

try:
    # quote_plus safely encodes special characters in password
    # Example: root@123 becomes root%40123
    connection_str = (
        f"mysql+mysqlconnector://{MYSQL_USER}:{quote_plus(MYSQL_PASSWORD)}"
        f"@{MYSQL_HOST}/{MYSQL_DB}"
    )
    engine = create_engine(connection_str)

    with engine.connect() as conn:
        print(f"[INFO]  Connected to MySQL  : database = {MYSQL_DB}")

except Exception as e:
    print(f"[ERROR] MySQL connection failed : {e}")
    print("[INFO]  Check MYSQL_USER, MYSQL_PASSWORD and MYSQL_DB in config section")
    sys.exit(1)

# ============================================================
# STEP 5 — LOAD DATA INTO MYSQL
# ============================================================

print(f"\n[STEP 5] Loading {df.shape[0]:,} rows into MySQL...")
print("[INFO]  This may take 2-3 minutes. Please wait...")

try:
    df.to_sql(
        name      = TABLE_NAME,
        con       = engine,
        if_exists = 'replace',
        index     = False,
        chunksize = CHUNK_SIZE
    )
    print(f"[INFO]  Data loaded into    : table = {TABLE_NAME}")

except Exception as e:
    print(f"[ERROR] MySQL load failed : {e}")
    sys.exit(1)

# ============================================================
# STEP 6 — VERIFY ROW COUNT
# ============================================================

print("\n[STEP 6] Verifying MySQL load...")

try:
    result    = pd.read_sql(f"SELECT COUNT(*) AS total FROM {TABLE_NAME}", engine)
    row_count = result['total'][0]
    print(f"[INFO]  Rows in MySQL table : {row_count:,}")

    if row_count == df.shape[0]:
        print("[INFO]  Verification passed : CSV and MySQL row counts match")
    else:
        print(f"[WARNING] Row count mismatch : CSV = {df.shape[0]:,} | MySQL = {row_count:,}")

except Exception as e:
    print(f"[WARNING] Verification error : {e}")

# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("  LOAD COMPLETE — SUMMARY")
print("=" * 60)
print(f"  Raw rows loaded      : {rows_before:,}")
print(f"  Duplicates removed   : {duplicates:,}")
print(f"  Final rows           : {df.shape[0]:,}")
print(f"  Columns              : {df.shape[1]}")
print(f"  Cleaned CSV path     : {CLEANED_PATH}")
print(f"  MySQL database       : {MYSQL_DB}")
print(f"  MySQL table          : {TABLE_NAME}")
print("=" * 60)
print("\n[DONE] Next step : Run eda_analysis.py")
print("[DONE] Power BI  : Import supply_chain_cleaned.csv")
