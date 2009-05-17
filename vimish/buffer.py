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
                self._start_iter(),
                self._stop_iter()
                )

    @text.setter
    def text(self, text):
        self.text_buffer.set_text(text)

    def append(self, text):
        self.text_buffer.insert(
                self._stop_iter(),
                text)

    def __len__(self):
        return self.text_buffer.get_line_count()

    def __getitem__(self, item):
        start, end = self._iter_range(item)
        slice = self.text_buffer.get_slice(start, end)
        if isinstance(item, int):
            return slice
        else:
            return slice.splitlines(True)

    def __delitem__(self, item):
        start, end = self._iter_range(item)
        self.text_buffer.delete(start, end)

    def __setitem__(self, item, value):
        if isinstance(value, list):
            #XXX: smarter?
            value = ''.join(value)

        del self[item]

        start = self._start_iter(item)
        self.text_buffer.insert(start, value)

    def _start_iter(self, pos=None):
        if isinstance(pos, int):
            return self._iter_at_line(pos)
        elif pos is None or pos.start is None:
            return self.text_buffer.get_start_iter()
        else:
            return self._iter_at_line(pos.start)

    def _stop_iter(self, pos=None):
        if pos is None:
            return self.text_buffer.get_end_iter()
        elif isinstance(pos, int):
            # end of line iter = start of next line
            if pos+1 < len(self):
                return self._iter_at_line(pos+1)
            else:
                return self._stop_iter()
        else:
            if pos.stop is None:
                return self._stop_iter()
            elif pos.stop <=len(self):
                return self._iter_at_line(pos.stop)
            else:
                self._stop_iter()

    def _iter_range(self, slice):
        start = self._start_iter(slice)
        stop = self._stop_iter(slice)
        return start, stop

    def _iter_at_line(self, line):
        return self.text_buffer.get_iter_at_line(line)
