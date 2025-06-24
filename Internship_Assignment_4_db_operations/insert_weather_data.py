import sqlite3

d = {"coord":{"lon":75.8167,"lat":26.9167},
 "weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],
 "base":"stations",
 "main":{"temp":303.29,"feels_like":307.8,"temp_min":303.29,"temp_max":303.29,"pressure":1000,"humidity":67,"sea_level":1000,"grnd_level":953},
 "visibility":10000,
 "wind":{"speed":7.96,"deg":276,"gust":8.25},
 "clouds":{"all":100},
 "dt":1750653133,
 "sys":{"country":"IN","sunrise":1750637032,"sunset":1750686832},
 "timezone":19800,
 "id":1269515,
 "name":"Jaipur",
 "cod":200}

db_filename = 'operations_db.db'

conn = None
try:
    conn = sqlite3.connect(db_filename)
    print(f"Connected to database: {db_filename}")

    cu = conn.cursor()

    weather_data_insert = (
        d['name'],
        d['main']['temp'],
        d['main']['feels_like'],
        d['main']['humidity'],
        d['weather'][0]['description'],
        d['wind']['speed'],
        d['sys']['country'],
        d['dt']
    )

    insert_sql = '''
    INSERT INTO weather_readings (
        city_name, temperature, feels_like, humidity, description, wind_speed, country_code, timestamp
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    '''
    cu.execute(insert_sql, weather_data_insert)

    conn.commit()
    print("Weather data inserted successfully into 'weather_readings' table.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")