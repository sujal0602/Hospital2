
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="Hospital"
)
cursor = db.cursor()

# Homepage
@app.route("/")
def index():
    return render_template("index.html")

# Registration Page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        idno = request.form["idno"]
        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        phone = request.form["phone"]
        bg = request.form["bg"]

        query = '''
            INSERT INTO appointment (idno, name, age, gender, phone, bg)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (idno, name, age, gender, phone, bg))
        db.commit()

        return render_template("success.html", message="Registration Successful!")
    return render_template("register.html")

# Appointment Page
@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    if request.method == "POST":
        idno = request.form["idno"]
        doctor = request.form["doctor"]
        date = request.form["date"]
        time = request.form["time"]

        appointment_no = f"APT-{idno[-4:]}"
        query = '''
            INSERT INTO appointment_details (idno, doctor, date, time, appointment_no)
            VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (idno, doctor, date, time, appointment_no))
        db.commit()

        return render_template("success.html", message="Appointment Booked Successfully!")
    return render_template("appointment.html")

# List of Doctors
@app.route("/doctors")
def doctors():
    return render_template("doctors.html")

# Services Available
@app.route("/services")
def services():
    return render_template("services.html")

if __name__ == "__main__":
    app.run(debug=True)
