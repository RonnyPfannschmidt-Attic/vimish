

def test_buffer_line_count(engine):
    buffer = engine.create_buffer()
    buffer.text = "Test\ntest2"
    assert len(buffer) == 2
    buffer.append("\n")
    assert len(buffer) == 3


