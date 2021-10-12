# Author: Oscar Wellner, 21144192
# Date: 2021-09-19
# About:    This Python script demonstrates how to create an instance of a Python Class.
#           put them in a list, and print them to the console.

LAST_NAME_KEY = 'last_name'
FIRST_NAME_KEY = 'first_name'


class Student:
    def __init__(self, **kwargs):
        self._last_name = kwargs[LAST_NAME_KEY] if LAST_NAME_KEY in kwargs else None
        self._first_name = kwargs[FIRST_NAME_KEY] if FIRST_NAME_KEY in kwargs else None

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name) -> None:
        self._last_name = last_name

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name) -> None:
        self._first_name = first_name

    def __repr__(self) -> str:
        return f'Student{{ name: \'{self.first_name} {self.last_name}\' }}'


def main():
    student1 = Student(first_name='Oscar', last_name='Wellner')
    student2 = Student(first_name='Menno', last_name='Wellner')

    students = [student1, student2]

    for student in students:
        print(student)


if __name__ == '__main__':
    main()
