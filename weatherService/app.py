import csv
from flask import Flask, request

app = Flask(__name__)

health = {"health" : "healthy"}

@app.route('/health')
def health_check():
    return health

@app.route('/toggle_health', methods = ['POST'])
def toggle_health():
    print(request.form.get("health"))
    health["health"] = request.form.get("health")
    return health
    
@app.route('/')
def weather_forecast():


    with open('forecast_data.csv','r') as file:
        CSVText = csv.reader(file)
        RowIndex = 0

    # The first row contain the headers and the additional rows each contain the weather metrics for a single day
    # To simply our code, we use the knowledge that column 0 contains the location and column 1 contains the date.  The data starts at column 4
        for Row in CSVText:
            if RowIndex == 0:
                FirstRow = Row
            else:
                print('Weather in ', Row[0], ' on ', Row[1])

                ColIndex = 0
                for Col in Row:
                    if ColIndex >= 4:
                        print('   ', FirstRow[ColIndex], ' = ', Row[ColIndex])
                    ColIndex += 1
            RowIndex += 1

        # If there are no CSV rows then something fundamental went wrong
        if RowIndex == 0:
            print('Sorry, but it appears that there was an error connecting to the weather server.')
            print('Please check your network connection and try again..')

        # If there is only one CSV  row then we likely got an error from the server
        if RowIndex == 1:
            print('Sorry, but it appears that there was an error retrieving the weather data.')
            print('Error: ', FirstRow)

    print()
    return "hello!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8005, debug=True)