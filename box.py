from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="BOX")

        #kutu
        self.kutu = Gtk.Box(spacing=50)
        self.add(self.kutu)

        #birinci button
        self.birinci_button = Gtk.Button(label="birinci")
        self.birinci_button.connect("clicked",self.birinci_tikla)
        self.kutu.pack_start(self.birinci_button, True, True, 0)

        #ikinci button
        self.ikinci_button = Gtk.Button(label="ikinci")
        self.ikinci_button.connect("clicked", self.ikinci_tikla)
        self.kutu.pack_start(self.ikinci_button, True, True, 0)

    def birinci_tikla(self, widget):
        print("birinci butona tiklandi!!!")

    def ikinci_tikla(self, widget):
         print("ikinci butona tiklandi!!!")

pencere = MainWindow()
pencere.connect("delete-event", Gtk.main_quit)
pencere.show_all()
Gtk.main()