

def test_buffer_line_count(engine):
    buffer = engine.create_buffer()

    buffer.text = "Test\ntest2"
    assert len(buffer) == 2

    buffer.append("\n")
    assert len(buffer) == 3

    buffer.text = "one line"
    assert len(buffer) == 1


def test_buffer_setitem_and_getitem(engine):
    buffer = engine.create_buffer()
    buffer.text = "Test text\n\nline2"
    assert len(buffer) == 3

    assert buffer[1] == "\n"

    print repr(buffer.text)

    buffer[1] = "Test\n"

    print repr(buffer.text)

    assert buffer[1] == "Test\n"
    assert buffer[2] == "line2"


def test_buffer_get_slice_and_set_slice(engine):
    buffer = engine.create_buffer()
    buffer.text = "Test\nslicing\nwell"
    assert buffer[:2] == ["Test\n", "slicing\n"]
    assert buffer[2:] == ['well']


    buffer[:2] = ['more\n', 'slicing\n', 'helps\n']
    assert buffer[2] == "helps\n"


