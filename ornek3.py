from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Header Bar")
        self.set_border_width(10)
        self.set_default_size(1000, 600)

        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = "HEADER BAR"
        self.set_titlebar(header_bar)

        # Olusturulan kutu da baglanmis ogeler
        kutu = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(kutu.get_style_context(), "linked")

        # Sol ok isareti
        sol_ok = Gtk.Button()
        sol_ok.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        kutu.add(sol_ok)

        # Sag ok isareti
        sag_ok = Gtk.Button()
        sag_ok.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        kutu.add(sag_ok)

        header_bar.pack_start(kutu)
        self.add(Gtk.TextView())

pencere = MainWindow()
pencere.connect("delete-event", Gtk.main_quit)
pencere.show_all()
Gtk.main()