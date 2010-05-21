

import gtk
import gtksourceview2

ESCAPE = gtk.gdk.keyval_from_name("Escape")


class VimWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
        self.command_mode = True
        self.buffer = gtksourceview2.Buffer()
        self.view = gtksourceview2.View(self.buffer)
        self.status = gtk.Statusbar()
        self.mode_label = gtk.Label("command")
        self.status.add(self.mode_label)
        self.info_label = gtk.Label("") #XXX: put engine infos in there


        #XXX: this handling is absolutely inacceptable
        #     unfortunately gtk has nothing better
        self.connect('key-press-event', self.on_key)
        self.connect('key-release-event', self.on_key)

        self.vbox = gtk.VBox()
        self.add(self.vbox)

        self.vbox.add(self.view)
        self.vbox.pack_start(self.status, False, False)



    def on_key(self, window, event):
        print  event
        #XXX: propper bind handling
        if event.string == "i":
            self.command_mode = False
            self.mode_label.set_text("edit")
            return True
        elif event.keyval==ESCAPE:
            self.mode_label.set_text("command")
            self.command_mode = True
        return self.command_mode

