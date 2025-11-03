#!/usr/bin/env python3
import gi, os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class TextParserApp(Gtk.Window):
    def __init__(self, removal_file: str = "removal_strings.txt"):
        super().__init__(title="Text Parser")
        self.set_default_size(800, 600)
        self.removal_file = removal_file

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(vbox)

        # Input text buffer
        self.input_buffer = Gtk.TextBuffer()
        input_view = Gtk.TextView(buffer=self.input_buffer)
        input_scrolled = Gtk.ScrolledWindow()
        input_scrolled.add(input_view)
        vbox.pack_start(input_scrolled, True, True, 0)

        # Output text buffer
        self.output_buffer = Gtk.TextBuffer()
        output_view = Gtk.TextView(buffer=self.output_buffer)
        output_scrolled = Gtk.ScrolledWindow()
        output_scrolled.add(output_view)
        vbox.pack_start(output_scrolled, True, True, 0)

        # Removal strings buffer
        self.removal_buffer = Gtk.TextBuffer()
        removal_view = Gtk.TextView(buffer=self.removal_buffer)
        removal_scrolled = Gtk.ScrolledWindow()
        removal_scrolled.add(removal_view)
        vbox.pack_start(removal_scrolled, True, True, 0)

        # Parse button
        parse_button = Gtk.Button(label="Parse")
        parse_button.connect("clicked", self.on_parse_clicked)
        vbox.pack_start(parse_button, False, False, 0)

        self.load_removal_strings()
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def load_removal_strings(self):
        if os.path.exists(self.removal_file):
            with open(self.removal_file, "r", encoding="utf-8") as f:
                self.removal_buffer.set_text(f.read())

    def save_removal_strings(self):
        start, end = self.removal_buffer.get_bounds()
        text = self.removal_buffer.get_text(start, end, False)
        with open(self.removal_file, "w", encoding="utf-8") as f:
            f.write(text)

    def on_parse_clicked(self, button):
        start, end = self.input_buffer.get_bounds()
        input_text = self.input_buffer.get_text(start, end, False)
        start, end = self.removal_buffer.get_bounds()
        removal_data = self.removal_buffer.get_text(start, end, False)
        removal_list = [r.strip() for r in removal_data.splitlines() if r.strip()]
        
        for r in removal_list:
            input_text = input_text.replace(r, "")

        self.output_buffer.set_text(input_text)
        self.save_removal_strings()

if __name__ == "__main__":
    app = TextParserApp()
    Gtk.main()
