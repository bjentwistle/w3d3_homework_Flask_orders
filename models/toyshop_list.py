from models.order import *

# some dummy data for now created from the Order class
order1 = Order("Andy", "Buzz Lightyear figure", 25, False)
order2 = Order("Sid", "Rockets, explosives, flash bangs", 50,  True)
order3 = Order("Bonnie", "Jessie figure", 20, True)
order4 = Order("Woody", "Bullseye Horse with saddle", 25, False)

orders = [order1, order2, order3, order4] #use index of this list to show a page with just a single order
