from flask import Flask, render_template
import csv
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Displays the index page accessible at '/'
    '''
    def read_csv(filename):
        data = {}
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for column, value in row.items():
                    if column not in data:
                        data[column] = []
                        data[column].append(float(value))
        return data

    data = read_csv('historical_data.csv')
    print(data)
    print(data.keys())  # Print the available column names

    x = data['Open']  # Replace 'Open' with the correct column name containing x-axis values
    y = data['Close']  # Replace 'Close' with the correct column name containing y-axis values

    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.xlabel('Open')
    plt.ylabel('Close')
    plt.title('CSV Data')
    plt.grid(True)
    plt.savefig('static/graph.png')  # Save the graph as a static file
    
    return render_template('index.html')

@app.route("/StockSummary")
def StockSummary():
    '''
    Displays the index page accessible at '/'
    '''
    return render_template('StockSummary.html')

@app.route("/liveChartPrediction")
def liveChartPrediction():
    '''
    Displays the index page accessible at '/'
    '''
    return render_template('liveChartPrediction.html')

@app.route('/Statistics')
def Statistics():
    '''
    Displays the index page accessible at '/'
    '''
    return render_template('Statistics.html')

@app.route('/CompanyProfile')
def CompanyProfile():
    '''
    Displays the index page accessible at '/'
    '''
    return render_template('CompanyProfile.html')

@app.route('/Analysis')
def Analysis():
    '''
    Displays the index page accessible at '/'
    '''
    return render_template('Analysis.html')

@app.route('/OtherExpPred')
def OtherExpPred():
    '''
    Displays the index page accessible at '/'
    '''
    return render_template('OtherExpPred.html')

if __name__ == '__main__':
    app.run(debug=True)