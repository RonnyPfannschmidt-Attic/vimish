"""
    vimish engine
    ~~~~~~~~~~~~~

    handles input mapping and command processing
"""

from gtk import TextBuffer


class Buffer(object):
    def __init__(self, engine):
        self.engine = engine
        self.text_buffer = TextBuffer()

    @property
    def text(self):
        return self.text_buffer.get_text(
                self.text_buffer.get_start_iter(),
                self.text_buffer.get_end_iter()
                )

    @text.setter
    def text(self, text):
        self.text_buffer.set_text(text)

    def append(self, text):
        self.text_buffer.insert(
                self.text_buffer.get_end_iter(),
                text)

    def __len__(self):
        return self.text_buffer.get_line_count()

class Engine(object):

    def create_buffer(self):
        return Buffer(self)


