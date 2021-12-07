from os import getcwd
from os.path import join
from tkinter import PhotoImage
from tkinter.constants import END, W, YES
from tkinter.font import BOLD, Font
from tkinter.ttk import Frame, Label, Notebook, Treeview

from ..models.student import HEADERS

KEY_HEADER_TEXT = 'header_text'


class OverviewFrame:
    def __init__(self, notebook: Notebook, **kwargs):
        self._frame = Frame(notebook)

        # Create a smaller logo
        logo = PhotoImage(file=join(getcwd(), 'assets', 'images', 'biker-banner.png')).subsample(3, 3)

        logo_container = Label(self.frame, image=logo, borderwidth=1)
        logo_container.img = logo
        logo_container.grid(column=0, row=0, pady=8, columnspan=2)

        # Create a Header
        header_text = kwargs.get(KEY_HEADER_TEXT)
        header = Label(self.frame, text=header_text, font=Font(weight=BOLD))

        header.grid(row=1, column=1, columnspan=2, ipady=8)

        # Create a Table widget for showing the data
        self._overview = Treeview(self.frame, columns='lastname')
        self._overview.grid(row=2, column=1, columnspan=2, padx=64)

        self.frame.grid_columnconfigure(2, weight=1)

        # Create table columns and headers
        for idx in range(0, 2):
            header = HEADERS[idx]

            self.overview.heading(f'#{idx}', text=header, anchor=W)
            self.overview.column(f'#{idx}', anchor=W, minwidth=64, stretch=YES)

        self.frame.grid(column=1, row=2)

    def insert_data(self, objects):
        """
        Inserts data into the Table Widget
        :param objects: The data to insert
        """
        if len(objects) == 0:
            return

        for index, student in enumerate(objects):
            self.overview.insert('', index=END, iid=index, text=student.firstname, values=student.lastname)

    @property
    def frame(self):
        return self._frame

    @property
    def overview(self):
        return self._overview
