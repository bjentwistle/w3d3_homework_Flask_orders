from app import app
from flask import render_template
from models.toyshop_list import orders
from models.toyshop_list import order1

@app.route('/orders') 
def index():   #should display all of the orders on the page
    return render_template("orders.jinja", title = "Toy's Home", orders = orders)

# @app.route('/orders/id')
# def one_order():
#     return render_template("single_order.jinja", title = "One order", order = order1)

@app.route('/orders/<index>')           #this will return the order details of a chosen order
def single_order(index):                #using the hyperlink added in the html/jinja file
    return render_template('single_order.jinja', order = orders[int(index)]) 