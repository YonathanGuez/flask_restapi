from flask import Flask
# instance Flask
app = Flask(__name__)

# Rooting
@app.route('/')
def hello_world():
    return 'Hello, World!'