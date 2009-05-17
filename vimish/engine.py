"""
    vimish engine
    ~~~~~~~~~~~~~

    handles input mapping and command processing

    :copyright: 2009 by Ronny Pfannschmidt
    :license: LGPL2 or later
"""

from gtk import TextBuffer


class Engine(object):

    def __init__(self):
        self.buffers = []

    def add(self, buffer):
        self.buffers.append(buffer)
        return len(self.buffers) # buffer id

    def remove(self, buffer):
        self.buffers[buffer.burnr] = None
        buffer.bufnr = None
