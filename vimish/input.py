
class Match(object):
    def __init__(self, next_tree=None, call=None, reset=None, final=None, last_match=None):
        self.next_tree = next_tree
        self.call = call
        self.reset = reset
        self.final = final
        self.last_match = last_match


class numbered(object):
    final = False

    def __init__(self, *commands, **kw):
        self.commands = commands
        self.args = kw

    def match(self, input, last_match):
        print self
        for cmd, tree in self.commands:
            print cmd, tree, input
            if cmd == input:
                print "hit"
                #XXX: aliases
                print self.args
                print last_match.call
                return Match(
                        next_tree=tree,
                        final=tree.final,
                        last_match = last_match,
                        call=(tree.args.get('call') or 
                              last_match.call))
    
        return Match(reset=any(
                        cmd[0].startswith(input)
                        for cmd in self.commands))

    def __repr__(self):
        return "<Numbered %r (%s)>"%(
                self.args, 
                ' '.join(cmd 
                         for cmd, tree in self.commands)
                )

class alias(str):
    args = {} #XXX
    final = True
    def __repr__(self):
        return "alias(%s)"%self

class select(object):
    args = {} #XXX
    final = True
    def __init__(self, selector):
        self.selector = selector

    def __repr__(self):
        return '<Selector %r>'%self.selector


remove = "remove"
copy = "copy"
word = "word"
full_word = "full_word" 
eol = "eol"
line = "line"

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
        self.match = Match()
        self.input = ""


    def keypress(self, press):
        #XXX: this is ugly painfull shit
        if press == '<Esc>':
            self.current = self.tree
            self.input = ""
            self.match = Match()
        else:
            self.input += press

        match = self.current.match(''.join(self.input), self.match)
        self.match = match
        if match.next_tree is not None:
            self.current = match.next_tree
            self.input = ""
        elif match.reset or match.final:
            self.current = self.tree
            self.input = ""
            self.match = Match()

        return match


