# Project: PyCharm
# File: main.py
# Created by 22/01/2021
from views.AirportView import AirportView
# how to check KeyboardInterrupt
# https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python
import signal
import sys
import os
import pickle

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        airport_file = 'data/airports.pkl'
        route_file = 'data/routes.pkl'
        airportView = AirportView(airport_file, route_file)
        airportView.displayMenu()
    except Exception as e:
        print(e.args)
