from django.test import TestCase

# Create your tests here.
import sqlite3

conn = sqlite3.connect("MapList.db")
cursor = conn.cursor()

cursor.execute('''SELECT name from Victims''')
names = cursor.fetchall()
print(names)