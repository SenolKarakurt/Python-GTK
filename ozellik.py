from gi.repository import Gtk

pencere = Gtk.Window()

label = Gtk.Label()
label.set_label("SENOLKARAKURT")
label.set_angle(20)
label.set_halign(Gtk.Align.END)
pencere.add(label)
print(label.get_properties("angle"))

pencere.connect("delete-event", Gtk.main_quit)
pencere.show_all()
Gtk.main()