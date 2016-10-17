from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Anahtarlayici")
        self.set_border_width(10)
        kutu = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(kutu)

        # Stack
        alan = Gtk.Stack()
        alan.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        alan.set_transition_duration(2000)

        # Checkbox
        check_button = Gtk.CheckButton("Secme yapma")
        alan.add_titled(check_button, "check_adi", "Check Box")

        # Label
        label = Gtk.Label()
        label.set_markup("<big>SENOLKARAKURT</big>")
        alan.add_titled(label, "label_adi", "Buyuk Label")

        # StackSwitcher
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(alan)
        kutu.pack_start(stack_switcher, True, True, 0)
        kutu.pack_start(alan, True, True, 0)

pencere = MainWindow()
pencere.connect("delete-event", Gtk.main_quit)
pencere.show_all()
Gtk.main()