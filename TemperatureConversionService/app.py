from flask import Flask,request

app = Flask(__name__)

health = {"health" : "healthy"}

@app.route('/health')
def health_check():
    return health

@app.route('/toggle_health', methods = ['POST'])
def toggle_health():
    health["health"] = request.form.get("health")
    return health

@app.route('/')
def hello():
    return 'Temperature Converter Service'

@app.route('/<value>')
def temp_conversion(value):
    fah = float(value)*1.8 +32
    return str(fah)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8006, debug=True)