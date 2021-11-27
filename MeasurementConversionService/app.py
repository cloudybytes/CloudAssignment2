from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Measurement Converter Service from Kg to g'

@app.route('/<int:kg>')
def temp_conversion(kg):
    g = kg*1000
    time.sleep(5)
    return str(g)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8006, debug=True)