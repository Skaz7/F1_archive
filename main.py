import os
import csv
import logging


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
    filename="D:\\Users\\sebas\\OneDrive\\Repositories\\F1_archive\\test\\Test.log",
    level=logging.DEBUG,
    format=LOG_FORMAT,
    filemode='w'
)
logger = logging.getLogger()


def open_file(file):
    """
    Data loaded from file must be assigned to variable.
    If we use 'with open' function, then file will be closed after return from open_file function.
    """
    datafile = open(
        f"D:\\Users\\sebas\\OneDrive\\Repositories\\F1_archive\\data\\{file}",
        "r",
        encoding="utf-8",
    )
    global data_table
    data_table = csv.reader(datafile)


def clear_screen():
    os.system("cls")


def welcome_screen():
    while True:
        clear_screen()
        print("\nChoose option:")
        print("\n\t 1 - Circuits info")
        print("\t 2 - Constructor results")
        print("\t 3 - Constructor standings")
        print("\t 4 - Constructors")
        print("\t 5 - Driver standings")
        print("\t 6 - Lap times")
        print("\t 7 - Pit stops")
        print("\t 8 - Qualifying")
        print("\t 9 - Races")
        print("\t10 - Results")
        print("\t11 - Seasons")
        print("\t12 - Status")
        print("\n\t 0 - EXIT")

        choice = input("\n\t> ")

        if choice == "0":
            quit()
        elif choice == "1":
            circuits()


def circuits():

    def search_by_name():
        print("Enter circuit name: ")
        search_name = input("\n> ").lower()
        for row in data_table:
            if search_name in row[1].lower() or search_name in row[2].lower():
                logging.debug(f"search_name - {search_name}")
                logging.debug(f"row[1] - {row[1]}")
                logging.debug(f"row[2] - {row[2]}")
                print(*row)
                input()
            else:
                print("\n NOT FOUND!")
                input()

    clear_screen()
    open_file("circuits.csv")

    for row in data_table:
        print(f"Id: {row[0]}.")
        print(f"Ref: {row[1]}")
        print(f"Name: {row[2]}")
        print(f"Location: {row[3]}")
        print(f"Country: {row[4]}")
        print(f"Coordinates: Lat: {row[5]}, Lng: {row[6]}, Alt: {row[7]}")
        print(f"Url: {row[8]}")
        print()
        # print(
        #     f"{row[0]:2}. {row[1]:15} {row[2]:40} {row[3]:21} {row[4]:14} {row[5]:9} {row[6]:9} {row[7]:4} {row[8]:72}"
        # )

    print("\n\n1 - Search for circuit by name")
    print("Enter - Back")

    choice = input("\n> ")
    if choice == "1":
        search_by_name()
    else:
        return    

def constructor_results():
    pass


def constructor_standings():
    pass


def constructors():
    pass


def driver_standings():
    pass


def drivers():
    pass


def lap_times():
    pass


def pit_stops():
    pass


def qualifying():
    pass


def races():
    pass


def results():
    pass


def seasons():
    pass


def status():
    pass


def search():
    pass


welcome_screen()
