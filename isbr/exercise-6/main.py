# Author: Oscar Wellner, 21144192
# Date: 2021-09-23
# About:    This Python script will read the CSV file for this exercise, create Student objects from the data
#           presented in that file, put them in a list, and finally print the created Students to the console.

import csv

FIRST_NAME_KEY = 'first_name'
LAST_NAME_KEY = 'last_name'


class Student:
    def __init__(self, **kwargs):
        self._first_name = kwargs[FIRST_NAME_KEY] if FIRST_NAME_KEY in kwargs else None
        self._last_name = kwargs[LAST_NAME_KEY] if LAST_NAME_KEY in kwargs else None

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        self._last_name = last_name

    def __repr__(self) -> str:
        return f'Student{{ name: \'{self.first_name} {self.last_name}\' }}'


def create_student_list() -> list[Student]:
    students = []

    with open('data.csv', 'r') as students_file:
        csv_reader = csv.DictReader(students_file)

        for student_data in csv_reader:
            students.append(Student(
                first_name=student_data['first_name'],
                last_name=student_data['last_name']
            ))

    return students


def main() -> None:
    students = create_student_list()

    for student in students:
        print(student)


if __name__ == '__main__':
    main()
