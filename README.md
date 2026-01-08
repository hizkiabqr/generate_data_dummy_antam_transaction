🏆 ANTAM Gold Transaction Data Generator
📋 Overview
Script Python untuk generate data transaksi penjualan emas ANTAM secara realistis. Dataset ini cocok untuk simulasi migrasi dari SQL Server ke Databricks, analytics, dashboard, dan machine learning.
🎯 Use Cases

Data Migration: Simulasi migrasi SQL Server → Databricks
Data Analytics: Analisis penjualan, customer behavior, revenue
Dashboard BI: Power BI, Tableau, Looker
Machine Learning: Sales forecasting, customer segmentation
Testing: ETL pipeline, data quality validation

📊 Dataset Specifications
Volume

Total Records: 100,000 transaksi
Period: 1 Januari 2025 - 31 Desember 2025
File Formats: CSV, Parquet

Data Schema (24 Columns)
| Column Name        | Type    | Description                                                   |
| ------------------ | ------- | ------------------------------------------------------------- |
| transaction_id     | String  | Unique ID transaksi (contoh: `TRX20250101000001`)             |
| transaction_date   | Date    | Tanggal transaksi (format `YYYY-MM-DD`)                       |
| transaction_time   | Time    | Waktu transaksi (format `HH:MM:SS`)                           |
| customer_id        | String  | ID customer (contoh: `IND10000`, `COR20000`, dll)             |
| customer_type      | String  | Tipe customer: Individual, Corporate, Investor, Reseller, VIP |
| customer_region    | String  | Provinsi / region customer (±10 region)                       |
| product_id         | String  | Kode produk (contoh: `BAT-001`, `PER-C01`)                    |
| product_name       | String  | Nama produk lengkap                                           |
| product_category   | String  | Kategori produk: Batangan / Perhiasan                         |
| purity_level       | String  | Kadar emas (contoh: 99.99%, 75%, 70%)                         |
| quantity           | Integer | Jumlah item yang dibeli                                       |
| unit_price         | Integer | Harga per unit (Rupiah)                                       |
| total_gross_amount | Integer | Total sebelum diskon                                          |
| discount_amount    | Integer | Nilai diskon                                                  |
| tax_amount         | Integer | Pajak PPN 11%                                                 |
| total_net_amount   | Integer | Total akhir (setelah diskon + pajak)                          |
| payment_method     | String  | Metode pembayaran: Cash, Debit, Credit, Transfer, E-Wallet    |
| sales_channel      | String  | Channel penjualan: Store, Online, Mobile App, Reseller        |
| branch_code        | String  | Kode cabang (contoh: `JKT-001`, `SBY-001`)                    |
| cost_of_goods_sold | Integer | Harga pokok penjualan (COGS)                                  |
| gross_profit       | Integer | Laba kotor (`total_net_amount - COGS`)                        |
| year               | Integer | Tahun transaksi                                               |
| month              | Integer | Bulan transaksi (1–12)                                        |
| quarter            | Integer | Kuartal transaksi (1–4)                                       |

🏅 Product Catalog
Emas Batangan (7 SKU)

1 gram, 2 gram, 5 gram, 10 gram, 25 gram, 50 gram, 100 gram
Kemurnian: 99.99%
Base price: Rp 1.1 juta/gram

Perhiasan (8 SKU)

Cincin, Kalung, Gelang, Liontin, Anting
Kemurnian: 70% - 75%
Berat bervariasi per item

💰 Business Rules
Pricing

Dynamic Pricing: Harga naik Rp 800/hari (simulate trend)
Fluctuation: ±3% sampai +5% per transaksi
Tax: PPN 11% dari amount after discount

Discount Rules

VIP: 5-15% discount
Corporate: 3-10% discount
Reseller: 2-8% discount
Bulk Purchase (≥5 items): 2-5% discount
Random Promo: 10% chance dapat 1-3% discount

Customer Distribution

Individual: 50%
Investor: 20%
Corporate: 15%
Reseller: 10%
VIP: 5%

Product Mix

Emas Batangan: 70% transaksi
Perhiasan: 30% transaksi
