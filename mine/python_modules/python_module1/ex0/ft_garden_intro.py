from typing import Protocol


class First(Protocol):
    def test():
        ...


class File:
    def test(self):
        return "file data"


class APIResponse:
    def test(self):
        return "api data"


f = File()
a = APIResponse()

f.test()
a.test()
