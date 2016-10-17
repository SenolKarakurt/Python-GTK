from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Buton tiklama")

        #Buton
        self.button = Gtk.Button(label="Buraya tikla!!")
        self.button.connect("clicked", self.buton_tikla)
        self.add(self.button)

    #Buton hareketi
    def buton_tikla(self, widget):
        print("PYTHONGTK")

pencere = MainWindow()
pencere.connect("delete-event", Gtk.main_quit)
pencere.show_all()
Gtk.main()
