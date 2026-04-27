import pandas as pd

def check_duplicates(conn, table_name, column):
    """
    Check for duplicate values in a specific column of a table.
    Returns a DataFrame with duplicate values and their count.
    """
    query = f"""
        SELECT [{column}], COUNT(*) as duplicate_count
        FROM [{table_name}]
        GROUP BY [{column}]
        HAVING COUNT(*) > 1
        ORDER BY duplicate_count DESC
    """
    try:
        df = pd.read_sql(query, conn)
        if df.empty:
            print(f"✅ No duplicates found in {table_name}.{column}")
        else:
            print(f"⚠️ Found {len(df)} duplicate values in {table_name}.{column}")
        return df
    except Exception as e:
        print(f"❌ Error checking duplicates: {e}")
        return pd.DataFrame()