##Create simple To Do app using Flask +sqlite3
from flask import Flask, render_template, request, redirect, url_for 
import sqlite3
app = Flask(__name__)
DATABASE = 'todo.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    todos = conn.execute('SELECT * FROM todos').fetchall()
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo_content = request.form['content']
    conn = get_db_connection()
    conn.execute('INSERT INTO todos (content) VALUES (?)', (todo_content,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    conn = get_db_connection()
    if request.method == 'POST':
        todo_content = request.form['content']
        conn.execute('UPDATE todos SET content = ? WHERE id = ?', (todo_content, todo_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    todo = conn.execute('SELECT * FROM todos WHERE id = ?', (todo_id,)).fetchone()
    conn.close()
    return render_template('edit.html', todo=todo)
@app.route('/toggle/<int:todo_id>', methods=['POST'])
def toggle_todo(todo_id):
    conn = get_db_connection()
    todo = conn.execute('SELECT completed FROM todos WHERE id = ?', (todo_id,)).fetchone()
    new_status = 0 if todo['completed'] else 1
    conn.execute('UPDATE todos SET completed = ? WHERE id = ?', (new_status, todo_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
    
def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            content TEXT NOT NULL,
            completed INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0',port=5000)
# Ensure the database and table exist
  
# To run the app, use the command: python app.py
# Access the app at http://127.0.0.1:5000/
# Make sure to have Flask installed: pip install Flask
# Make sure to have SQLite3 installed: pip install sqlite3
# The database file 'todo.db' will be created in the same directory as this script. 
# You can add, delete, and edit todos through the web interface.
