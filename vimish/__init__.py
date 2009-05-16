"""
    vim alike editing ui on top of gtksourceview

"""
import gtk
from .ui import VimWindow


def main(args):
    window = VimWindow()
    window.connect("destroy", gtk.main_quit)
    window.show_all()
    gtk.main()

