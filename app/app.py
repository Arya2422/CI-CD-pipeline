# app/app.py
import os
from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# Load DB connection details from environment variables
DB_HOST = os.environ.get("MYSQL_HOST", "db")
DB_USER = os.environ.get("MYSQL_USER", "appuser")
DB_PASSWORD = os.environ.get("MYSQL_PASSWORD", "apppass")
DB_NAME = os.environ.get("MYSQL_DATABASE", "appdb")
DB_PORT = int(os.environ.get("MYSQL_PORT", 3306))


@app.route("/")
def home():
    return jsonify({"message": "✅ Flask + MySQL Docker Compose App is running!"})


@app.route("/db")
def db_connection():
    """Check MySQL database connectivity"""
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT,
            connect_timeout=5
        )
        with conn.cursor() as cur:
            cur.execute("SELECT NOW();")
            result = cur.fetchone()
        conn.close()
        return jsonify({"db_connection": "success", "current_time": str(result[0])})
    except Exception as e:
        return jsonify({"db_connection": "failed", "error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
