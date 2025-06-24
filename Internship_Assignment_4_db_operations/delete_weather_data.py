import sqlite3

db_filename = 'operations_db.db'

conn = None
try:
    conn = sqlite3.connect(db_filename)
    cu = conn.cursor()
    print(f"Connected to database: {db_filename}")

    city_to_delete = 'Jaipur'
    delete_sql = '''
    DELETE FROM weather_readings
    WHERE city_name = ?
    '''
    cu.execute(delete_sql, (city_to_delete,))

    conn.commit()
    print(f"Successfully deleted record for city: '{city_to_delete}'.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")