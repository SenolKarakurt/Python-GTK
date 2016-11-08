from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Notebook Deneme")
        self.set_border_width(10)
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # ilk sayfa
        self.sayfa1 = Gtk.Box()
        self.sayfa1.set_border_width(10)
        self.sayfa1.add(Gtk.Label("PYTHONGTK"))
        self.notebook.append_page(self.sayfa1, Gtk.Label("ilk tab"))

        # ikinci sayfa
        self.sayfa2 = Gtk.Box()
        self.sayfa2.set_border_width(10)
        self.sayfa2.add(Gtk.Label("Python ile Gtk"))
        self.notebook.append_page(self.sayfa2, Gtk.Label("ikinci tab"))

pencere = MainWindow()
pencere.connect("delete-event", Gtk.main_quit)
pencere.show_all()
Gtk.main()