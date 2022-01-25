from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.context_processor
def inject_now():
    return {'current_year': datetime.utcnow().strftime("%Y")}

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
    return render_template('nonfatal_dash.html')

@app.route('/dashboards-and-visualizations/hospital-intervention-response-to-shootings/dashboard')
def hospital_interven():
    return render_template('no_dash_placeholder.html')

@app.route('/dashboards-and-visualizations/hospital-intervention-response-to-shootings/info')
def hospital_interven_info():
    return render_template('no_info_placeholder.html')

# Hospital Emergency Room Data for Assault-Related Injuries
@app.route('/dashboards-and-visualizations/hospital-emergency-room-data-for-assault-related-injuries/dashboard')
def hospital_emergen():
    return render_template('no_dash_placeholder.html')

@app.route('/dashboards-and-visualizations/hospital-emergency-room-data-for-assault-related-injuries/info')
def hospital_emergen_info():
    return render_template('no_info_placeholder.html')

if __name__=="__main__":
    app.run()