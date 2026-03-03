from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        "message": "Hello from Flask! 🦊",
        "status": "ok",
        "version": "1.0.1"
    })

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "environment": "production"})

@app.route('/api/info')
def info():
    return jsonify({
        "app": "flask-demo",
        "author": "Max"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
