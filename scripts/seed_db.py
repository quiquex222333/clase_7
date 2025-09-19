import sqlite3, pathlib
from faker import Faker

db_path = pathlib.Path("data/testdata.db")
db_path.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS addresses (first TEXT, last TEXT, zip TEXT)")
cur.execute("DELETE FROM addresses")
fake = Faker("es_ES")
for _ in range(2):
    cur.execute("INSERT INTO addresses VALUES (?, ?, ?)",
                (fake.first_name(), fake.last_name(), fake.postcode()[:5]))
conn.commit()
conn.close()
print("DB seed ok.")
