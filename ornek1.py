from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Pizza")
        self.set_border_width(10)
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listbox)

        # Checkbox
        satir1 = Gtk.ListBoxRow()
        kutu1  = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        satir1.add(kutu1)
        label = Gtk.Label("Pizza sever misiniz?:")
        check = Gtk.CheckButton()
        kutu1.pack_start(label, True, True, 0)
        kutu1.pack_start(check, True, True, 0)
        listbox.add(satir1)

        # basma butonlu anahtar
        satir2 = Gtk.ListBoxRow()
        kutu2  = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        satir2.add(kutu2)
        label = Gtk.Label("Lahmacun ister misiniz?")
        switch = Gtk.Switch()
        kutu2.pack_start(label, True, True, 0)
        kutu2.pack_start(switch, True, True, 0)
        listbox.add(satir2)

pencere = MainWindow()
pencere.connect("delete-event", Gtk.main_quit)
pencere.show_all()
Gtk.main()