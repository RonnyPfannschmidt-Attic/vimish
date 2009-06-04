

class Match(object):
    pass



class numbered(object):
    def __init__(self, *commands, **kw):
        self.commands = commands,
        self.args = kw

    def match(self,input):
        for cmd, tree in self.commands:
            if cmd == input:
                #XXX: aliases
                return Match(next_tree=tree)

        return Match(reset=any(
                        cmd.startswith(input)
                        for cmd, _ in self.commands))



def alias(x):
    return x
remove = copy = alias
word = full_word = eol = line = alias
select = alias

normal = numbered(
    ('d', numbered(
        ('d', alias('Vl')),
        ('w', select(word)),
        ('iw', select(full_word)),
        ('$', select(eol)),
        ('Vl', select(line)),
        call=remove)), 

    ('y', numbered(
        ('y', alias('Vl')),
        ('w', select(word)),
        ('iw', select(full_word)),
        ('$', select(eol)),
        ('Vl', select(line)),
        call=copy)),


)



class InputMachine(object):
    def __init__(self, tree):
        self.tree = tree
        self.current = tree
        self.input = ""


    def keypress(self, press):
        #XXX: this is ugly painfull shit
        if press == '<Esc>':
            self.current = self.tree
            self.input = ""
        else:
            self.input += press

        match = self.current.match(''.join(self.input))
        if match.next_tree is not None:
            self.current = match.next_tree
        elif match.reset:
            self.current = self.tree
            self.input.clear()
        elif match.final:
            return match


