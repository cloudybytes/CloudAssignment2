from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Temperature Converter Service'

@app.route('/<value>')
def temp_conversion(value):
    fah = float(value)*1.8 +32
    return str(fah)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8006, debug=True)