from vimish.engine import Engine
from vimish.buffer import Buffer


def pytest_funcarg__engine(request):
    return Engine()

def pytest_funcarg__buffer(request):
    return Buffer(Engine())
