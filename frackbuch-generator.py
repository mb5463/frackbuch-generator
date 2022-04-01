import gi
import os
import subprocess
from threading import Thread
from time import sleep
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
from os.path import exists
from random import randrange
from PIL import Image

timeout = 1
make_screen_shots = True
scaleup = False
render_windows = True
autoclose_windows = True

klassen = [{"name": "REPLACE_ME",
            "pages": [
                {"bg": "capture_bold_C_Black_red", "upper": "Max Muster", "lower": "Eric Example"},
                {"bg": "capture_bold_C_Black_blue", "upper": "Beat Beispiel", "lower": "Fancy Dude"},
            ],
            "mitglieder":
            [{"name":"Max Muster",
               "bild":"portraits/REPLACE_ME/a.png",
                               "darkmode": True,
                "widgets":
                    [{"type": "progressBar", "percentage":0.8, "label": "Anwesenheit im Unterricht", "inverted": False},
                     {"type": "progressBar", "percentage":0.3, "label": "Caffeine To Code Conversion Efficiency", "inverted": True},
                     {"type": "switch", "label": "Dark Mode"},
                     {"type": "switch", "enabled": True, "label": "WASD stark abgenutzt"},
                     {"type": "switch", "enabled": False, "label": "Lüfterdrehzahl korreliert mit \nInteresse an der Vorlesung"},
                     {"type": "entry", "label": "Lieblings IDE", "entry": "vim"},
                     {"type": "entry", "label": "Spricht fliessend", "entry": "Python, Java, C"},
                    ],
                "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "zitat": "\"Well, that was fun :D\""
            },
            {"name": "Eric Example",
                "bild":"portraits/REPLACE_ME/b.png",
                "darkmode": True,
                "widgets":
                    [{"type": "progressBar", "percentage":0.8, "label": "Anwesenheit im Unterricht", "inverted": False},
                     {"type": "progressBar", "percentage":0.3, "label": "Caffeine To Code Conversion Efficiency", "inverted": False},
                     {"type": "switch", "label": "Dark Mode"},
                     {"type": "switch", "enabled": True, "label": "WASD stark abgenutzt"},
                     {"type": "switch", "enabled": False, "label": "Lüfterdrehzahl korreliert mit \nInteresse an der Vorlesung"},
                     {"type": "entry", "label": "Lieblings IDE", "entry": "vim"},
                     {"type": "entry", "label": "Spricht fliessend", "entry": "Python, Java, C"},
                    ],
                "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "zitat": "\"Well, that was fun :D\""
            },
            {"name": "Beat Beispiel",
                "bild":"portraits/REPLACE_ME/c.png",
                "darkmode": False,
                "widgets":
                    [{"type": "progressBar", "percentage":0.8, "label": "Anwesenheit im Unterricht", "inverted": False},
                     {"type": "progressBar", "percentage":0.3, "label": "Caffeine To Code Conversion Efficiency", "inverted": False},
                     {"type": "switch", "label": "Dark Mode"},
                     {"type": "switch", "enabled": True, "label": "WASD stark abgenutzt"},
                     {"type": "switch", "enabled": False, "label": "Lüfterdrehzahl korreliert mit \nInteresse an der Vorlesung"},
                     {"type": "entry", "label": "Lieblings IDE", "entry": "vim"},
                     {"type": "entry", "label": "Spricht fliessend", "entry": "Python, Java, C"},
                    ],
                "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "zitat": "\"Well, that was fun :D\""
            },
            {"name": "Fancy Dude",
                "bild":"portraits/REPLACE_ME/d.png",
                "darkmode": True,
                "widgets":
                    [{"type": "progressBar", "percentage":0.8, "label": "Anwesenheit im Unterricht", "inverted": False},
                     {"type": "progressBar", "percentage":0.3, "label": "Caffeine To Code Conversion Efficiency", "inverted": False},
                     {"type": "switch", "label": "Dark Mode"},
                     {"type": "switch", "enabled": True, "label": "WASD stark abgenutzt"},
                     {"type": "switch", "enabled": False, "label": "Lüfterdrehzahl korreliert mit \nInteresse an der Vorlesung"},
                     {"type": "entry", "label": "Lieblings IDE", "entry": "vim"},
                     {"type": "entry", "label": "Spricht fliessend", "entry": "Python, Java, C"},
                    ],
                "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "zitat": "\"Well, that was fun :D\""
            },
            ]}]

class Svg_img():
    def __init__(self, file, x, y, width, height):
        self.file = file
        self.x = str(x)
        self.y = str(y)
        self.width = str(width)
        self.height = str(height)
        self.basepath = os.getcwd() + "/"

    def code(self):
        c = '<image sodipodi:absref="' + self.basepath + self.file + '"\n' + 'xlink:href="../../' + self.file + '"\n' + 'y="' + self.y + '"\n' + 'x="' + self.x + '"\n' + 'id="image911" preserveAspectRatio="none"\n' + 'height="' + self.height + '"\n' + 'width="' + self.width + '"/>\n'
        return c

def svg_head():
    return """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="216mm"
   height="303mm"
   viewBox="0 0 216 303"
   version="1.1"
   id="svg1201"
   inkscape:version="1.0.2 (e86c870879, 2021-01-15)"
   sodipodi:docname="4.svg">
  <defs
     id="defs1195" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.9899495"
     inkscape:cx="-28.101011"
     inkscape:cy="560.86456"
     inkscape:document-units="mm"
     inkscape:current-layer="layer1"
     inkscape:document-rotation="0"
     showgrid="false"
     inkscape:window-width="1920"
     inkscape:window-height="1016"
     inkscape:window-x="1920"
     inkscape:window-y="27"
     inkscape:window-maximized="1" />
  <metadata
     id="metadata1198">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title />
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Ebene 1"
     inkscape:groupmode="layer"
     id="layer1">
"""

def svg_foot():
    return """</g></svg>"""

class ProgressBarWindow(Gtk.Window):
    def __init__(self, mitglied):
        super().__init__(title="")
        self.set_border_width(10)
        self.set_default_size(800, 10)

        grid = Gtk.Grid(column_homogeneous=True, column_spacing=10, row_spacing=10, orientation=Gtk.Orientation.VERTICAL)
        grid.set_column_spacing(12)
        grid.set_row_spacing(12)

        name = Gtk.Label()
        name.set_markup("<big><b>"+ mitglied["name"]+ "</b></big>")
        grid.attach(name, 0, 0, 3, 1)
        if mitglied["darkmode"]:
            self.img = Gtk.Image.new_from_file(f"dark2.png")
        else:
            self.img = Gtk.Image.new_from_file(f"std2.png")
        grid.add(self.img)
        
        last_widget = None
        for widget in mitglied["widgets"]:
            if widget["type"] == "progressBar":
                label = Gtk.Label(label=widget["label"])
                label.set_xalign(0)
                grid.add(label)
                progressbar = Gtk.ProgressBar()
                progressbar.set_fraction(widget["percentage"])
                progressbar.set_inverted(widget["inverted"])
                grid.add(progressbar)
                last_widget = progressbar

            elif widget["type"] == "switch":
                row = Gtk.ListBoxRow()
                hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
                row.add(hbox)
                vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
                hbox.pack_start(vbox, True, True, 0)
                label = Gtk.Label(label=widget["label"], xalign=0)
                vbox.pack_start(label, True, True, 0)
                switch = Gtk.Switch()
                if "Dark Mode" in widget["label"]:
                    switch.set_active(mitglied["darkmode"])
                else:
                    switch.set_active(widget["enabled"])
                switch.props.valign = Gtk.Align.CENTER
                hbox.pack_start(switch, False, True, 0)
                grid.add(row)
                last_widget = row

            elif widget["type"] == "label":
                label = Gtk.Label(label=widget["text"])
                label.set_xalign(0)
                grid.add(label)
                last_widget = label

            elif widget["type"] == "entry":
                row = Gtk.ListBoxRow()
                hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
                row.add(hbox)
                vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
                hbox.pack_start(vbox, True, True, 0)
                label = Gtk.Label(label=widget["label"], xalign=0)
                vbox.pack_start(label, True, True, 0)
                entry = Gtk.Entry()
                entry.set_text(widget["entry"])
                hbox.pack_start(entry, False, True, 0)
                grid.add(row)
                last_widget = row

        raw_text = mitglied["text"]
        text = Gtk.Label(label=raw_text)
        text.set_line_wrap(True)
        grid.attach(text, 1, 1, 2, len(mitglied["widgets"]))

        label = Gtk.Label(label=mitglied["zitat"])
        grid.attach_next_to(label, last_widget, Gtk.PositionType.RIGHT, 2, 1)
        self.add(grid)

def shoot_screen(klasse, mitglied):
    if make_screen_shots:
        subprocess.run(["gnome-screenshot", "-w", "-d", str(timeout), "-f", "window/"+klasse+"/"+mitglied+".png"])
    else:
        sleep(timeout*2)

if not exists("window"):
    os.mkdir("window")

if not exists("pages"):
    os.mkdir("pages")

for klasse in klassen:
    if not exists("window/"+klasse["name"]):
        os.mkdir("window/"+klasse["name"])
    if not exists("pages/"+klasse["name"]):
        os.mkdir("pages/"+klasse["name"])

if render_windows:
    active_window = None
    active_theme = subprocess.check_output(["gsettings", "get", "org.gnome.desktop.interface", "gtk-theme"]).decode('utf-8')
    for klasse in klassen:
        for mitglied in klasse["mitglieder"]:
            if not exists("portraits/"+klasse["name"]+"/"+mitglied["name"]+".png") and exists(mitglied["bild"]):
                os.rename(mitglied["bild"], "portraits/"+klasse["name"]+"/"+mitglied["name"]+".png")
            current_theme = subprocess.check_output(["gsettings", "get", "org.gnome.desktop.interface", "gtk-theme"]).decode('utf-8')
            if mitglied["darkmode"] and not current_theme == 'Adwaita-dark':
                os.system("""gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'""")
            elif not mitglied["darkmode"] and not current_theme == 'Adwaita':
                os.system("""gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita'""")
            if scaleup:
                os.system("""gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "[{'Gdk/WindowScalingFactor', <5>}]" && gsettings set org.gnome.desktop.interface scaling-factor 5""")
            active_window = ProgressBarWindow(mitglied)
            active_window.connect("destroy", Gtk.main_quit)
            active_window.show_all()
            if autoclose_windows:
                window_thread = Thread(target=Gtk.main)
                window_thread.start()
            else:
                Gtk.main()
            shoot_screen(klasse["name"], mitglied["name"])
            if autoclose_windows:
                active_window.destroy()
            if scaleup:
                os.system("""gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "[{'Gdk/WindowScalingFactor', <1>}]" && gsettings set org.gnome.desktop.interface scaling-factor 1""")
                sleep(timeout*2)
            #window_thread.join()
    
    
    subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", active_theme])

for klasse in klassen:
    page_no = 0
    s_wid = 190
    for page in klasse["pages"]:
        r1 = 3
        r2 = 3
        #r1 = randrange(6)
        #r2 = randrange(6)
        bg = Svg_img("img/"+page["bg"]+".png", 0, 0, 216, 382.26562)
        
        upper_png = "window/"+klasse["name"]+"/"+page["upper"]+".png"
        p = Image.open(upper_png)
        wid, hgt = p.size
        s_hgt = hgt / (wid / s_wid)
        margin = (216 - 190) /2
        upper = Svg_img(upper_png, margin, 5, s_wid, s_hgt)
        up = Svg_img("portraits/"+klasse["name"]+"/"+page["upper"]+".png", margin +12, 23, 41, 54)
        
        lower_png = "window/"+klasse["name"]+"/"+page["lower"]+".png"
        p = Image.open(lower_png)
        wid, hgt = p.size
        s_hgt = hgt / (wid / s_wid)
        y_pos = 303 - s_hgt - 5
        margin = (216 - 190) /2
        lower = Svg_img(lower_png, margin, y_pos, s_wid, s_hgt)
        
        lp = Svg_img("portraits/"+klasse["name"]+"/"+page["lower"]+".png", margin +12, y_pos+22, 41, 54)
        svg_out = svg_head() + bg.code() + upper.code()+ lower.code() + up.code() + lp.code() + svg_foot()
        svg_out_name = "pages/"+klasse["name"]+"/"+str(page_no)+".svg"
        pdf_out_name = "pages/"+klasse["name"]+"/"+str(page_no)+".pdf"
        with open(svg_out_name, "w") as f:
            f.write(svg_out)
        subprocess.Popen(["/usr/bin/inkscape", "--export-filename="+pdf_out_name, "--export-type=pdf", "--export-dpi=1000", "--export-pdf-version=1.5", svg_out_name])
        page_no += 1
