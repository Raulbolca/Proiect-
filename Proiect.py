

import sqlite3

import jsonify as jsonify


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database/monitor_hours.db')
        self.create_tables()

    def create_tables(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                company TEXT NOT NULL,
                id_manager INTEGER,
                FOREIGN KEY (id_manager) REFERENCES employees(id)
            )
        ''')


    def insert_employee(self, name, surname, company, id_manager=None):
        self.conn.execute('''
            INSERT INTO employees (name, surname, company, id_manager)
            VALUES (?, ?, ?, ?)
        ''', (name, surname, company, id_manager))
        self.conn.commit()



class Employee:
    def __init__(self, id, name, surname, company, id_manager=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.company = company
        self.id_manager = id_manager

class Entry:
    def __init__(self, data, sens, id_person, id_porta):
        self.data = data
        self.sens = sens
        self.id_person = id_person
        self.id_porta = id_porta

import os
import shutil

class Gate:
    def __init__(self, gate_number):
        self.gate_number = gate_number

    def read_files(self,):
        entry_files = [f for f in os.listdir('entries') if f.startswith(f"Gate{self.gate_number}.")]
        for file in entry_files:
            file_path = os.path.join('entries', poarta1)
            with open(file_path, 'r') as f:
            backup_path= os.path.join('backup_entries', Poarta2)
            shutil.move(file_path, Poarta2)


app = Flask(__name__)

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.get_json()
    return jsonify({'message': 'Data received successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
# utils.py
import datetime
import smtplib

def calculate_hours_worked():

    pass

def send_email(recipient, subject, body):

    pass
