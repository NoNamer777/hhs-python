"""
Author: Oscar Wellner, 21144192
Date: 2021-10-14
About:    This Python script will create a GUI app with the Tkinter module,
          in which it will show a list of Students in a Text widget with a banner above that.
"""
from student import Student
from studentOverviewApp import StudentOverviewApp
from tkinter.constants import DISABLED

STUDENTS = [
    Student(firstname='Oscar', lastname='Wellner'),
    Student(firstname='Dylan', lastname='van der Hout'),
    Student(firstname='Daniel', lastname='van Nieuwenhuizen'),
    Student(firstname='Yasmine', lastname='Amadou'),
]


def main():
    try:
        student_overview_app = StudentOverviewApp()

        for index in range(0, len(STUDENTS)):
            student = STUDENTS[index]

            student_overview_app.student_list_text.insert(f'{index + 1}.0', f'- {student.name()}\n')

        student_overview_app.student_list_text['state'] = DISABLED

        student_overview_app.app.mainloop()

    except KeyboardInterrupt:
        print('Successfully closed application')


if __name__ == '__main__':
    main()
