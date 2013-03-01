#!/usr/bin/python

import gtk
import glib
import webkit 
import os;
import argparse

class App:
    
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("file", help="Markdown file")
        args = parser.parse_args()


        toolbar = gtk.Toolbar()
        toolbar.set_style(gtk.TOOLBAR_ICONS)
        savetb = gtk.ToolButton(gtk.STOCK_SAVE)
        sep = gtk.SeparatorToolItem()
        quittb = gtk.ToolButton(gtk.STOCK_QUIT)
        toolbar.insert(savetb, 0)
        toolbar.insert(sep, 1)
        toolbar.insert(quittb, 2)
        
        self.view = webkit.WebView()
        sw = gtk.ScrolledWindow() 
        sw.add(self.view) 

        win = gtk.Window(gtk.WINDOW_TOPLEVEL)
        vbox = gtk.VBox()
        vbox.pack_start(toolbar, False, False, 0)
        win.add(vbox)
        vbox.add(sw)

        win.show_all() 
        win.connect("delete-event", gtk.main_quit)
        self.view.open("file://" + os.path.abspath(args.file))
        win.maximize()
#idle_index=glib.idle_add(idleHookFunction)

App()        
gtk.main()

