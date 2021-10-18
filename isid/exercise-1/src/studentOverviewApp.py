from os import chdir, getcwd
from os.path import join
from pathlib import Path
from tkinter import ttk, Toplevel, PhotoImage, Text, Tk, X, CENTER
from tkinter.font import Font, BOLD

# Gets the current file location of this file
FILE_LOCATION = Path(__file__)
# Changes the working directory of the Python script to 2 directories higher,
# which would be the project root.
chdir(FILE_LOCATION.parent.parent)


class StudentOverviewApp:
    _app: Tk = None
    _window: Toplevel = None
    _banner: PhotoImage = None
    _student_list_text: Text = None

    def __init__(self):
        self._app = Tk()
        self._app.title('Student Overview')
        self._app.minsize(800, 600)

        self._create_banner()
        self._create_text_widget()

    def _create_banner(self):
        self._banner = PhotoImage(file=join(getcwd(), 'assets', 'images', 'biker-banner.png'))

        label = ttk.Label(self._app, image=self._banner)
        label.config(anchor=CENTER)
        label.img = self._banner

        label.pack(fill=X, pady=4)

    def _create_text_widget(self):
        student_overview_label = ttk.Label(self._app, text='Students Overview:', font=Font(weight=BOLD))
        student_overview_label.pack(ipady=4, padx=80, fill=X)

        self._student_list_text = Text(self._app)

        self._student_list_text.pack()

    @property
    def student_list_text(self) -> Text:
        return self._student_list_text

    @property
    def app(self) -> Tk:
        return self._app
