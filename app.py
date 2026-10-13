import os

import psycopg2
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            database=os.environ.get("DB_NAME", "flaskdb"),
            user=os.environ.get("DB_USER", "flaskuser"),
            password=os.environ.get("DB_PASSWORD", "flaskpass"),
        )
        cur = conn.cursor()
        cur.execute("SELECT 'Hola desde PostgreSQL con Docker Compose y Kubernetes!'")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result[0]
    except Exception as e:
        return f"Error conectando a la base de datos: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)