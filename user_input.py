from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Giris Ekrani")
        self.set_border_width(10)
        self.set_size_request(200, 100)

        # Duzenleme
        kutu = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.add(kutu)

        # Username
        self.kullanici_adi = Gtk.Entry()
        self.kullanici_adi.set_text("Username")
        kutu.pack_start(self.kullanici_adi, True, True, 0)

        # Password
        self.sifre = Gtk.Entry()
        self.sifre.set_text("Password")
        self.sifre.set_visibility(False)
        kutu.pack_start(self.sifre, True, True, 0)

        # Giris yap butonu
        self.buton = Gtk.Button(label="Giris Yap")
        self.buton.connect("clicked", self.giris) # Butona tiklandigi anda giris fonksiyonunu cagirir.
        kutu.pack_start(self.buton, True, True, 0)

    def giris(self, widget):
        print(self.kullanici_adi.get_text()) # kullanici adini alir ve ekrana basar
        print(self.sifre.get_text()) # sifreyi alir ve ekrana basar

pencere = MainWindow()
pencere.connect("delete-event", Gtk.main_quit)
pencere.show_all()
Gtk.main()