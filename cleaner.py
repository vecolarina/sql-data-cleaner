import pyodbc
import pandas as pd
from checks.duplicates import check_duplicates
from checks.nulls import check_nulls
from checks.format_check import check_email_format, check_phone_format, check_name_format

# ─── CONNECTION SETTINGS ──────────────────────────────────────
# Replace these with your actual MSSQL connection details
SERVER = "your_server_name"
DATABASE = "your_database_name"
USERNAME = "your_username"
PASSWORD = "your_password"

# ─── SETTINGS ─────────────────────────────────────────────────
# Set the table and columns you want to check
TABLE_NAME = "your_table_name"
EMAIL_COLUMN = "email"
PHONE_COLUMN = "phone"
NAME_COLUMN = "name"
DUPLICATE_COLUMN = "email"

REPORT_PATH = "sample_report/data_quality_report.xlsx"

# ─── MAIN ─────────────────────────────────────────────────────
def main():
    print("🚀 SQL Data Cleaner Starting...")
    print(f"📡 Connecting to {SERVER}/{DATABASE}...")

    try:
        conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};'
            f'SERVER={SERVER};'
            f'DATABASE={DATABASE};'
            f'UID={USERNAME};'
            f'PWD={PASSWORD}'
        )
        print("✅ Connected to MSSQL successfully.\n")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return

    # Run all checks
    print("─── Running Checks ───────────────────────────────────")
    duplicates_df = check_duplicates(conn, TABLE_NAME, DUPLICATE_COLUMN)
    nulls_df = check_nulls(conn, TABLE_NAME)
    invalid_emails_df = check_email_format(conn, TABLE_NAME, EMAIL_COLUMN)
    invalid_phones_df = check_phone_format(conn, TABLE_NAME, PHONE_COLUMN)
    name_issues_df = check_name_format(conn, TABLE_NAME, NAME_COLUMN)

    # Export all results to Excel
    print("\n─── Exporting Report ─────────────────────────────────")
    try:
        with pd.ExcelWriter(REPORT_PATH, engine='openpyxl') as writer:
            if not duplicates_df.empty:
                duplicates_df.to_excel(writer, sheet_name='Duplicates', index=False)
            if not nulls_df.empty:
                nulls_df.to_excel(writer, sheet_name='Null Values', index=False)
            if not invalid_emails_df.empty:
                invalid_emails_df.to_excel(writer, sheet_name='Invalid Emails', index=False)
            if not invalid_phones_df.empty:
                invalid_phones_df.to_excel(writer, sheet_name='Invalid Phones', index=False)
            if not name_issues_df.empty:
                name_issues_df.to_excel(writer, sheet_name='Name Issues', index=False)

        print(f"✅ Report exported to: {REPORT_PATH}")
    except Exception as e:
        print(f"❌ Error exporting report: {e}")

    conn.close()
    print("\n✅ SQL Data Cleaner Done.")

if __name__ == "__main__":
    main()