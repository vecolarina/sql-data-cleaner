import pandas as pd

def check_nulls(conn, table_name):
    """
    Check for null values in all columns of a table.
    Returns a DataFrame showing null count per column.
    """
    query = f"""
        SELECT 
            COLUMN_NAME,
            SUM(CASE WHEN [{table_name}].[COLUMN_NAME] IS NULL 
                THEN 1 ELSE 0 END) as null_count
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = '{table_name}'
        GROUP BY COLUMN_NAME
        ORDER BY null_count DESC
    """
    try:
        # Alternative approach — more reliable across MSSQL versions
        df_table = pd.read_sql(f"SELECT * FROM [{table_name}]", conn)
        null_counts = df_table.isnull().sum().reset_index()
        null_counts.columns = ['column_name', 'null_count']
        null_counts = null_counts[null_counts['null_count'] > 0]
        null_counts = null_counts.sort_values('null_count', ascending=False)

        if null_counts.empty:
            print(f"✅ No null values found in {table_name}")
        else:
            print(f"⚠️ Found null values in {len(null_counts)} columns in {table_name}")
        return null_counts
    except Exception as e:
        print(f"❌ Error checking nulls: {e}")
        return pd.DataFrame()