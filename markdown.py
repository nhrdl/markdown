#!/usr/bin/python

import gtk
import glib
import webkit 

import argparse
parser = argparse.ArgumentParser()
parser.parse_args()


idle_index = ""

toolbar = gtk.Toolbar()
toolbar.set_style(gtk.TOOLBAR_ICONS)
savetb = gtk.ToolButton(gtk.STOCK_SAVE)
sep = gtk.SeparatorToolItem()
quittb = gtk.ToolButton(gtk.STOCK_QUIT)
toolbar.insert(savetb, 0)
toolbar.insert(sep, 1)
toolbar.insert(quittb, 2)
        
view = webkit.WebView()
sw = gtk.ScrolledWindow() 
sw.add(view) 

win = gtk.Window(gtk.WINDOW_TOPLEVEL)
vbox = gtk.VBox()
vbox.pack_start(toolbar, False, False, 0)
win.add(vbox)
vbox.add(sw)
#sw.set_size_request(900, 900)

win.show_all() 
win.connect("delete-event", gtk.main_quit)
view.open("file:///home/niranjan/work/markdown/markdown.html");
win.maximize()
#idle_index=glib.idle_add(idleHookFunction)
gtk.main()

