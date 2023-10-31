import pickle

from datastructor.Graph import AdjacencyGraph
from entities.Airport import Airport


class AirportService:
    def __init__(self):
        self.__airportRepository = AdjacencyGraph()
        self.__list_airports = []

    def getAirportByCode(self, code):
        for airport in self.__list_airports:
            if airport.get_code() == code:
                return airport
        return None

    # Add airports: Implement a function to add airports to the system, expanding the network with each addition.
    def addAirport(self, code, name, city, state):
        try:
            airport = Airport(code, name, city, state)
            self.__list_airports.append(airport)
            self.__airportRepository.addVertex(airport.get_code())
        except Exception as e:
            raise e

    def addRoute(self, from_airport, to_airport, cost):
        try:
            self.__airportRepository.addEdge(from_airport, to_airport, cost)
        except Exception as e:
            raise e

    # Display airport information: Enable the system to display comprehensive information about all airports,
    # providing a clear overview of the entire network.
    def getAllAirports(self):
        try:
            return self.__airportRepository.getAllVertices()
        except Exception as e:
            raise e

    # Search functionality: Implement a search mechanism allowing users to find specific airports based on their
    # names. Once found, display detailed information about the respective airport.
    def searchAirportsByName(self, airport_name):
        try:
            list_air = []
            for airport in self.__list_airports:
                if airport.get_name().lower().find(airport_name.lower()) != -1:
                    list_air.append(airport)
            return list_air
        except Exception as e:
            raise e

    # Cost calculation: Develop a function to calculate the cost of travel from one airport (A) to another airport
    # (B), considering the directional and connected nature of the airport system.
    def calculateCost(self, from_airport, to_airport):
        try:
            list_paths = self.__airportRepository.getAllPaths(from_airport, to_airport)
            return list_paths
        except Exception as e:
            raise e

    # Update airport information: Implement a feature enabling the system to update airport details based on their
    # unique ID, ensuring accurate and up-to-date information for each airport.
    def updateAirport(self, airport_code, airport_name, airport_city, airport_state):
        try:
            for airport in self.__list_airports:
                if airport.get_code() == airport_code:
                    airport.set_name(airport_name)
                    airport.set_city(airport_city)
                    airport.set_state(airport_state)
                    break
        except Exception as e:
            raise e

    # Deletion capability: Develop a function to remove individual airports from the system, streamlining the network
    # as needed.
    def deleteAirport(self, airport_code):
        try:
            self.__airportRepository.deleteVertex(airport_code)
            for airport in self.__list_airports:
                if airport.get_code() == airport_code:
                    self.__list_airports.remove(airport)
        except Exception as e:
            raise e

    # Additionally, it's crucial to adhere to the note provided: after all operations are completed, save the updated
    # data to a file.JSON.
    def saveToFile(self, file_airports, file_routes):
        try:
            with open(file_airports, 'wb') as file:
                pickle.dump(self.__list_airports, file)
            with open(file_routes, 'wb') as file:
                pickle.dump(self.__airportRepository, file)
        except Exception as e:
            raise e

    def loadFromFile(self, file_airports, file_routes):
        try:
            with open(file_airports, 'rb') as file:
                self.__list_airports = pickle.load(file)
            with open(file_routes, 'rb') as file:
                self.__airportRepository = pickle.load(file)
        except Exception as e:
            raise e

    def deleteRoute(self, from_airport, to_airport):
        try:
            self.__airportRepository.deleteEdge(from_airport, to_airport)
        except Exception as e:
            raise e
