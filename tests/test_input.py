
from vimish.input import InputMachine, normal
import re

def split_input(input):
    return re.findall('<[\w-]+?>|[\w$]', input)

class CheckInputMachine(InputMachine):
    def press_keys(self, input):
        for press in split_input(input):
            result = self.keypress(press)
            if result is not None:
                yield result

def test_split_input():
    data = split_input("d$yVldiw20gg$<Ctrl-w><Ctrl-W>")
    assert data[:2] == ['d', '$']
    assert data[2:5] == ['y', 'V', 'l']
    assert data[5:12] == ['d', 'i', 'w', '2', '0', 'g', 'g']
    assert data[12] == '$'
    assert data[-2:] == ['<Ctrl-w>', '<Ctrl-W>']

    assert split_input("a a") == ['a', 'a']



def test_simple_dd():
    machine = CheckInputMachine(normal)
    

    call = machine.keypress("d")
    assert call.call
    final = machine.keypress("d")
    assert final.final
    assert final.last_match is call
