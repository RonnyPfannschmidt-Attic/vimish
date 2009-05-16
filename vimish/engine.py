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

    def __getitem__(self, item):
        if isinstance(item, int):
            start = self.text_buffer.get_iter_at_line(item)
            # the last line doesnt end with \n
            if item+1 < len(self):
                end = self.text_buffer.get_iter_at_line(item +1)
            else:
                end = self.text_buffer.get_end_iter()
            return self.text_buffer.get_slice(start, end)
        else:
            if item.start is None:
                start = self.text_buffer.get_start_iter()
            else:
                start = self.text_buffer.get_iter_at_line(item.start)

            if item.stop is None or item.stop >= len(self):
                end = self.text_buffer.get_end_iter()
            else:
                end = self.text_buffer.get_iter_at_line(item.stop)

            slice = self.text_buffer.get_slice(start, end)
            return slice.splitlines(True)


    def __setitem__(self, item, value):
        if isinstance(value, list):
            #XXX: smarter?
            value = ''.join(value)


        if isinstance(item, int):
            start = self.text_buffer.get_iter_at_line(item)
            end = self.text_buffer.get_iter_at_line(item +1)
        else:
            if item.start is None:
                start = self.text_buffer.get_start_iter()

            end = self.text_buffer.get_iter_at_line(item.stop)

        self.text_buffer.select_range(start, end)
        self.text_buffer.delete_selection(False, False)

        if isinstance(item, int):
            start = self.text_buffer.get_iter_at_line(item)
        elif item.start is None:
            start = self.text_buffer.get_start_iter()
        else:
            start = self.text_buffer.get_iter_at_line(item.start)
        self.text_buffer.insert(start, value)


class Engine(object):

    def create_buffer(self):
        return Buffer(self)


