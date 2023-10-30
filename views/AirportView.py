from enum import Enum

from services.AirportService import AirportService

RED = "\033[91m"
GREEN = "\033[92m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"  # Reset text color to default


class AirportView:
    class AirportMenu(Enum):
        ADD_NEW_AIRPORT = 1
        ADD_NEW_ROUTE = 2
        DISPLAY_AIRPORT_INFORMATION = 3
        SEARCH_AIRPORT_BY_NAME = 4
        CALCULATE_COST = 5
        UPDATE_AIRPORT_INFORMATION = 6
        DELETE_AIRPORT = 7
        DELETE_ROUTE = 8
        EXIT = 9

    def __init__(self, airport_file='/data/airports.pkl', route_file='/data/routes.pkl'):
        self.airportService = AirportService()
        self.airport_file = airport_file
        self.route_file = route_file
        self.airportService.loadFromFile(airport_file, route_file)

    def displayMenu(self):
        while True:
            print('-----------------------------------')
            for menu in self.AirportMenu:
                print(f'{menu.value}. {" ".join(menu.name.lower().split("_"))}')
            print('-----------------------------------')
            choice = int(input('Enter your choice: '))
            menu_choice = {
                self.AirportMenu.ADD_NEW_AIRPORT.value: self.__addNewAirport,
                self.AirportMenu.ADD_NEW_ROUTE.value: self.__addNewRoute,
                self.AirportMenu.DISPLAY_AIRPORT_INFORMATION.value: self.__displayAirportInformation,
                self.AirportMenu.SEARCH_AIRPORT_BY_NAME.value: self.__searchAirportByName,
                self.AirportMenu.CALCULATE_COST.value: self.__calculateCost,
                self.AirportMenu.UPDATE_AIRPORT_INFORMATION.value: self.__updateAirportInformation,
                self.AirportMenu.EXIT.value: self.__exit,
                self.AirportMenu.DELETE_AIRPORT.value: self.__deleteAirport,
                self.AirportMenu.DELETE_ROUTE.value: self.__deleteRoute
            }
            if choice not in menu_choice:
                print('Invalid choice')
                return
            menu_choice.get(choice)()

    def __deleteAirport(self):
        try:
            code = input('Enter airport code: ')
            self.airportService.deleteAirport(code)
            print('Delete airport successfully')
        except Exception as e:
            print(e.args)

    def __deleteRoute(self):
        try:
            from_airport = input('Enter from airport: ')
            to_airport = input('Enter to airport: ')
            self.airportService.deleteRoute(from_airport, to_airport)
            print('Delete route successfully')
        except Exception as e:
            print(e.args)

    def __addNewAirport(self):
        try:
            code = input('Enter airport code: ')
            if self.airportService.getAirportByCode(code) is not None:
                print(f'Airport with code {GREEN}{code}{RESET} is existed')
                return
            name = input('Enter airport name: ')
            city = input('Enter airport city: ')
            state = input('Enter airport state: ')
            self.airportService.addAirport(code, name, city, state)
            print('Add new airport successfully')
        except Exception as e:
            print(e.args)

    def __addNewRoute(self):
        try:
            from_airport = input('Enter from airport: ')
            to_airport = input('Enter to airport: ')
            cost = int(input('Enter cost: '))
            self.airportService.addRoute(from_airport, to_airport, cost)
            print('Add new route successfully')
        except Exception as e:
            print(e.args)

    def __displayAirportInformation(self):
        try:
            list_airports = self.airportService.getAllAirports()
            for key, airport in list_airports.items():
                from_airport = self.airportService.getAirportByCode(key)
                print(f'{RED}Airport{RESET} has code {GREEN}{from_airport.code}{RESET}'
                      f', name {GREEN}{from_airport.name}{RESET}'
                      f', city {GREEN}{from_airport.city}{RESET}'
                      f', state {GREEN}{from_airport.state}{RESET}'
                      f' has routes: ')
                for route in airport:
                    print(f' \t to airport has code {GREEN}{route.v}{RESET}'
                          f', city {GREEN}{self.airportService.getAirportByCode(route.v).city}{RESET}'
                          f', state {GREEN}{self.airportService.getAirportByCode(route.v).state}{RESET}'
                          f' with cost {GREEN}{route.cost}{RESET}')
        except Exception as e:
            print(e.args)

    def __searchAirportByName(self):
        try:
            name = input('Enter airport name: ')
            list_airports = self.airportService.searchAirportsByName(name)
            if len(list_airports) == 0:
                print(f'Not found airport with name {GREEN}{name}{RESET}')
                return
            for airport in list_airports:
                print(f'{RED}Airport{RESET} has code {GREEN}{airport.code}{RESET}'
                      f', name {GREEN}{airport.name}{RESET}'
                      f', city {GREEN}{airport.city}{RESET}'
                      f', state {GREEN}{airport.state}{RESET}')
        except Exception as e:
            print(e.args)

    def __calculateCost(self):
        try:
            from_airport = input('Enter from airport: ')
            to_airport = input('Enter to airport: ')
            list_paths = self.airportService.calculateCost(from_airport, to_airport)
            print(f'All paths from {GREEN}{from_airport}{RESET} to {GREEN}{to_airport}{RESET} are: ')
            for path in list_paths:
                print(f'\tPath: {GREEN}{" -> ".join(path["path"])}{RESET} with cost {GREEN}{path["cost"]}{RESET}')
        except Exception as e:
            print(e.args)

    def __updateAirportInformation(self):
        try:
            code = input('Enter airport code: ')
            name = input('Enter airport name: ')
            city = input('Enter airport city: ')
            state = input('Enter airport state: ')
            self.airportService.updateAirport(code, name, city, state)
            print('Update airport successfully')
        except Exception as e:
            print(e.args)

    def __exit(self):
        try:
            self.airportService.saveToFile(self.airport_file, self.route_file)
            print('Goodbye!')
            exit(0)
        except Exception as e:
            print(e.args)

