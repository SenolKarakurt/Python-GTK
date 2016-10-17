from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Grid Example")
        grid = Gtk.Grid()
        self.add(grid)

        buton1 = Gtk.Button(label="Buton 1")
        buton2 = Gtk.Button(label="Buton 2")
        buton3 = Gtk.Button(label="Buton 3")
        buton4 = Gtk.Button(label="Buton 4")
        buton5 = Gtk.Button(label="Buton 5")
        buton6 = Gtk.Button(label="Buton 6")

        grid.add(buton1)
        grid.attach(buton2, 1, 0, 2, 1)
        grid.attach_next_to(buton3, buton1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(buton4, buton3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(buton5, 1, 2, 1, 1)
        grid.attach_next_to(buton6, buton5, Gtk.PositionType.RIGHT, 1, 1)

pencere = MainWindow()
pencere.connect("delete-event", Gtk.main_quit)
pencere.show_all()
Gtk.main()