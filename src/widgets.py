# coding: utf-8

try:
    import tkinter as tk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import tkFileDialog as filedialog


class Widget(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        tk.LabelFrame.__init__(self, master, *args, **kwargs)

    
class WidgetEntry(Widget):
    def __init__(self, master, *args, **kwargs):
        Widget.__init__(self, master, *args, **kwargs)
        self._entry = tk.Entry(self)
        self._entry.pack(side="left", fill="x", expand=True, padx=1, pady=1)

    def entry(self):
        return self._entry
    
    def value(self):
        return self._entry.get()


class WidgetEntryDirectory(WidgetEntry):
    def __init__(self, master, *args, **kwargs):
        WidgetEntry.__init__(self, master, *args, **kwargs)
        self._button = tk.Button(self, text="Find",
                                 command=self.ask_directory)
        self._button.pack(side="left", padx=1, pady=1)

    def ask_directory(self):
        directory = filedialog.askdirectory()
        self.entry().delete(0, "end")
        self.entry().insert("end", directory)


class WidgetSlider(Widget):
    def __init__(self, master, minimum=1, maximum=1000, *args, **kwargs):
        Widget.__init__(self, master, *args, **kwargs)
        # minimum and maximum
        self.set_minimum(minimum)
        self.set_maximum(maximum)

        # spinbox
        _stringvar = tk.StringVar()
        self._spinbox = tk.Spinbox(self, from_=self.minimum(),
                                            to=self.maximum(),
                                      textvariable=_stringvar) 
        self._spinbox.pack(side="left", anchor="s", padx=1, pady=1)

        # scale
        self._scale = tk.Scale(self, orient="horizontal", 
                                    from_=self.minimum(),
                                       to=self.maximum())
        self._scale.pack(side="left", fill="x", expand=True, 
                                                 anchor="s",
                                             padx=1, pady=1)

        # commands
        self._spinbox["command"] = self.update_scale
        self._scale["command"] = self.update_spinbox

    def update_spinbox(self, *args):
        self._spinbox.delete(0, "end")
        self._spinbox.insert("end", str(self._scale.get()))

    def update_scale(self, *args):
        current_spinbox_value = (int(self._spinbox.get()) if 
                                self._spinbox.get().isdigit() else 
                                                    self.minimum())
        self._scale.set(current_spinbox_value)

    def value(self):
        return self._scale.get()

    def minimum(self):
        return self._minimum

    def maximum(self):
        return self._maximum

    def set_minimum(self, minimum):
        self._minimum = minimum

    def set_maximum(self, maximum):
        self._maximum = (maximum if maximum > self.minimum() else 
                                                self.minimum()+1)

    def set_value(self, value):
        if self.minimum() <= value <= self.maximum():
            self._scale.set(value)
        else:
            self._scale.set(self.minimum())
        self.update_spinbox()


class WidgetOptionMenu(Widget):
    def __init__(self, master, values=None, *args, **kwargs):
        Widget.__init__(self, master, *args, **kwargs)
        # menu
        values = values or [""]
        self._stringmenu = tk.StringVar()
        self._stringmenu.set(values[0])
        self._menu = tk.OptionMenu(self, self._stringmenu, *values)
        self._menu.pack(fill="x", padx=1, pady=1)

    def value(self):
        return self._stringmenu.get()

    def set_values(self, values):
        self._stringmenu.set(values[0])
        self._menu.children["menu"].delete(0, "end")
        for value in values:
            self._menu.children["menu"].add_command(label=value, command=lambda string=value: self._stringmenu.set(string))


class UiReduzirImagem(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self._input = WidgetEntryDirectory(self, text="Input")
        self._output = WidgetEntryDirectory(self, text="Output")
        self._optionmenu = WidgetOptionMenu(self, text="New Extension",
                                                values=[".jpg", ".png"])
        self._width = WidgetSlider(self, text="New width", maximum=3000)
        self._height = WidgetSlider(self, text="New width", maximum=3000)
        self._button = tk.Button(self, text="Execute")

        self._input.pack(fill="x", padx=5, pady=5)
        self._output.pack(fill="x", padx=5, pady=5)
        self._optionmenu.pack(fill="x", padx=5, pady=5)
        self._width.pack(fill="x", padx=5, pady=5)
        self._height.pack(fill="x", padx=5, pady=5)
        self._button.pack(padx=5, pady=5)

    def execute(self):
        self.geometry("500x500")
        self.mainloop()

    def button(self):
        return self._button

    def value(self):
        return {"input":self._input.value(),
                "output":self._output.value(),
                "optionmenu":self._optionmenu.value(),
                "width":self._width.value(),
                "height":self._height.value()}

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")

    widget_entry = WidgetEntry(root, text="entry")
    widget_entry.pack(fill="x", padx=5, pady=5)
    
    widget_slider = WidgetSlider(root, text="width")
    widget_slider.set_value(-12)
    widget_slider.pack(fill="x", padx=5, pady=5)

    widget_directory = WidgetEntryDirectory(root, text="directory")
    widget_directory.pack(fill="x", padx=5, pady=5)

    widget_option_menu = WidgetOptionMenu(root, text="ext", values=[".png", ".jpg"])
    widget_option_menu.pack(fill="x", padx=5, pady=5)
    
    root.mainloop()
