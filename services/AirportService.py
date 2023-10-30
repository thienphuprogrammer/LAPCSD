from datastructor.Graph import AdjacencyGraph


class AirportService:
    """
        Develop a robust data structure: Create an efficient data structure in the computer's memory
        that optimizes query speed, ensuring seamless operation of the airport system.
    """
    def __init__(self):
        self.airportRepository = AdjacencyGraph()

    # Add airports: Implement a function to add airports to the system, expanding the network with each addition.
    def addAirport(self, airport):
        self.airportRepository.addVertex(airport.code, airport)

    # Display airport information: Enable the system to display comprehensive information about all airports,
    # providing a clear overview of the entire network.
    def displayAirports(self):
        return self.airportRepository.getVertex()

    # Search functionality: Implement a search mechanism allowing users to find specific airports based on their
    # names. Once found, display detailed information about the respective airport.
    def searchAirport(self, airportCode):
        return self.airportRepository.mapVertices.get(airportCode)

    # Cost calculation: Develop a function to calculate the cost of travel from one airport (A) to another airport
    # (B), considering the directional and connected nature of the airport system.
    def calculateCost(self, source, destination):
        return self.airportRepository.mapVertices.get(source, destination)

    # Update airport information: Implement a feature enabling the system to update airport details based on their
    # unique ID, ensuring accurate and up-to-date information for each airport.
    def updateAirport(self, airport):
        self.airportRepository.updateVertex(airport.code, airport)

    # Deletion capability: Develop a function to remove individual airports from the system, streamlining the network as needed.
    def deleteAirport(self, airport):
        self.airportRepository.deleteVertex(airport.code)

    # Additionally, it's crucial to adhere to the note provided: after all operations are completed, save the updated data to a text file.
    def saveToFile(self):
        self.airportRepository.saveToFile()
