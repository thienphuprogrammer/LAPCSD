# Project: PyCharm
# File: main.py
# Created by Nguyen Ngoc Thien Phu at 11:01 PM 2023/31/10
from views.AirportView import AirportView

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        airport_file = 'data/airports.pkl'
        route_file = 'data/routes.pkl'
        airportView = AirportView(airport_file, route_file)
        airportView.displayMenu()
    except Exception as e:
        print(e.args)
