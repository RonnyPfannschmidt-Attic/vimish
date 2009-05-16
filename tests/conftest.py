
from vimish.engine import Engine


class ConftestPlugin:
    def pytest_funcarg__engine(self, request):
        return Engine()
