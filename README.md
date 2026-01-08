# 🏆 ANTAM Gold Data & FAQ Repository

Repository ini berisi **dua komponen data utama PT Aneka Tambang Tbk (ANTAM)**:

1. 📊 **ANTAM Gold Transaction Data Generator**  
2. 📘 **FAQ PT Antam Knowledge Base**

Dirancang untuk kebutuhan **data engineering, analytics, business intelligence, machine learning, dan chatbot berbasis LLM (RAG)**.

---

## 📋 Overview

### 1️⃣ ANTAM Gold Transaction Data Generator
Script Python untuk **generate data transaksi penjualan emas ANTAM secara realistis** dengan volume besar.  
Dataset ini sangat cocok untuk:

- Simulasi **migrasi SQL Server → Databricks**
- Analisis penjualan & customer behavior
- Pembuatan dashboard BI
- Machine learning (forecasting & segmentation)
- Testing pipeline ETL & data quality

---

### 2️⃣ FAQ PT Antam Knowledge Base
Dataset **Frequently Asked Questions (FAQ)** PT Antam dalam format terstruktur (Excel), cocok untuk:

- Knowledge base chatbot
- Semantic search (sBERT / BERT)
- Dokumentasi bisnis
- Data dummy enterprise

---

## 🎯 Use Cases

### Data & Engineering
- Data Migration (SQL Server → Databricks)
- ETL Pipeline Testing
- Data Quality Validation
- Data Modeling & Star Schema

### Analytics & BI
- Sales performance analysis
- Revenue & profit monitoring
- Customer segmentation
- Power BI / Tableau / Looker dashboard

### AI & Machine Learning
- Sales forecasting
- Customer clustering
- NLP FAQ chatbot
- Retrieval Augmented Generation (RAG)

---

## 📊 Dataset 1: Gold Transaction Data

### 📦 Volume & Period
- **Total Records**: 100,000 transaksi
- **Periode**: 1 Januari 2025 – 31 Desember 2025
- **Format Output**: CSV, Parquet

---

### 🧱 Data Schema (24 Columns)

| Column Name | Type | Description |
|------------|------|-------------|
| transaction_id | String | ID unik transaksi (`TRX20250101000001`) |
| transaction_date | Date | Tanggal transaksi |
| transaction_time | Time | Waktu transaksi |
| customer_id | String | ID customer |
| customer_type | String | Individual, Corporate, Investor, Reseller, VIP |
| customer_region | String | Region / provinsi customer |
| product_id | String | Kode produk |
| product_name | String | Nama produk |
| product_category | String | Batangan / Perhiasan |
| purity_level | String | Kadar emas |
| quantity | Integer | Jumlah item |
| unit_price | Integer | Harga per unit |
| total_gross_amount | Integer | Total sebelum diskon |
| discount_amount | Integer | Diskon |
| tax_amount | Integer | PPN 11% |
| total_net_amount | Integer | Total akhir |
| payment_method | String | Cash, Debit, Credit, Transfer, E-Wallet |
| sales_channel | String | Store, Online, Mobile App, Reseller |
| branch_code | String | Kode cabang |
| cost_of_goods_sold | Integer | COGS |
| gross_profit | Integer | Laba kotor |
| year | Integer | Tahun |
| month | Integer | Bulan |
| quarter | Integer | Kuartal |

---

### 🏅 Product Catalog

#### Emas Batangan (7 SKU)
- 1g, 2g, 5g, 10g, 25g, 50g, 100g
- Kemurnian: **99.99%**
- Base price: **Rp1.100.000/gram**

#### Perhiasan (8 SKU)
- Cincin, Kalung, Gelang, Liontin, Anting
- Kemurnian: **70% – 75%**
- Berat bervariasi

---

### 💰 Business Rules

#### Pricing
- Dynamic Pricing: naik Rp800/hari
- Fluktuasi harga: -3% s/d +5%
- Pajak: PPN 11%

#### Discount Rules
- VIP: 5–15%
- Corporate: 3–10%
- Reseller: 2–8%
- Bulk (≥5 item): 2–5%
- Random Promo: 10% chance (1–3%)

#### Customer Distribution
- Individual: 50%
- Investor: 20%
- Corporate: 15%
- Reseller: 10%
- VIP: 5%

#### Product Mix
- Emas Batangan: 70%
- Perhiasan: 30%

---

## 📘 Dataset 2: FAQ PT Antam

### 🗂 Struktur Data

| Kolom | Deskripsi |
|-----|----------|
| No | Nomor urut |
| Kategori | Kategori FAQ |
| Pertanyaan | Pertanyaan pengguna |
| Jawaban | Jawaban informatif |

---

### 🏷 Kategori FAQ
- Informasi Umum
- Produk Logam Mulia
- Harga
- Tempat Pembelian
- Prosedur Pembelian
- Buyback
- Biaya dan Pajak
- Keaslian
- Penyimpanan
- Strategi Investasi
- Waktu Terbaik Membeli
- Pemula
- Wilayah Operasional
- Manajemen
- Kontak

📌 Total: **50+ FAQ, 15+ kategori**
