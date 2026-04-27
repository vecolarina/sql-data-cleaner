# SQL Data Cleaner 🧹

A Python utility tool that connects to any MSSQL database and performs
automated data quality checks — detecting duplicates, null values, and
formatting issues across your tables.

Built by a working IT/Database specialist with real hospital and business
system experience.

---

## Features
- 🔍 Duplicate detection on any column
- 🕳️ Null value reporting across all columns
- 📧 Email format validation
- 📱 Philippine phone number format validation
- 🔤 Name formatting inconsistency detection
- 📊 Exports full report to Excel with separate sheets per issue

---

## Requirements
- Python 3.8+
- Microsoft SQL Server instance
- MSSQL user credentials with read access

---

## Installation

1. Clone the repository:
   git clone https://github.com/vecolarina/sql-data-cleaner.git
   cd sql-data-cleaner

2. Install dependencies:
   pip install -r requirements.txt

3. Configure your connection in cleaner.py:
   SERVER = "your_server_name"
   DATABASE = "your_database_name"
   USERNAME = "your_username"
   PASSWORD = "your_password"

4. Set the table and columns to check:
   TABLE_NAME = "your_table_name"
   EMAIL_COLUMN = "email"
   PHONE_COLUMN = "phone"
   NAME_COLUMN = "name"

5. Run:
   python cleaner.py

---

## Output
A full Excel report is generated in sample_report/ containing:
- Duplicates sheet — duplicate values and their count
- Null Values sheet — columns with null entries
- Invalid Emails sheet — incorrectly formatted emails
- Invalid Phones sheet — non-standard PH phone numbers
- Name Issues sheet — inconsistent name formatting

---

## Tech Stack
- Python 3
- pyodbc
- pandas
- openpyxl

---

## Use Cases
- Hospital patient record audits
- Business customer database cleanup
- Pre-migration data validation
- Regular automated data quality monitoring

---

Built by Von Adrian Colarina
Python Developer | IT Database Specialist
github.com/vecolarina