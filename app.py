from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from my CI/CD powered Flask app! V1 samtha'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
