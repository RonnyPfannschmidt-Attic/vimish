from vimish.engine import Engine
from vimish.buffer import Buffer


class ConftestPlugin:
    def pytest_funcarg__engine(self, request):
        return Engine()

    def pytest_funcarg__buffer(self, request):
        return Buffer(Engine())
