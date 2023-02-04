from flask import Flask, request, jsonify

app = Flask(__name__)

from routes.search import search_bp

# Client facing endpoints
app.register_blueprint(search_bp)

if __name__ == '__main__':
    app.run(debug=False, port=80, host="0.0.0.0")