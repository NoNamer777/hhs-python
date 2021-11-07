"""
Project created by Oscar Wellner, 21144192

This application will read the CSV-file and insert the data found into the Text widget of the student overview tab.
"""

from src.layout import BikerManagementApp


def main():
    try:
        biker_management_app = BikerManagementApp()

        biker_management_app.app.mainloop()

    except KeyboardInterrupt:
        print('Successfully closed application')


if __name__ == '__main__':
    main()
