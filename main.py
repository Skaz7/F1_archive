import os
import csv
import logging
import time
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
    filename="D:\\Users\\sebas\\OneDrive\\Repositories\\F1_archive\\test\\Test.log",
    level=logging.DEBUG,
    format=LOG_FORMAT,
    filemode="w",
)
logger = logging.getLogger()


# GUI Window class
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 60, 401, 321))

        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionNew.triggered.connect(lambda: self.clicked("New was clicked"))
        self.actionSave.triggered.connect(lambda: self.clicked("Save was clicked"))
        self.actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.actionCopy.triggered.connect(lambda: self.clicked("Copy was clicked"))
        self.actionPaste.triggered.connect(lambda: self.clicked("Paste was clicked"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("F1 Statistics", "F1 Statistics"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save a file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit the program"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy a file"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste a file"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))

    def clicked(self, text):
        self.label.setText(text)
        self.label.adjustSize()


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
    
    datafile.close()


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

        input("\n\nENTER")

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
        input("\n\nENTER")

    def search_by_country():
        constructors_nationalities = sorted(set([row[3] for row in data_list]))
        print("\nAll nationalities:\n")
        print("+-----------------+")
        for nationality in constructors_nationalities:
            print(f"| {nationality:15} | ")
        print("+-----------------+")

        print("\nEnter constructor nationality from above table: ")
        choice = input("\n> ").lower()
        data_list.sort(key=lambda x: x[3])
        
        for row in data_list:
            if choice in row[3].lower():
                print("\n-------------------------------------------------------------")
                print(f"{'Name: ':12} {row[2].upper()}")
                print(f"{'Nationality:':12} {row[3]}")
                print(f"{'Url: ':12} {row[4]}")
                print("-------------------------------------------------------------")
        input("\n\nENTER")

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
        input("\n\nENTER")

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
        input("\n\nENTER")

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

    # races in csv file aren't sorted by year, so it needs to be sorted it manually
    data_list.sort(key=lambda x: x[5])

    for row in data_list:
        # convert date from string format to datetime, and use .date() to delete time (convert 2017-10-01 00:00:00 to 2017-10-01)
        row[5] = datetime.strptime(row[5], "%Y-%m-%d").date()

    # for row in data_list:
    #     logging.debug(f"{row}")
    # input()


    # def print_race():
    #     print("---------------------------------------------------------------")
    #     print(f"{'Round: ':7} {row[2]}")
    #     print(f"{'Name: ':7} {row[4]}")
    #     print(f"{'Date: ':7} {row[5]}")
    #     print(f"{'Time: ':7} {row[6]}")
    #     print(f"{'Url: ':7} {row[7]}")


    def races_by_date():
        print("\nWhen do you want to start? (YYYY-MM-DD)")
        start_date = input("> ")
        print("\nWhen do you want to stop? (YYYY-MM-DD)")
        stop_date = input("> ")

        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        stop_date = datetime.strptime(stop_date, "%Y-%m-%d").date()
        print()

        for row in data_list:
            if row[5] >= start_date and row[5] <= stop_date:
                print("---------------------------------------------------------------")
                print(f"{'Round: ':7} {row[2]}")
                print(f"{'Name: ':7} {row[4]}")
                print(f"{'Date: ':7} {row[5]}")
                print(f"{'Time: ':7} {row[6]}")
                print(f"{'Url: ':7} {row[7]}")
        input("\n\nENTER")


    def races_by_name():
        print("\nEnter race name:")
        choice = input("> ").lower()
        for row in data_list:
            if choice in row[4].lower():
                print("---------------------------------------------------------------")
                print(f"{'Round: ':7} {row[2]}")
                print(f"{'Name: ':7} {row[4]}")
                print(f"{'Date: ':7} {row[5]}")
                print(f"{'Time: ':7} {row[6]}")
                print(f"{'Url: ':7} {row[7]}")
        input("\n\nENTER")


    def races_by_round():
        print("\nEnter round number:")
        choice = input("> ")
        for row in data_list:
            if row[2] == choice:
                print("---------------------------------------------------------------")
                print(f"{'Round: ':7} {row[2]}")
                print(f"{'Name: ':7} {row[4]}")
                print(f"{'Date: ':7} {row[5]}")
                print(f"{'Time: ':7} {row[6]}")
                print(f"{'Url: ':7} {row[7]}")
        input("\n\nENTER")


    while True:
        clear_screen()
        print("\nOptions:")
        print("\n\t1 - Print races by date")
        print("\t2 - Print races by name")
        print("\t3 - Print races by round")
        print("\n\t0 - Back")

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


# welcome_screen()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())