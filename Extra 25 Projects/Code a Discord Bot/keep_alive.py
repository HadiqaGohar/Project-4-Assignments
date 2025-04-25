# from flask import Flask
# from threading import Thread

# app = Flask('')

# @app.route('/')
# def home ():
#     return "Hello. I am alive!"

# def run():
#     app.run(host='0.0.0.0', port=8080)

# def keep_alive():
#     t = Thread(target=run)
#     t.start()


from flask import Flask, g
from threading import Thread
import sqlite3

# Initialize Flask app
app = Flask('')

# SQLite database setup
DATABASE = 'encouragements.db'

# Function to get the database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Function to close the database connection
@app.teardown_appcontext
def close_db(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return "Hello. I am alive!"

@app.route('/add_encouragement', methods=['POST'])
def add_encouragement():
    # You can modify this to accept user input, here we just add a static message
    message = "You are awesome!"
    
    # Insert into database
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO encouragements (message) VALUES (?)", (message,))
    db.commit()
    
    return "Encouragement added to database!"

@app.route('/get_encouragements')
def get_encouragements():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT message FROM encouragements")
    messages = cursor.fetchall()
    
    # Convert the results into a list of strings
    return '<br>'.join([msg[0] for msg in messages])

# Run the Flask app
def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
