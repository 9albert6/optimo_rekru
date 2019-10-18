from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def fibbonaci_numbers() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'database',
        'port': '3306',
        'database': 'fibbonaci'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT fib_number FROM fibbonaci_numbers;')
    results = [fib_number for (fib_number) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'fibbonaci_numbers': fibbonaci_numbers()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')