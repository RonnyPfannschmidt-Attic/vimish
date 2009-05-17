"""
    vimish buffer
    ~~~~~~~~~~~~~

    simple interface to various textbuffer implementations

    :copyright: 2009 by Ronny Pfannschmidt
    :license: LGPL 2 or later
"""

from gtk import TextBuffer


class Buffer(object):
    def __init__(self, engine):
        self.engine = engine
        self.text_buffer = TextBuffer()
        self.bufnr = engine.add(self)

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

        self.text_buffer.delete(start, end)

        if isinstance(item, int):
            start = self.text_buffer.get_iter_at_line(item)
        elif item.start is None:
            start = self.text_buffer.get_start_iter()
        else:
            start = self.text_buffer.get_iter_at_line(item.start)
        self.text_buffer.insert(start, value)
