import pandas as pd
import psycopg2

data = pd.read_csv('/path/to/transformed.csv')
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS mytable")
cur.execute("""
    CREATE TABLE mytable (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        age INTEGER
    )
""")

for row in data.itertuples(index=False):
    cur.execute("INSERT INTO mytable (name, age) VALUES (%s, %s)", (row.name, row.age))

conn.commit()
cur.close()
conn.close()
