# INET 4031 Intro to Systems
# 
# Project: Geometry Calculator Web App
#
# Sample Code for the Python Flask Web App Implementation of the Geometry Calculator
#
# Author: Joe Axberg
# Orig Date: 3/31/2022
# Mod Date: 12/30/2023
# Mod Date: 12/31/2024
#

# imports
from flask import Flask, request, render_template, redirect, url_for
import cylinder
import sphere

# flask plumbing
app = Flask(__name__)

# flask route for the index aka 'home' page
# uses html template for user selection
@app.route("/", methods=["GET", "POST"])
def mainForm():
    if request.method == "POST":
        sphere_selected = request.form.get("sphere")
        cylinder_selected = request.form.get("cylinder")
        print("Selection was: ", sphere_selected, cylinder_selected)
        if sphere_selected == "on":
            print("User selected sphere")
            return redirect(url_for('sphereForm'))
        elif cylinder_selected == "on":
            print("User selected cylinder")
            return redirect(url_for('cylinderForm'))
    return render_template("index.html")

# flask route for the cylinder calculations page
@app.route("/cylinder", methods=["GET", "POST"])
def cylinderForm():
    if request.method == "POST":
        radius = request.form.get("rad")
        height = request.form.get("hgt")
        vol = cylinder.volume(int(radius), int(height))
        return "User entered: Radius " + str(radius) + " and Height: " + str(height) + ". <p>The Volume is: " + str(vol)
    return render_template("cylinder.html")

# flask route for the sphere calculations page
@app.route("/sphere", methods=["GET", "POST"])
def sphereForm():
    if request.method == "POST":
        radius = request.form.get("rad")
        vol = sphere.volume(int(radius))
        return "User entered: Radius " + str(radius) + ". <p>The Volume is: " + str(vol)
    return render_template("sphere.html")

# more code here for the rest of the calculators: sphere, cube, etc.

if __name__ == '__main__':
    app.run(host='0.0.0.0')

