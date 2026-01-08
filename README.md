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
ColumnTypeDescriptiontransaction_idStringUnique ID (TRX20250101000001)transaction_dateDateTanggal transaksi (YYYY-MM-DD)transaction_timeTimeWaktu transaksi (HH:MM:SS)customer_idStringCustomer ID (IND10000, COR20000, etc)customer_typeStringIndividual, Corporate, Investor, Reseller, VIPcustomer_regionStringProvinsi customer (10 regions)product_idStringProduct code (BAT-001, PER-C01, etc)product_nameStringNama produk lengkapproduct_categoryStringBatangan / Perhiasanpurity_levelStringKadar emas (99.99%, 75%, 70%)quantityIntegerJumlah item dibeliunit_priceIntegerHarga per unit (Rupiah)total_gross_amountIntegerTotal sebelum diskondiscount_amountIntegerNilai diskontax_amountIntegerPPN 11%total_net_amountIntegerTotal setelah diskon + pajakpayment_methodStringCash, Debit, Credit, Transfer, E-Walletsales_channelStringStore, Online, Mobile App, Reseller, etcbranch_codeStringKode cabang (JKT-001, SBY-001, etc)cost_of_goods_soldIntegerCOGS (Rupiah)gross_profitIntegerLaba kotoryearIntegerTahun transaksimonthIntegerBulan (1-12)quarterIntegerKuartal (1-4)
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