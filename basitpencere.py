from gi.repository import Gtk

pencere = Gtk.Window()
pencere.connect("delete-event", Gtk.main_quit)
pencere.show_all()
Gtk.main()