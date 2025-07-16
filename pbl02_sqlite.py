import sqlite3

# Koneksi ke database
conn = sqlite3.connect('mobil.db')
cursor = conn.cursor()

# CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS TBCars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    price REAL NOT NULL
)
""")
conn.commit()

# CREATE DATA (INSERT)
cursor.execute("""
INSERT INTO TBCars (brand, model, year, price)
VALUES ('Toyota', 'Avanza', 2020, 18000)
""")
conn.commit()

# READ DATA (SELECT)
cursor.execute("SELECT * FROM TBCars")
rows = cursor.fetchall()
print("DATA MOBIL:")
for row in rows:
    print(row)

# UPDATE DATA
cursor.execute("""
UPDATE TBCars SET price = 20000 WHERE id = 1
""")
conn.commit()

# DELETE DATA
cursor.execute("DELETE FROM TBCars WHERE id = 1")
conn.commit()

# Tutup koneksi
conn.close()
