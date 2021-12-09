from flask import Flask
import sqlite3
app = Flask('app')
conn = sqlite3.connect('database.db')
print ('Opened database successfully') ;

conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print('Table created successfully') 
conn.close()

@app.route('/')
def hello_world():
  return '<h1>Hello, World!</h1>'

app.run(host='0.0.0.0', port=8080)