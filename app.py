from flask import Flask, render_template

app = Flask(__name__)

if __name__=="__main__":
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboards-and-visualizations')
def dashboards():
    return render_template('dashboards.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/dashboards-and-visualizations/nonfatal-shootings-and-homicides/info')
def nonfatal_dash_info():
    return render_template('nonfatal_dash_info.html')

@app.route('/dashboards-and-visualizations/nonfatal-shootings-and-homicides/dashboard')
def nonfatal_dash():
    return render_template('nonfatal_dash.html', showFooter=False)