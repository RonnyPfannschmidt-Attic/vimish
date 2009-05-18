from vimish.buffer import Buffer

import py.test
from operator import itemgetter

def test_engine_buffer_id(engine):

    buffer = Buffer(engine)
    buffer2 = Buffer(engine)

    assert buffer.bufnr == 1
    assert buffer2.bufnr == 2

def test_buffer_line_count(buffer):

    buffer.text = "Test\ntest2"
    assert len(buffer) == 2

    buffer.append("\n")
    assert len(buffer) == 3

    buffer.text = "one line"
    assert len(buffer) == 1


def test_buffer_setitem_and_getitem(buffer):

    buffer.text = "Test text\n\nline2"
    assert len(buffer) == 3

    assert buffer[1] == "\n"

    print repr(buffer.text)

    buffer[1] = "Test\n"

    print repr(buffer.text)

    assert buffer[1] == "Test\n"
    assert buffer[2] == "line2"


def test_buffer_get_slice_and_set_slice(buffer):

    buffer.text = "Test\nslicing\nwell"

    assert buffer[:2] == ["Test\n", "slicing\n"]
    assert buffer[2:] == ['well']

    buffer[:2] = ['more\n', 'slicing\n', 'helps\n']
    assert buffer[2] == "helps\n"



def test_buffer_del_slice(buffer):

    buffer.text = "Test\ndelete\na\nslice\n"

    del buffer[0]
    assert buffer.text == "delete\na\nslice\n"

    del buffer[:2]
    assert buffer.text == "slice\n"


def test_buffer_wrong_index(buffer):

    buffer.text = "Test\na\nbuffer"
    assert py.test.raises(IndexError, "buffer[30]")


def test_buffer_negative_index(buffer):

    buffer.text = "Test\na\nbuffer"
    
    assert buffer[5:6] == []

