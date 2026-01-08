import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed untuk reproducibility
np.random.seed(42)
random.seed(42)

# ========== KONFIGURASI ==========
TOTAL_ROWS = 100000
START_DATE = datetime(2025, 1, 1)  # Agustus 2025
END_DATE = datetime(2025, 12, 31)  # Desember 2025

# Produk ANTAM dengan Product ID
EMAS_BATANGAN = {
    'BAT-001': {'name': 'Emas Batangan 1 gram', 'weight': 1, 'category': 'Batangan', 'purity': '99.99%', 'base_price': 1100000, 'cogs': 1050000},
    'BAT-002': {'name': 'Emas Batangan 2 gram', 'weight': 2, 'category': 'Batangan', 'purity': '99.99%', 'base_price': 2200000, 'cogs': 2100000},
    'BAT-005': {'name': 'Emas Batangan 5 gram', 'weight': 5, 'category': 'Batangan', 'purity': '99.99%', 'base_price': 5500000, 'cogs': 5250000},
    'BAT-010': {'name': 'Emas Batangan 10 gram', 'weight': 10, 'category': 'Batangan', 'purity': '99.99%', 'base_price': 11000000, 'cogs': 10500000},
    'BAT-025': {'name': 'Emas Batangan 25 gram', 'weight': 25, 'category': 'Batangan', 'purity': '99.99%', 'base_price': 27500000, 'cogs': 26250000},
    'BAT-050': {'name': 'Emas Batangan 50 gram', 'weight': 50, 'category': 'Batangan', 'purity': '99.99%', 'base_price': 55000000, 'cogs': 52500000},
    'BAT-100': {'name': 'Emas Batangan 100 gram', 'weight': 100, 'category': 'Batangan', 'purity': '99.99%', 'base_price': 110000000, 'cogs': 105000000},
}

PERHIASAN = {
    'PER-C01': {'name': 'Cincin Emas Classic', 'weight': (2, 4), 'category': 'Perhiasan', 'purity': '75%', 'base_price_per_gram': 1250000, 'cogs_per_gram': 1100000},
    'PER-C02': {'name': 'Cincin Emas Modern', 'weight': (1.5, 3.5), 'category': 'Perhiasan', 'purity': '70%', 'base_price_per_gram': 1200000, 'cogs_per_gram': 1050000},
    'PER-K01': {'name': 'Kalung Emas Luxury', 'weight': (5, 12), 'category': 'Perhiasan', 'purity': '75%', 'base_price_per_gram': 1300000, 'cogs_per_gram': 1150000},
    'PER-K02': {'name': 'Kalung Emas Simple', 'weight': (3, 8), 'category': 'Perhiasan', 'purity': '70%', 'base_price_per_gram': 1250000, 'cogs_per_gram': 1100000},
    'PER-G01': {'name': 'Gelang Emas Classic', 'weight': (3, 8), 'category': 'Perhiasan', 'purity': '75%', 'base_price_per_gram': 1280000, 'cogs_per_gram': 1130000},
    'PER-G02': {'name': 'Gelang Emas Modern', 'weight': (2, 6), 'category': 'Perhiasan', 'purity': '70%', 'base_price_per_gram': 1230000, 'cogs_per_gram': 1080000},
    'PER-L01': {'name': 'Liontin Emas', 'weight': (1, 3), 'category': 'Perhiasan', 'purity': '75%', 'base_price_per_gram': 1320000, 'cogs_per_gram': 1170000},
    'PER-A01': {'name': 'Anting Emas', 'weight': (0.5, 2), 'category': 'Perhiasan', 'purity': '70%', 'base_price_per_gram': 1290000, 'cogs_per_gram': 1140000},
}

ALL_PRODUCTS = {**EMAS_BATANGAN, **PERHIASAN}

# Customer Types & Regions
CUSTOMER_TYPES = ['Individual', 'Corporate', 'Investor', 'Reseller', 'VIP']
CUSTOMER_REGIONS = [
    'DKI Jakarta', 'Jawa Barat', 'Jawa Timur', 'Jawa Tengah',
    'Sumatera Utara', 'Sumatera Selatan', 'Bali', 'Sulawesi Selatan',
    'Kalimantan Timur', 'Papua'
]

# Payment & Sales
PAYMENT_METHODS = ['Cash', 'Debit Card', 'Credit Card', 'Bank Transfer', 'E-Wallet']
# PAYMENT_STATUS = ['Paid', 'Pending', 'Failed']
SALES_CHANNELS = ['Store', 'Online', 'Mobile App', 'Reseller', 'Corporate', 'e-commerce']

# Branch Codes
BRANCH_CODES = [
    'JKT-001', 'JKT-002', 'JKT-003', 'SBY-001', 'BDG-001',
    'MDN-001', 'SMG-001', 'MKS-001', 'DPS-001', 'YGY-001'
]

# ========== FUNGSI HELPER ==========

def generate_random_date(start, end):
    """Generate random datetime between start and end"""
    delta = end - start
    random_days = random.randint(0, delta.days)
    random_seconds = random.randint(0, 86400)
    return start + timedelta(days=random_days, seconds=random_seconds)

def generate_transaction_id(date, index):
    """Generate unique transaction ID"""
    return f"TRX{date.strftime('%Y%m%d')}{str(index).zfill(6)}"

def generate_customer_id(customer_type):
    """Generate customer ID based on type"""
    prefix_map = {
        'Individual': 'IND',
        'Corporate': 'COR',
        'Investor': 'INV',
        'Reseller': 'RSL',
        'VIP': 'VIP'
    }
    prefix = prefix_map[customer_type]
    return f"{prefix}{random.randint(10000, 99999)}"

def calculate_price_with_fluctuation(base_price, date):
    """Simulate price fluctuation based on date"""
    days_from_start = (date - START_DATE).days
    trend = days_from_start * 800  # Trend naik Rp 800/hari
    fluctuation = random.uniform(-0.03, 0.05) * base_price  # -3% to +5%
    return int(base_price + trend + fluctuation)

def calculate_discount(customer_type, quantity, gross_amount):
    """Calculate discount based on customer type and quantity"""
    discount_rate = 0
    
    if customer_type == 'VIP':
        discount_rate = random.uniform(0.05, 0.15)  # 5-15%
    elif customer_type == 'Corporate':
        discount_rate = random.uniform(0.03, 0.10)  # 3-10%
    elif customer_type == 'Reseller':
        discount_rate = random.uniform(0.02, 0.08)  # 2-8%
    elif quantity >= 5:
        discount_rate = random.uniform(0.02, 0.05)  # 2-5% for bulk
    elif random.random() < 0.1:  # 10% chance promo
        discount_rate = random.uniform(0.01, 0.03)  # 1-3%
    
    return int(gross_amount * discount_rate)

# ========== GENERATE DATA ==========

data = []

for i in range(TOTAL_ROWS):
    # Random date
    trans_date = generate_random_date(START_DATE, END_DATE)
    
    # Customer info
    customer_type = random.choices(
        CUSTOMER_TYPES, 
        weights=[0.5, 0.15, 0.20, 0.10, 0.05]  # Individual paling banyak
    )[0]
    
    customer_id = generate_customer_id(customer_type)
    customer_region = random.choice(CUSTOMER_REGIONS)
    
    # Product selection (70% Batangan, 30% Perhiasan)
    if random.random() < 0.7:
        # Pilih dari Batangan
        weights = [0.35, 0.25, 0.15, 0.12, 0.07, 0.04, 0.02]
        product_id = random.choices(list(EMAS_BATANGAN.keys()), weights=weights)[0]
    else:
        # Pilih dari Perhiasan
        product_id = random.choice(list(PERHIASAN.keys()))
    
    product_info = ALL_PRODUCTS[product_id]
    product_name = product_info['name']
    product_category = product_info['category']
    purity_level = product_info['purity']
    
    # Quantity (lebih banyak beli 1-2 pcs)
    quantity = random.choices([1, 2, 3, 4, 5, 10], weights=[0.5, 0.25, 0.12, 0.07, 0.04, 0.02])[0]
    
    # Calculate prices
    if product_category == 'Batangan':
        base_unit_price = product_info['base_price']
        base_cogs = product_info['cogs']
    else:  # Perhiasan
        weight = round(random.uniform(product_info['weight'][0], product_info['weight'][1]), 2)
        base_unit_price = int(weight * product_info['base_price_per_gram'])
        base_cogs = int(weight * product_info['cogs_per_gram'])
    
    unit_price = calculate_price_with_fluctuation(base_unit_price, trans_date)
    cogs = calculate_price_with_fluctuation(base_cogs, trans_date)
    
    # Gross amount
    total_gross_amount = unit_price * quantity
    
    # Discount
    discount_amount = calculate_discount(customer_type, quantity, total_gross_amount)
    
    # Amount after discount
    amount_after_discount = total_gross_amount - discount_amount
    
    # Tax (11% PPN)
    tax_amount = int(amount_after_discount * 0.11)
    
    # Net amount
    total_net_amount = amount_after_discount + tax_amount
    
    # Payment
    payment_method = random.choice(PAYMENT_METHODS)
    # payment_status = random.choices(
    #     PAYMENT_STATUS,
    #     weights=[0.92, 0.05, 0.03]  # 92% Paid, 5% Pending, 3% Failed
    # )[0]
    
    # Sales channel
    if customer_type == 'Corporate':
        sales_channel = 'Corporate'
    elif customer_type == 'Reseller':
        sales_channel = 'Reseller'
    else:
        sales_channel = random.choices(
            ['Store', 'Online', 'Mobile App','e-commerce'],
            weights=[0.3, 0.25, 0.15, 0.3]
        )[0]
    
    branch_code = random.choice(BRANCH_CODES)
    
    # COGS & Gross Profit
    cost_of_goods_sold = cogs * quantity
    gross_profit = total_gross_amount - discount_amount - cost_of_goods_sold
    
    # Date components
    year = trans_date.year
    month = trans_date.month
    quarter = (month - 1) // 3 + 1
    
    # Append to data
    data.append({
        'transaction_id': generate_transaction_id(trans_date, i),
        'transaction_date': trans_date.strftime('%Y-%m-%d'),
        'transaction_time': trans_date.strftime('%H:%M:%S'),
        'customer_id': customer_id,
        'customer_type': customer_type,
        'customer_region': customer_region,
        'product_id': product_id,
        'product_name': product_name,
        'product_category': product_category,
        'purity_level': purity_level,
        'quantity': quantity,
        'unit_price': unit_price,
        'total_gross_amount': total_gross_amount,
        'discount_amount': discount_amount,
        'tax_amount': tax_amount,
        'total_net_amount': total_net_amount,
        'payment_method': payment_method,
        # 'payment_status': payment_status,
        'sales_channel': sales_channel,
        'branch_code': branch_code,
        'cost_of_goods_sold': cost_of_goods_sold,
        'gross_profit': gross_profit,
        'year': year,
        'month': month,
        'quarter': quarter
    })
    
    # Progress indicator
    if (i + 1) % 10000 == 0:
        print(f"Generated {i + 1:,} rows...")

# ========== CREATE DATAFRAME ==========

df = pd.DataFrame(data)

# Sort by date
df = df.sort_values(['transaction_date', 'transaction_time']).reset_index(drop=True)

# ========== SAVE TO FILES ==========

print("\n" + "="*60)
print("📊 DATA GENERATION COMPLETE!")
print("="*60)

# Save to CSV
csv_filename = 'antam_transactions_100k.csv'
df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
print(f"✅ Saved to: {csv_filename}")

# Save to Parquet (untuk Databricks)
parquet_filename = 'antam_transactions_100k.parquet'
df.to_parquet(parquet_filename, index=False)
print(f"✅ Saved to: {parquet_filename}")

# ========== SUMMARY STATISTICS ==========

print("\n" + "="*60)
print("📈 SUMMARY STATISTICS")
print("="*60)

print(f"\n📋 Basic Info:")
print(f"Total Rows: {len(df):,}")
print(f"Date Range: {df['transaction_date'].min()} to {df['transaction_date'].max()}")
print(f"Unique Customers: {df['customer_id'].nunique():,}")
print(f"Unique Products: {df['product_id'].nunique()}")

print(f"\n💰 Financial Summary:")
print(f"Total Gross Amount: Rp {df['total_gross_amount'].sum():,.0f}")
print(f"Total Discount: Rp {df['discount_amount'].sum():,.0f}")
print(f"Total Tax: Rp {df['tax_amount'].sum():,.0f}")
print(f"Total Net Amount: Rp {df['total_net_amount'].sum():,.0f}")
print(f"Total COGS: Rp {df['cost_of_goods_sold'].sum():,.0f}")
print(f"Total Gross Profit: Rp {df['gross_profit'].sum():,.0f}")
print(f"Avg Gross Profit Margin: {(df['gross_profit'].sum() / df['total_gross_amount'].sum() * 100):.2f}%")

print(f"\n🎯 Customer Distribution:")
print(df['customer_type'].value_counts())

print(f"\n📦 Product Category:")
print(df['product_category'].value_counts())

print(f"\n🏆 Top 5 Products:")
top_products = df.groupby('product_name').agg({
    'quantity': 'sum',
    'total_net_amount': 'sum'
}).sort_values('total_net_amount', ascending=False).head()
print(top_products)

print(f"\n🌍 Top Regions:")
region_sales = df.groupby('customer_region')['total_net_amount'].sum().sort_values(ascending=False)
print(region_sales)

# print(f"\n📊 Payment Status:")
# print(df['payment_status'].value_counts())

print(f"\n🏪 Sales Channel:")
print(df['sales_channel'].value_counts())

print(f"\n📅 Monthly Revenue:")
monthly_revenue = df.groupby(['year', 'month']).agg({
    'total_net_amount': 'sum',
    'transaction_id': 'count'
}).rename(columns={'transaction_id': 'transactions'})
print(monthly_revenue)

print(f"\n📈 Quarterly Performance:")
quarterly = df.groupby(['year', 'quarter']).agg({
    'total_net_amount': 'sum',
    'gross_profit': 'sum',
    'transaction_id': 'count'
}).rename(columns={'transaction_id': 'transactions'})
print(quarterly)

print("\n" + "="*60)
print("🎉 DONE! Files generated successfully.")
print("="*60)

# Display sample
print("\n📄 Sample Data (First 5 Rows):")
print(df.head().to_string())