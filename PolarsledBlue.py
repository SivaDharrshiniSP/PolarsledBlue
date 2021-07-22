from flask import Flask, render_template, request, Response,send_file,make_response,jsonify,flash,redirect,url_for
import configparser 
import requests

app = Flask(__name__)
app.secret_key="secret"
framework="PolarSled Blue"

@app.route("/")
def home():
    return render_template("home.html",framework=framework)

@app.route("/initDbtProj")
def init_dbt_proj():
    return render_template("dbtProject.html",framework=framework)

@app.route("/connection")
def connc():
    return render_template("connection.html",framework=framework)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)