"""
Author: Oscar Wellner, 21144192
Date: 2021-10-30
About:    This Python script will create a GUI app with the Tkinter module.
          The application is split up in 2 tabs with a Notebook element.
          The first tab is the main menu which will show a banner and an area to hold some text,
          the second tab will show the actual Student data in 2 Text widgets for the first- and last name
          of a Student.
"""
from tkinter.constants import DISABLED

from student import Student
from studentOverviewApp import StudentOverviewApp

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

            student_overview_app\
                .student_first_name_text_widget\
                .insert(f'{index + 3}.0', f'{index + 1}. {student.firstname}\n')
            student_overview_app\
                .student_last_name_text_widget\
                .insert(f'{index + 3}.0', f'{student.lastname}\n')

        student_overview_app.student_first_name_text_widget['state'] = DISABLED
        student_overview_app.student_last_name_text_widget['state'] = DISABLED

        student_overview_app.app.mainloop()

    except KeyboardInterrupt:
        print('Successfully closed application')


if __name__ == '__main__':
    main()
