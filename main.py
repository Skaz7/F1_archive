import os
import csv
import logging
import time

from datetime import datetime


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
    filename="D:\\Users\\sebas\\OneDrive\\Repositories\\F1_archive\\test\\Test.log",
    level=logging.DEBUG,
    format=LOG_FORMAT,
    filemode="w",
)
logger = logging.getLogger()


def open_file(file):
    """
    Data loaded from file must be assigned to variable.
    If we use 'with open' function, then file will be closed after return from open_file function.
    """
    global data_list
    data_list = []

    datafile = open(
        f"D:\\Users\\sebas\\OneDrive\\Repositories\\F1_archive\\data\\{file}",
        "r",
        encoding="utf-8",
    )

    for row in csv.reader(datafile):
        data_list.append(row)


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
        print("\n\t 0 - EXIT")

        choice = input("\n\t> ")

        if choice == "0":
            quit()
        elif choice == "1":
            circuits()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            constructors()
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            pass
        elif choice == "9":
            races()
        elif choice == "10":
            pass
        elif choice == "11":
            pass
        elif choice == "12":
            pass
        else:
            print("\n\n\t\t\tWrong option!")
            time.sleep(1)


def circuits():
    def search_by_name():
        print("Enter circuit name: ")
        search_name = input("\n> ").lower()
        logging.debug(f"search = {search_name}")
        for row in data_list:
            if search_name in row[1].lower() or search_name in row[2].lower():

                print(f"Id: {row[0]}.")
                print(f"Ref: {row[1]}")
                print(f"Name: {row[2]}")
                print(f"Location: {row[3]}")
                print(f"Country: {row[4]}")
                print(f"Coordinates: Lat: {row[5]}, Lng: {row[6]}, Alt: {row[7]}")
                print(f"Url: {row[8]}")
                print()

        input()

    clear_screen()
    open_file("circuits.csv")

    for row in data_list:
        print(f"Id: {row[0]}.")
        print(f"Ref: {row[1]}")
        print(f"Name: {row[2]}")
        print(f"Location: {row[3]}")
        print(f"Country: {row[4]}")
        print(f"Coordinates: Lat: {row[5]}, Lng: {row[6]}, Alt: {row[7]}")
        print(f"Url: {row[8]}")
        print()

    print("\n\n\t1 - Search for circuit by name")
    print("\n\tEnter - Back")

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
    open_file("constructors.csv")

    def search_by_name():
        print("\nEnter constructor name to find: ")
        choice = input("\n> ").lower()
        data_list.sort(key=lambda x: x[2])
        for row in data_list:
            if choice in row[2].lower():
                print("\n-------------------------------------------------------------")
                print(f"{'Name: ':12} {row[2].upper()}")
                print(f"{'Nationality:':12} {row[3]}")
                print(f"{'Url: ':12} {row[4]}")
                print("-------------------------------------------------------------")
        input()

    def search_by_country():
        print("\nEnter constructor nationality: ")
        choice = input("\n> ").lower()
        data_list.sort(key=lambda x: x[3])
        for row in data_list:
            if choice in row[3].lower():
                print("\n-------------------------------------------------------------")
                print(f"{'Name: ':12} {row[2].upper()}")
                print(f"{'Nationality:':12} {row[3]}")
                print(f"{'Url: ':12} {row[4]}")
                print("-------------------------------------------------------------")
        input()

    def print_by_name():
        names = set()

        data_list.sort(key=lambda x: x[2])

        for row in data_list:
            names.add(row[3])
        names = sorted(list(names))

        for name in names:
            print("\n------------------------------------")
            print(f"Nationality: {name.upper()}")
            print("------------------------------------")
            for row in data_list:
                if name in row:
                    print(f"Name: {row[2]}")
                    print(f"Url: {row[4]}\n")
            print()
        input()

    def print_by_country():
        nationalities = set()

        data_list.sort(key=lambda x: x[3])

        for row in data_list:
            nationalities.add(row[3])
        nationalities = sorted(list(nationalities))

        for nationality in nationalities:
            print("\n------------------------------------")
            print(f"Nationality: {nationality.upper()}")
            print("------------------------------------")
            for row in data_list:
                if nationality in row:
                    print(f"Name: {row[2]}")
                    print(f"Url: {row[4]}\n")
            print()
        input()

    # main loop for constructors module
    while True:
        clear_screen()
        print("\nOptions:")
        print("\n\t1 - Search by name")
        print("\t2 - Search by country")
        print("\t3 - Print all by name")
        print("\t4 - Print all by country")
        print("\n\t0 - Back")

        choice = input("\n\t> ")

        if choice == "1":
            search_by_name()
        elif choice == "2":
            search_by_country()
        elif choice == "3":
            print_by_name()
        elif choice == "4":
            print_by_country()
        elif choice == "0":
            return
        else:
            print("\n\n\t\t\tWrong option!!!")
            time.sleep(2)
            continue


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
    open_file("races.csv")

    def races_by_date():
        print("\nWhen do you want to start? (YYYY-MM-DD)")
        start_date = input("> ")
        print("\nWhen do you want to stop? (YYYY-MM-DD)")
        stop_date = input("> ")
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        stop_date = datetime.strptime(stop_date, "%Y-%m-%d").date()

        for row in data_list:
            if row[1] >= start_date and row[1] <= stop_date:
                print(f"Id: {row[0]}.")
                print(f"Year: {row[1]}")
                print(f"Round: {row[2]}")
                print(f"Circuit Id: {row[3]}")
                print(f"Name: {row[4]}")

                # convert date from string format to datetime, and use .date() to delete time (convert 2017-10-01 00:00:00 to 2017-10-01)
                row[5] = datetime.strptime(row[5], "%Y-%m-%d").date()

                print(f"Date: {row[5]}")
                print(f"Time: {row[6]}")
                print(f"Url: {row[7]}")
                print()
                logging.debug(f"{row}")
        input()

    def races_by_name():
        pass

    def races_by_round():
        pass

    # races in csv file aren't sorted by year, so it needs to be sorted it manually
    data_list.sort(key=lambda x: x[5])

    while True:
        clear_screen()
        print("\nOptions:")
        print("\n\t1 - Print races by date")
        print("\t2 - Print races by name")
        print("\t3 - Print races by round")
        
        choice = input("\n\t> ")

        if choice == "1":
            races_by_date()
        elif choice == "2":
            races_by_name()
        elif choice == "3":
            races_by_round()
        elif choice == "0":
            return
        else:
            print("\n\n\t\t\tWrong Option!!!")
            time.sleep(1)
            continue


def results():
    pass


def seasons():
    pass


def status():
    pass


def search():
    pass


welcome_screen()
