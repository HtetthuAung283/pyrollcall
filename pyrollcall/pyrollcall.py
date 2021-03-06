# -*- encoding: utf-8 -*-

from pyrollcall.mainwindow import MainWindow
from pyrollcall.database import Database

def main():
    # Try to unpickle database from file.
    try:
        db = Database("rollcall.db")
        db.load()
    except FileNotFoundError:
        print("[WARNING] Database file not found")

    main_window = MainWindow()
    main_window.connect_db(db)
    main_window.show()
