from os import chdir, getcwd
from os.path import join
from pathlib import Path
from tkinter import Tk, PhotoImage, Text
from tkinter.constants import BOTH, SOLID, NW, N, Y
from tkinter.font import Font, BOLD
from tkinter.ttk import Notebook, Frame, Label

TAB_MAIN_MENU_LABEL = 'Main Menu'
MAIN_MENU_TEXT = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut ' \
                 'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris ' \
                 'nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit ' \
                 'esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non ' \
                 'proident, sunt in culpa qui officia deserunt mollit anim id est laborum. '
TAB_STUDENTS_OVERVIEW_LABEL = 'Students'
STUDENTS_OVERVIEW_LABEL_TEXT = 'List of Students:'
WINDOW_TITLE = 'Students Overview'
WINDOW_DEFAULT_WIDTH = 800
WINDOW_DEFAULT_HEIGHT = 600

# Gets the current file location of this file
FILE_LOCATION = Path(__file__)
# Changes the working directory of the Python script to 2 directories higher,
# which would be the project root.
chdir(FILE_LOCATION.parent.parent)


class StudentOverviewApp:
    _app: Tk = None
    _notebook: Notebook = None
    _main_menu_frame: Frame = None
    _students_overview_frame: Frame = None
    _first_name_text_widget: Text = None
    _last_name_text_widget: Text = None

    def __init__(self):
        self._app = Tk()
        self._app.title(WINDOW_TITLE)
        self._app.minsize(WINDOW_DEFAULT_WIDTH, WINDOW_DEFAULT_HEIGHT)

        self._notebook = Notebook(self.app)
        self._notebook.pack(expand=True, fill=BOTH)

        self._create_main_menu_frame()
        self._create_students_overview_frame()

    def _create_main_menu_frame(self):
        """
        Creates the Main menu with a logo and an area to show some text.
        """
        self._main_menu_frame = Frame(self._notebook)

        banner = self._create_banner(self._main_menu_frame)
        banner.grid(row=0, column=0, padx=8, pady=16, sticky=NW)

        text_container = Label(self._main_menu_frame, text=MAIN_MENU_TEXT, borderwidth=1, relief=SOLID)
        text_container.config(wraplength=400, anchor=N, padding=(0, 96))
        text_container.grid(row=0, column=1, ipadx=16, pady=16, padx=16, sticky='nes')

        self._main_menu_frame.grid_rowconfigure(0, weight=1)
        self._main_menu_frame.grid_columnconfigure(1, weight=1)

        self._main_menu_frame.pack(fill=Y, expand=True)
        self._notebook.add(self._main_menu_frame, text=TAB_MAIN_MENU_LABEL)

    def _create_students_overview_frame(self):
        """
        Creates the frame which will show an overview of the Students information.
        """
        self._students_overview_frame = Frame(self._notebook)

        overview_label = Label(self._students_overview_frame, text=STUDENTS_OVERVIEW_LABEL_TEXT, font=Font(weight=BOLD))
        overview_label.grid(row=0, column=0, columnspan=2, ipady=8)

        self._create_student_overview_widgets(self._students_overview_frame)

        self._students_overview_frame.grid_columnconfigure(0, weight=1)
        self._students_overview_frame.grid_columnconfigure(1, weight=1)

        self._students_overview_frame.pack(fill=BOTH, expand=True)
        self._notebook.add(self._students_overview_frame, text=TAB_STUDENTS_OVERVIEW_LABEL)

    def _create_banner(self, parent: Frame) -> Label:
        """
        Creates a logo.
        :param parent: Where the logo will be added to.
        """
        banner = PhotoImage(file=join(getcwd(), 'assets', 'images', 'biker-banner.png'))

        banner_container = Label(parent, image=banner)
        banner_container.img = banner

        return banner_container

    def _create_student_overview_widgets(self, parent: Frame):
        """
        Creates the Text widgets which will hold the information of te Students.
        :param parent: Where the Text widgets will be added to.
        """
        line = '-' * 40
        firstname = 'Firstname'
        lastname = 'Lastname'

        self._first_name_text_widget = Text(parent, width=40, borderwidth=1, relief=SOLID)
        self._first_name_text_widget.grid(row=1, column=0, sticky='nes')

        self._first_name_text_widget.insert('1.0', f'{firstname.center(40)}\n')
        self._first_name_text_widget.insert('2.0', f'{line}')

        self._last_name_text_widget = Text(parent, width=40, borderwidth=1, relief=SOLID)
        self._last_name_text_widget.grid(row=1, column=1, sticky='nsw')

        self._last_name_text_widget.insert('1.0',  f'{lastname.center(40)}\n')
        self._last_name_text_widget.insert('2.0', f'{line}')

    @property
    def app(self) -> Tk:
        return self._app

    @property
    def student_first_name_text_widget(self):
        return self._first_name_text_widget

    @property
    def student_last_name_text_widget(self):
        return self._last_name_text_widget
