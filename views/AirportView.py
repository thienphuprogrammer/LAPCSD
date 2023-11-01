from enum import Enum
from services.AirportService import AirportService

RED = "\033[91m"  # Red text
GREEN = "\033[92m"  # Green text
UNDERLINE = "\033[4m"  # Underline text
RESET = "\033[0m"  # Reset text color to default


class AirportView:
    """
        Develop a robust data structure: Create an efficient data structure in the computer's memory
        that optimizes query speed, ensuring seamless operation of the airport system.
    """
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
        self.__airportService = AirportService()
        self.airport_file = airport_file
        self.route_file = route_file
        self.__airportService.loadFromFile(airport_file, route_file)

    def displayMenu(self):
        try:
            while True:
                print('---------------------------------------------------------')
                print(f'\t\t\t\t{RED}{UNDERLINE}Airport Management{RESET} {RESET}')
                for menu in self.AirportMenu:
                    print(f'\t\t\t\t{menu.value}. {" ".join(menu.name.lower().split("_"))}')
                print('---------------------------------------------------------')
                try:
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
                        print(f'{RED}Invalid choice{RESET}')
                        return
                    menu_choice.get(choice)()
                    print(f'Enter any key to continue', end='')
                    input()
                except ValueError:
                    print(f'{RED}Invalid choice{RESET}')
        except KeyboardInterrupt:
            print('\nDo you want to save to file? (y/n): ', end='')
            choice = input()
            if choice == 'y' or choice == 'Y':
                self.__airportService.saveToFile(self.airport_file, self.route_file)
                print(f'{GREEN}Save to file successfully{RESET}')
            else:
                print(f'{RED}Not save to file{RESET}')

            print(f'{GREEN}Exit successfully{RESET}')
            print(f'{GREEN}Thank you for using our service{RESET}')
            print(f'{GREEN}Goodbye{RESET}')
            exit(0)

    def __deleteAirport(self):
        try:
            code = input('Enter airport code: ')
            self.__airportService.deleteAirport(code)
            print(f'{GREEN}Delete airport with code {code} successfully{RESET}')
        except Exception as e:
            print(f'{RED}{e.args}{RESET}')

    def __deleteRoute(self):
        try:
            from_airport = input('Enter from airport: ')
            to_airport = input('Enter to airport: ')
            self.__airportService.deleteRoute(from_airport, to_airport)
            print(f'{GREEN}Delete route from {from_airport} to {to_airport} successfully{RESET}')
        except Exception as e:
            print(f'{RED}{e.args}{RESET}')

    def __addNewAirport(self):
        try:
            code = input('Enter airport code: ')
            if self.__airportService.getAirportByCode(code) is not None:
                print(f'{RED}Airport with code {code} already exists{RESET}')
                return
            name = input('Enter airport name: ')
            city = input('Enter airport city: ')
            state = input('Enter airport state: ')
            self.__airportService.addAirport(code, name, city, state)
            print(f'{GREEN}Add new airport successfully{RESET}')
        except Exception as e:
            print(f'{RED}{e.args}{RESET}')

    def __addNewRoute(self):
        try:
            from_airport = input('Enter from airport: ')
            to_airport = input('Enter to airport: ')
            cost = int(input('Enter cost: '))
            self.__airportService.addRoute(from_airport, to_airport, cost)
            print(f'{GREEN}Add new route successfully{RESET}')
        except Exception as e:
            print(f'{RED}{e.args}{RESET}')

    def __displayAirportInformation(self):
        try:
            list_airports = self.__airportService.getAllAirports()
            for key, airport in list_airports.items():
                from_airport = self.__airportService.getAirportByCode(key)
                print(f'{RED}Airport{RESET} has code {GREEN}{from_airport.code}{RESET}'
                      f', name {GREEN}{from_airport.name}{RESET}'
                      f', city {GREEN}{from_airport.city}{RESET}'
                      f', state {GREEN}{from_airport.state}{RESET}'
                      f' has routes: ')
                for route in airport:
                    print(f' \t to airport has code {GREEN}{route.v}{RESET}'
                          f', city {GREEN}{self.__airportService.getAirportByCode(route.v).city}{RESET}'
                          f', state {GREEN}{self.__airportService.getAirportByCode(route.v).state}{RESET}'
                          f' with cost {GREEN}{route.cost}{RESET}')
        except Exception as e:
            print(f'{RED}{e.args}{RESET}')

    def __searchAirportByName(self):
        try:
            name = input('Enter airport name: ')
            list_airports = self.__airportService.searchAirportsByName(name)
            if len(list_airports) == 0:
                print(f'Not found airport with name {GREEN}{name}{RESET}')
                return
            for airport in list_airports:
                print(f'{RED}Airport{RESET} has code {GREEN}{airport.code}{RESET}'
                      f', name {GREEN}{airport.name}{RESET}'
                      f', city {GREEN}{airport.city}{RESET}'
                      f', state {GREEN}{airport.state}{RESET}')
        except Exception as e:
            print(f'{RED}{e.args}{RESET}')

    def __calculateCost(self):
        try:
            from_airport = input('Enter from airport: ')
            to_airport = input('Enter to airport: ')
            list_paths = self.__airportService.calculateCost(from_airport, to_airport)
            print(f'All paths from {GREEN}{from_airport}{RESET} to {GREEN}{to_airport}{RESET} are: ')
            for path in list_paths:
                print(f'\tPath: {GREEN}{" -> ".join(path["path"])}{RESET} with cost {GREEN}{path["cost"]}{RESET}')
        except Exception as e:
            print(f'{RED}{e.args}{RESET}')

    def __updateAirportInformation(self):
        try:
            code = input('Enter airport code: ')
            name = input('Enter airport name: ')
            city = input('Enter airport city: ')
            state = input('Enter airport state: ')
            self.__airportService.updateAirport(code, name, city, state)
            airport = self.__airportService.getAirportByCode(code)
            print(f'Airport with code {GREEN}{airport.code}{RESET} has name {GREEN}{airport.name}{RESET}'
                  f', city {GREEN}{airport.city}{RESET}'
                  f', state {GREEN}{airport.state}{RESET}')
            print(f'{GREEN}Update airport successfully{RESET}')
        except Exception as e:
            print(f'{RED}{e.args}{RESET}')

    def __exit(self):
        try:
            self.__airportService.saveToFile(self.airport_file, self.route_file)
            print(f'{GREEN}Save to file successfully{RESET}')
            print(f'{GREEN}Exit successfully{RESET}')
            print(f'{GREEN}Thank you for using our service{RESET}')
            print(f'{GREEN}Goodbye{RESET}')
            exit(0)
        except Exception as e:
            print(f'{RED}{e.args}{RESET}')
