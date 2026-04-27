import pandas as pd
import re

def check_email_format(conn, table_name, column):
    """
    Check for invalid email formats in a specific column.
    Returns a DataFrame with invalid email entries.
    """
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    try:
        df = pd.read_sql(f"SELECT [{column}] FROM [{table_name}] WHERE [{column}] IS NOT NULL", conn)
        invalid = df[~df[column].astype(str).str.match(email_pattern)]
        
        if invalid.empty:
            print(f"✅ All email formats are valid in {table_name}.{column}")
        else:
            print(f"⚠️ Found {len(invalid)} invalid email formats in {table_name}.{column}")
        return invalid
    except Exception as e:
        print(f"❌ Error checking email format: {e}")
        return pd.DataFrame()

def check_phone_format(conn, table_name, column):
    """
    Check for invalid Philippine phone number formats.
    Valid formats: 09XXXXXXXXX or +639XXXXXXXXX
    """
    phone_pattern = r'^(09\d{9}|\+639\d{9})$'

    try:
        df = pd.read_sql(f"SELECT [{column}] FROM [{table_name}] WHERE [{column}] IS NOT NULL", conn)
        invalid = df[~df[column].astype(str).str.match(phone_pattern)]

        if invalid.empty:
            print(f"✅ All phone formats are valid in {table_name}.{column}")
        else:
            print(f"⚠️ Found {len(invalid)} invalid phone formats in {table_name}.{column}")
        return invalid
    except Exception as e:
        print(f"❌ Error checking phone format: {e}")
        return pd.DataFrame()

def check_name_format(conn, table_name, column):
    """
    Check for inconsistent name formatting (all caps, all lowercase, 
    extra spaces, numbers in names).
    """
    try:
        df = pd.read_sql(f"SELECT [{column}] FROM [{table_name}] WHERE [{column}] IS NOT NULL", conn)
        
        issues = df[
            df[column].astype(str).str.isupper() |
            df[column].astype(str).str.islower() |
            df[column].astype(str).str.contains(r'\d') |
            df[column].astype(str).str.contains(r'\s{2,}')
        ]

        if issues.empty:
            print(f"✅ No name formatting issues found in {table_name}.{column}")
        else:
            print(f"⚠️ Found {len(issues)} name formatting issues in {table_name}.{column}")
        return issues
    except Exception as e:
        print(f"❌ Error checking name format: {e}")
        return pd.DataFrame()