FIRST_NAME_KEY = 'firstname'
LAST_NAME_KEY = 'lastname'


class Student:
    _firstname: str = None
    _lastname: str = None

    def __init__(self, **kwargs):
        self.firstname = kwargs.get(FIRST_NAME_KEY)
        self.lastname = kwargs.get(LAST_NAME_KEY)

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
