import sqlite3

db_filename = 'operations_db.db'

conn = None
try:
    conn = sqlite3.connect(db_filename)
    cu = conn.cursor()
    print(f"Connected to database: {db_filename}")

    new_temperature = 300.50
    city_to_update = 'Jaipur'

    update_sql = '''
    UPDATE weather_readings
    SET temperature = ?, feels_like = ?
    WHERE city_name = ?
    '''
    data_for_update = (new_temperature, new_temperature + 5, city_to_update)

    cu.execute(update_sql, data_for_update)

    conn.commit()
    print(f"Successfully updated temperature for '{city_to_update}'.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")