"""
    vimish engine
    ~~~~~~~~~~~~~

    handles input mapping and command processing
"""

from gtk import TextBuffer


class Engine(object):

    def __init__(self):
        self.buffers = []

    def add(self, buffer):
        self.buffers.append(buffer)
        return len(self.buffers)

    def remove(self, buffer):
        self.buffers[buffer.burnr] = None
        buffer.bufnr = None
