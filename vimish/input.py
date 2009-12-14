
class Match(object):
    __slots__ = "next_tree", "call", "reset", "final", "_last_match", "count"
    def __init__(self,
                 next_tree=None,
                 call=None,
                 reset=None,
                 final=None,
                 last_match=None,
                 count=None):
        self.next_tree = next_tree
        self.call = call
        self.reset = reset
        self.final = final
        self._last_match = last_match
        self.count = count

    def __repr__(self):
        return "<Match %s>" %' '.join(
                "%s=%r"%(x, getattr(self, x)) 
                for x in self.__slots__ if x[0]!='_' and getattr(self, x) is not None)

    @property
    def previous_actor(self):
        def components(x):
            while x is not None:
                x = x._last_match
                yield x

        for c in components(self):
            if c.next_tree is not None:
                return c


class numbered(object):
    final = False

    def __init__(self, *commands, **kw):
        self.commands = commands
        self.args = kw

    def match(self, input, last_match):
        nondigits = input.lstrip("0123456789")
        digits = input[:-len(nondigits)] if nondigits else input
        number = int(digits) if digits else 1
        if not nondigits:
            return Match(count=number, last_match=last_match)
        for cmd, tree in self.commands:
            if cmd == nondigits:
                return Match(
                        next_tree=tree,
                        final=tree.final,
                        count=number,
                        last_match=last_match,
                        call=(tree.args.get('call') or 
                              last_match.call))
    
        return Match(reset=any(
                        cmd[0].startswith(input)
                        for cmd in self.commands),
                     last_match=last_match)

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
            match = Match(reset=True, next_tree=self.tree)
        else:
            self.input += press
            match = self.current.match(''.join(self.input), self.match)

        self.match = match
        if match.next_tree is not None:
            self.current = match.next_tree
            self.input = ""

        if match.reset or match.final:
            self.current = self.tree
            self.input = ""

        return match


