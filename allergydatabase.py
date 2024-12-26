import sqlite3
import requests
from bs4 import BeautifulSoup

# Set up the database
conn = sqlite3.connect('skincare_products.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS products
(id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT type UNIQUE,
 ingredients TEXT)
''')

conn.commit()

