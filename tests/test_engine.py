

def test_buffer_line_count(engine):
    buffer = engine.create_buffer()

    buffer.text = "Test\ntest2"
    assert len(buffer) == 2

    buffer.append("\n")
    assert len(buffer) == 3

    buffer.text = "one line"
    assert len(buffer) == 1


def test_buffer_slice(engine):
    buffer = engine.create_buffer()
    buffer.text = "Test text\n\nline2"
    assert len(buffer) == 3

    assert buffer[1] == "\n"

    print repr(buffer.text)

    buffer[1] = "Test\n"

    print repr(buffer.text)

    assert buffer[1] == "Test\n"
    assert buffer[2] == "line2"
