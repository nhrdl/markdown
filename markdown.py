#!/usr/bin/python

import gtk
import glib
import webkit 

import argparse
parser = argparse.ArgumentParser()
parser.parse_args()


idle_index = ""


view = webkit.WebView()
sw = gtk.ScrolledWindow() 
sw.add(view) 

win = gtk.Window(gtk.WINDOW_TOPLEVEL)
vbox = gtk.VBox()
win.add(vbox)
vbox.add(sw)
sw.set_size_request(900, 900)

win.show_all() 
win.connect("delete-event", gtk.main_quit)
view.open("file:///home/niranjan/work/markdown/test.html");
win.maximize()
#idle_index=glib.idle_add(idleHookFunction)
gtk.main()

