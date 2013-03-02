#!/usr/bin/python

#import gtk
#import glib
#import webkit 
import os;
import argparse
import gi
from gi.repository import WebKit 
from gi.repository import Gtk 

class MarkdownFile:
    def __init__(self, path):
        self.filePath = path

    def save(self, webview):
        element = self.getTextElement(webview)
        text = element.get_value()
        open(self.filePath, "w").write(text)
        
    def getTextElement(self, frame):
        doc = frame.get_dom_document()
        element = doc.get_element_by_id("wmd-input")
        return element

    def load(self, webview, frame):
        """
        Loads the file from disk if it exists and sets up the value in the html page.
        """
        text = ""
        if (os.path.exists(self.filePath)):
            text = open(self.filePath).read()
            
        element = self.getTextElement(webview)
        element.set_value(text)

        
class App:
    def save(self, arg):
        """"Saves the file to the disk"""
        self.view.mdFile.save(self.view);
    
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("file", help="Markdown file")
        args = parser.parse_args()


        toolbar = Gtk.Toolbar()
        #toolbar.set_style(Gtk.ToobarStyle.GTTOOLBAR_ICONS)
        savetb = Gtk.ToolButton(Gtk.STOCK_SAVE)
        savetb.connect("clicked", self.save)
        sep = Gtk.SeparatorToolItem()
        quittb = Gtk.ToolButton(Gtk.STOCK_QUIT)
        toolbar.insert(savetb, 0)
        toolbar.insert(sep, 1)
        toolbar.insert(quittb, 2)
        
        self.view = WebKit.WebView()
        sw = Gtk.ScrolledWindow() 
        sw.add(self.view) 

        win = Gtk.Window()
        vbox = Gtk.VBox()
        vbox.pack_start(toolbar, False, False, 0)
        win.add(vbox)
        vbox.add(sw)

        win.show_all() 
        win.connect("delete-event", Gtk.main_quit)
        self.view.mdFile = MarkdownFile(os.path.abspath(args.file))
        self.view.connect("document-load-finished", self.view.mdFile.load)
        self.view.open("file://" + os.path.abspath("./markdown.html"))
        win.maximize()
#idle_index=glib.idle_add(idleHookFunction)

App()        
Gtk.main()

