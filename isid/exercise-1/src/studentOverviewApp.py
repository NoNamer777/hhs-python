from os import chdir, getcwd
from os.path import join
import pathlib
from tkinter import ttk, font
import tkinter

PROJECT_DIR = pathlib.Path(__file__)
chdir(PROJECT_DIR.parent.parent)


class StudentOverviewApp:
    _app: tkinter.Tk = None
    _window: tkinter.Toplevel = None
    _banner: tkinter.PhotoImage = None
    _student_list_text: tkinter.Text = None

    def __init__(self):
        self._app = tkinter.Tk()
        self._app.title('Student Overview')
        self._app.minsize(800, 600)

        self._create_banner()
        self._create_text_widget()

    def _create_banner(self):
        print(join(getcwd(), 'assets', 'images', 'biker-banner.png'))

        self._banner = tkinter.PhotoImage(
            file=join(getcwd(), 'assets', 'images', 'biker-banner.png'))

        label = ttk.Label(self._app, image=self._banner)
        label.config(anchor=tkinter.CENTER)
        label.img = self._banner

        label.pack(fill=tkinter.X, pady=4)

    def _create_text_widget(self):
        student_overview_label = ttk.Label(self._app, text='Students Overview:', font=font.Font(weight=font.BOLD))
        student_overview_label.pack(ipady=4, padx=80, fill=tkinter.X)

        self._student_list_text = tkinter.Text(self._app)

        self._student_list_text.pack()

    @property
    def student_list_text(self) -> tkinter.Text:
        return self._student_list_text

    @property
    def app(self) -> tkinter.Tk:
        return self._app
