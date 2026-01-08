import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed untuk reproducibility
np.random.seed(42)
random.seed(42)

# ========== KONFIGURASI ==========
TOTAL_ROWS = 100000
START_DATE = datetime(2024, 8, 1)  # Agustus 2024
END_DATE = datetime(2024, 12, 31)  # Desember 2024

# Supplier Data
SUPPLIERS = [
    {'id': 'SUP-001', 'name': 'PT Emas Nusantara', 'region': 'Jakarta', 'reliability': 0.95},
    {'id': 'SUP-002', 'name': 'CV Tambang Murni', 'region': 'Surabaya', 'reliability': 0.92},
    {'id': 'SUP-003', 'name': 'PT Logam Mulia Jaya', 'region': 'Bandung', 'reliability': 0.90},
    {'id': 'SUP-004', 'name': 'CV Emas Sejahtera', 'region': 'Medan', 'reliability': 0.88},
    {'id': 'SUP-005', 'name': 'PT Mineral Emas Indonesia', 'region': 'Jakarta', 'reliability': 0.93},
    {'id': 'SUP-006', 'name': 'UD Tambang Berkah', 'region': 'Kalimantan Timur', 'reliability': 0.85},
    {'id': 'SUP-007', 'name': 'PT Emas Prima', 'region': 'Semarang', 'reliability': 0.91},
    {'id': 'SUP-008', 'name': 'CV Logam Precious', 'region': 'Makassar', 'reliability': 0.87},
    {'id': 'SUP-009', 'name': 'PT Indo Gold Mining', 'region': 'Papua', 'reliability': 0.89},
    {'id': 'SUP-010', 'name': 'CV Emas Bersama', 'region': 'Yogyakarta', 'reliability': 0.86},
]

# Raw Material Types
RAW_MATERIALS = {
    'Refined Gold 99.99%': {
        'purity': '99.99%',
        'base_price_per_gram': 1020000,
        'quantity_range': (1, 10),  # kg
        'weight': 0.6  # 60% dari total pembelian
    },
    'Refined Gold 99.5%': {
        'purity': '99.5%',
        'base_price_per_gram': 1000000,
        'quantity_range': (2, 15),
        'weight': 0.25
    },
    'Gold Ore 95%': {
        'purity': '95%',
        'base_price_per_gram': 950000,
        'quantity_range': (5, 30),
        'weight': 0.10
    },
    'Gold Scrap 90%': {
        'purity': '90%',
        'base_price_per_gram': 900000,
        'quantity_range': (3, 20),
        'weight': 0.05
    }
}

# Payment Terms
PAYMENT_TERMS = ['Cash', 'Net 15', 'Net 30', 'Net 45', 'Net 60']

# Warehouse Locations
WAREHOUSE_LOCATIONS = [
    'Jakarta Pusat', 'Jakarta Utara', 'Surabaya', 'Bandung', 
    'Semarang', 'Medan', 'Makassar', 'Batam'
]

# Quality Check Status
QC_STATUS = ['Approved', 'Approved with Notes', 'Rejected']

# ========== FUNGSI HELPER ==========

def generate_random_date(start, end):
    """Generate random datetime between start and end"""
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

def generate_purchase_id(date, index):
    """Generate unique purchase ID"""
    return f"PUR{date.strftime('%Y%m%d')}{str(index).zfill(5)}"

def calculate_delivery_date(purchase_date, supplier_region):
    """Calculate delivery date based on distance"""
    # Jakarta & nearby: 1-3 days
    # Other Java: 2-5 days
    # Outside Java: 3-7 days
    if supplier_region in ['Jakarta', 'Bandung', 'Tangerang', 'Bekasi']:
        days = random.randint(1, 3)
    elif supplier_region in ['Surabaya', 'Semarang', 'Yogyakarta']:
        days = random.randint(2, 5)
    else:
        days = random.randint(3, 7)
    
    return purchase_date + timedelta(days=days)

def calculate_price_with_fluctuation(base_price, date):
    """Simulate gold price fluctuation"""
    # Trend naik seiring waktu
    days_from_start = (date - START_DATE).days
    trend = days_from_start * 500  # Naik Rp 500/hari
    
    # Random fluctuation ±2%
    fluctuation = base_price * random.uniform(-0.02, 0.02)
    
    return int(base_price + trend + fluctuation)

def determine_payment_status(qc_status, payment_terms, delivery_date):
    """Determine payment status based on QC and terms"""
    if qc_status == 'Rejected':
        return random.choice(['Cancelled', 'Dispute'])
    
    # Check if payment should be done based on delivery date
    days_since_delivery = (datetime.now() - delivery_date).days
    
    if payment_terms == 'Cash':
        return 'Paid'
    elif payment_terms == 'Net 15':
        return 'Paid' if days_since_delivery > 15 else random.choice(['Paid', 'Pending'])
    elif payment_terms == 'Net 30':
        return 'Paid' if days_since_delivery > 30 else random.choice(['Paid', 'Pending', 'Pending'])
    elif payment_terms == 'Net 45':
        return 'Paid' if days_since_delivery > 45 else random.choice(['Paid', 'Pending', 'Pending'])
    else:  # Net 60
        return 'Paid' if days_since_delivery > 60 else random.choice(['Paid', 'Pending', 'Pending', 'Pending'])

# ========== GENERATE DATA ==========

print("="*60)
print("🏭 GENERATING ANTAM PURCHASING DATA - 100K ROWS")
print("="*60)

data = []

for i in range(TOTAL_ROWS):
    # Random purchase date
    purchase_date = generate_random_date(START_DATE, END_DATE)
    
    # Select supplier (more frequently from reliable suppliers)
    supplier_weights = [s['reliability'] for s in SUPPLIERS]
    supplier = random.choices(SUPPLIERS, weights=supplier_weights)[0]
    
    # Select raw material type
    material_types = list(RAW_MATERIALS.keys())
    material_weights = [RAW_MATERIALS[m]['weight'] for m in material_types]
    raw_material_type = random.choices(material_types, weights=material_weights)[0]
    
    material_info = RAW_MATERIALS[raw_material_type]
    purity_level = material_info['purity']
    
    # Quantity in kg (larger purchases for refined gold)
    min_qty, max_qty = material_info['quantity_range']
    quantity_kg = round(random.uniform(min_qty, max_qty), 2)
    
    # Calculate price
    base_price_per_gram = material_info['base_price_per_gram']
    unit_price_per_gram = calculate_price_with_fluctuation(base_price_per_gram, purchase_date)
    
    # Total amount (quantity in kg * 1000 grams * price per gram)
    total_amount = int(quantity_kg * 1000 * unit_price_per_gram)
    
    # Payment terms (Cash for smaller amounts, Net terms for larger)
    if total_amount < 50000000:  # < 50 juta
        payment_terms = random.choices(
            PAYMENT_TERMS, 
            weights=[0.5, 0.3, 0.15, 0.03, 0.02]
        )[0]
    else:
        payment_terms = random.choices(
            PAYMENT_TERMS,
            weights=[0.1, 0.2, 0.35, 0.25, 0.1]
        )[0]
    
    # Delivery date
    delivery_date = calculate_delivery_date(purchase_date, supplier['region'])
    
    # Quality check status (reliable suppliers have higher approval rate)
    qc_weights = [
        supplier['reliability'],  # Approved
        (1 - supplier['reliability']) * 0.7,  # Approved with Notes
        (1 - supplier['reliability']) * 0.3   # Rejected
    ]
    quality_check_status = random.choices(QC_STATUS, weights=qc_weights)[0]
    
    # Payment status
    payment_status = determine_payment_status(quality_check_status, payment_terms, delivery_date)
    
    # Warehouse location (closer to supplier region if possible)
    if supplier['region'] in WAREHOUSE_LOCATIONS:
        warehouse_location = supplier['region']
    elif supplier['region'] in ['Papua', 'Kalimantan Timur']:
        warehouse_location = random.choice(['Surabaya', 'Makassar'])
    else:
        warehouse_location = random.choice(WAREHOUSE_LOCATIONS)
    
    # Date components
    year = purchase_date.year
    month = purchase_date.month
    quarter = (month - 1) // 3 + 1
    
    # Purchase order notes (optional)
    if quality_check_status == 'Approved with Notes':
        notes = random.choice([
            'Minor impurity detected',
            'Slight weight discrepancy',
            'Packaging issue',
            'Documentation incomplete'
        ])
    elif quality_check_status == 'Rejected':
        notes = random.choice([
            'Purity below specification',
            'Significant weight shortage',
            'Contamination detected',
            'Failed metallurgical test'
        ])
    else:
        notes = 'All checks passed'
    
    # Append to data
    data.append({
        'purchase_id': generate_purchase_id(purchase_date, i),
        'purchase_date': purchase_date.strftime('%Y-%m-%d'),
        'supplier_id': supplier['id'],
        'supplier_name': supplier['name'],
        'supplier_region': supplier['region'],
        'raw_material_type': raw_material_type,
        'purity_level': purity_level,
        'quantity_kg': quantity_kg,
        'unit_price_per_gram': unit_price_per_gram,
        'total_amount': total_amount,
        'payment_terms': payment_terms,
        'payment_status': payment_status,
        'delivery_date': delivery_date.strftime('%Y-%m-%d'),
        'warehouse_location': warehouse_location,
        'quality_check_status': quality_check_status,
        'qc_notes': notes,
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
df = df.sort_values('purchase_date').reset_index(drop=True)

# ========== SAVE TO FILES ==========

print("\n" + "="*60)
print("📊 DATA GENERATION COMPLETE!")
print("="*60)

# Save to CSV
csv_filename = 'antam_purchasing_100k.csv'
df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
print(f"✅ Saved to: {csv_filename}")

# Save to Parquet (untuk Databricks)
parquet_filename = 'antam_purchasing_100k.parquet'
df.to_parquet(parquet_filename, index=False)
print(f"✅ Saved to: {parquet_filename}")

# Save to Excel (optional - comment jika terlalu besar)
# excel_filename = 'antam_purchasing_100k.xlsx'
# df.to_excel(excel_filename, index=False, engine='openpyxl')
# print(f"✅ Saved to: {excel_filename}")

# ========== SUMMARY STATISTICS ==========

print("\n" + "="*60)
print("📈 SUMMARY STATISTICS")
print("="*60)

print(f"\n📋 Basic Info:")
print(f"Total Purchases: {len(df):,}")
print(f"Date Range: {df['purchase_date'].min()} to {df['purchase_date'].max()}")
print(f"Unique Suppliers: {df['supplier_id'].nunique()}")

print(f"\n💰 Financial Summary:")
print(f"Total Purchase Value: Rp {df['total_amount'].sum():,.0f}")
print(f"Average Purchase: Rp {df['total_amount'].mean():,.0f}")
print(f"Largest Purchase: Rp {df['total_amount'].max():,.0f}")
print(f"Smallest Purchase: Rp {df['total_amount'].min():,.0f}")

print(f"\n📦 Material Distribution:")
print(df['raw_material_type'].value_counts())

print(f"\n🏢 Top 5 Suppliers by Volume:")
top_suppliers = df.groupby(['supplier_id', 'supplier_name']).agg({
    'quantity_kg': 'sum',
    'total_amount': 'sum',
    'purchase_id': 'count'
}).rename(columns={'purchase_id': 'transactions'}).sort_values('total_amount', ascending=False).head()
print(top_suppliers)

print(f"\n✅ Quality Check Results:")
print(df['quality_check_status'].value_counts())
approval_rate = (df['quality_check_status'] == 'Approved').sum() / len(df) * 100
print(f"\nApproval Rate: {approval_rate:.2f}%")

print(f"\n💳 Payment Status:")
print(df['payment_status'].value_counts())

print(f"\n📊 Payment Terms Distribution:")
print(df['payment_terms'].value_counts())

print(f"\n🏭 Warehouse Distribution:")
print(df['warehouse_location'].value_counts())

print(f"\n📅 Monthly Purchase Volume:")
monthly_summary = df.groupby(['year', 'month']).agg({
    'quantity_kg': 'sum',
    'total_amount': 'sum',
    'purchase_id': 'count'
}).rename(columns={'purchase_id': 'transactions'})
print(monthly_summary)

print(f"\n📈 Quarterly Performance:")
quarterly_summary = df.groupby(['year', 'quarter']).agg({
    'quantity_kg': 'sum',
    'total_amount': 'sum',
    'purchase_id': 'count'
}).rename(columns={'purchase_id': 'transactions'})
print(quarterly_summary)

# Rejected purchases analysis
if (df['quality_check_status'] == 'Rejected').any():
    print(f"\n⚠️  Rejected Purchases Analysis:")
    rejected = df[df['quality_check_status'] == 'Rejected']
    print(f"Total Rejected: {len(rejected)} ({len(rejected)/len(df)*100:.2f}%)")
    print(f"Rejected Value: Rp {rejected['total_amount'].sum():,.0f}")
    print("\nTop reasons for rejection:")
    print(rejected['qc_notes'].value_counts())

print("\n" + "="*60)
print("🎉 DONE! Files generated successfully.")
print("="*60)

# Display sample data
print("\n📄 Sample Data (First 5 Rows):")
print(df.head().to_string())