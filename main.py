# Project: PyCharm
# File: main.py
# Created by 22/01/2021
from views.AirportView import AirportView

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    airport_file = 'data/airports.pkl'
    route_file = 'data/routes.pkl'
    airportView = AirportView(airport_file, route_file)
    airportView.displayMenu()
