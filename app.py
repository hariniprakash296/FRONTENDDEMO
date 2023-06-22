from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Displays the index page accessible at '/'
    '''
    
    return render_template('index.html')

@app.route("/liveChartPrediction")
def liveChartPrediction():
    '''
    Displays the index page accessible at '/'
    '''
    return render_template('liveChartPrediction.html')

@app.route('/liveChart')
def liveChart():
    return render_template('liveChart.php')

if __name__ == '__main__':
    app.run(debug=True)