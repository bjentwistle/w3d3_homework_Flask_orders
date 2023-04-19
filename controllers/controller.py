from app import app
from flask import render_template
from models.toyshop_list import orders


@app.route('/orders') 
def index():   #should display all of the orders on the page
    return render_template("index.jinja", title = "Toy's Home", orders = orders)