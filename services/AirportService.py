import pickle

from datastructor.Graph import AdjacencyGraph
from entities.Airport import Airport


class AirportService:
    """
        Develop a robust data structure: Create an efficient data structure in the computer's memory
        that optimizes query speed, ensuring seamless operation of the airport system.
    """
    def __init__(self):
        self.airportRepository = AdjacencyGraph()
        self.list_airports = []

    def getAirportByCode(self, code):
        for airport in self.list_airports:
            if airport.code == code:
                return airport
        return None

    # Add airports: Implement a function to add airports to the system, expanding the network with each addition.
    def addAirport(self, code, name, city, state):
        try:
            airport = Airport(code, name, city, state)
            self.list_airports.append(airport)
            self.airportRepository.addVertex(airport.code)
        except Exception as e:
            raise e

    def addRoute(self, from_airport, to_airport, cost):
        try:
            self.airportRepository.addEdge(from_airport, to_airport, cost)
        except Exception as e:
            raise e

    # Display airport information: Enable the system to display comprehensive information about all airports,
    # providing a clear overview of the entire network.
    def getAllAirports(self):
        try:
            return self.airportRepository.getAllVertices()
        except Exception as e:
            raise e

    # Search functionality: Implement a search mechanism allowing users to find specific airports based on their
    # names. Once found, display detailed information about the respective airport.
    def searchAirportsByName(self, airport_name):
        try:
            list_air = []
            for airport in self.list_airports:
                if airport.name.find(airport_name) != -1:
                    list_air.append(airport)
            return list_air
        except Exception as e:
            raise e

    # Cost calculation: Develop a function to calculate the cost of travel from one airport (A) to another airport
    # (B), considering the directional and connected nature of the airport system.
    def calculateCost(self, from_airport, to_airport):
        try:
            list_paths = self.airportRepository.getAllPaths(from_airport, to_airport)
            return list_paths
        except Exception as e:
            raise e

    # Update airport information: Implement a feature enabling the system to update airport details based on their
    # unique ID, ensuring accurate and up-to-date information for each airport.
    def updateAirport(self, airport_code, airport_name, airport_city, airport_state):
        try:
            for airport in self.list_airports:
                if airport.code == airport.code:
                    airport.name = airport_name
                    airport.city = airport_city
                    airport.state = airport_state
                    break
        except Exception as e:
            raise e

    # Deletion capability: Develop a function to remove individual airports from the system, streamlining the network
    # as needed.
    def deleteAirport(self, airport_code):
        try:
            self.airportRepository.deleteVertex(airport_code)
            for airport in self.list_airports:
                if airport.code == airport_code:
                    self.list_airports.remove(airport)
        except Exception as e:
            raise e

    # Additionally, it's crucial to adhere to the note provided: after all operations are completed, save the updated
    # data to a file.JSON.
    def saveToFile(self, file_airports, file_routes):
        try:
            with open(file_airports, 'wb') as file:
                pickle.dump(self.list_airports, file)
            with open(file_routes, 'wb') as file:
                pickle.dump(self.airportRepository, file)
        except Exception as e:
            raise e

    def loadFromFile(self, file_airports, file_routes):
        try:
            with open(file_airports, 'rb') as file:
                self.list_airports = pickle.load(file)
            with open(file_routes, 'rb') as file:
                self.airportRepository = pickle.load(file)
        except Exception as e:
            raise e

    def deleteRoute(self, from_airport, to_airport):
        try:
            self.airportRepository.deleteEdge(from_airport, to_airport)
        except Exception as e:
            raise e