

import gtk
import gtksourceview

ESCAPE = gtk.gdk.keyval_from_name("Escape")


class VimWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
        self.command_mode = True
        self.buffer = gtksourceview.SourceBuffer()
        self.view = gtksourceview.SourceView(self.buffer)

        #XXX: this handling is absolutely inacceptable
        #     unfortunately gtk has nothing better
        self.connect('key-press-event', self.on_key)
        self.connect('key-release-event', self.on_key)

        self.vbox = gtk.VBox()
        self.add(self.vbox)

        self.vbox.add(self.view)



    def on_key(self, window, event):
        print  event
        if event.string == "i":
            self.command_mode = False
            return True
        elif event.keyval==ESCAPE:
            self.command_mode = True
        return self.command_mode

