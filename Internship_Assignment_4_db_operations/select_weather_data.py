import sqlite3

db_filename = 'operations_db.db'

conn = None
try:
    conn = sqlite3.connect(db_filename)
    print(f"Connected to database: {db_filename}")

    print("\n1. All weather data records:")
    data_records = conn.execute("SELECT * FROM weather_readings")
    for row in data_records:
        print(row)

    print("\n2. City name and Temperature for all records:")
    data_city_temps = conn.execute("SELECT city_name, temperature FROM weather_readings")
    for row in data_city_temps:
        print(row)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if conn:
        conn.close()
        print("\nDatabase connection closed.")