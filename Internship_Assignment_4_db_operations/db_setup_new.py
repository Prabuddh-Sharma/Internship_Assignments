import sqlite3

create_table_weather = '''
CREATE TABLE IF NOT EXISTS weather_readings (
    reading_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name VARCHAR(100) NOT NULL,
    temperature REAL,
    feels_like REAL,
    humidity INTEGER,
    description VARCHAR(100),
    wind_speed REAL,
    country_code VARCHAR(10),
    timestamp INTEGER
)
'''

db_filename = 'operations_db.db'

conn = None
try:
    conn = sqlite3.connect(db_filename)
    print(f"SQLite version: {sqlite3.sqlite_version}")
    print(f"Connected to database: {db_filename}")

    cu = conn.cursor()
    cu.execute(create_table_weather)
    print("Table 'weather_readings' created successfully.")

    conn.commit()
    print("Database setup complete. 'weather_readings' table is ready.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")