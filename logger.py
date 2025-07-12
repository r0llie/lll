import os
from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    ua = request.headers.get('User-Agent')
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{time} - IP: {ip} - UA: {ua}")
    return "<h1>Logged!</h1>", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
