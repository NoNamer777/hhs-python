FIRST_NAME_KEY = 'firstname'
LAST_NAME_KEY = 'lastname'


class Student:
    _firstname: str = None
    _lastname: str = None

    def __init__(self, **kwargs):
        firstname = kwargs[FIRST_NAME_KEY]
        lastname = kwargs[LAST_NAME_KEY]

        self.firstname = firstname if firstname is not None else None
        self.lastname = lastname if lastname is not None else None

    def name(self) -> str:
        return f'{self.firstname} {self.lastname}'

    @property
    def firstname(self) -> str:
        return self._firstname

    @firstname.setter
    def firstname(self, firstname: str) -> None:
        self._firstname = firstname

    @property
    def lastname(self) -> str:
        return self._lastname

    @lastname.setter
    def lastname(self, lastname) -> None:
        self._lastname = lastname
