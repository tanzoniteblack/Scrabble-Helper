#!/usr/bin/python3

import gtk
#from gi.repository import Gtk, GObject, GLib, GdkPixbuf, Pango, Gdk
from findwords import *

class PyApp(gtk.Window):
	def __init__(self):
		super(PyApp, self).__init__()
		
		tiles = "..."
		self.set_title("Anagram Creator")
		self.set_size_request(510, 500)
		self.set_position(1)
		
		vbox = gtk.VBox(False, 3)

		self.label = gtk.Label("Letters in hand: " + tiles)
		vbox.pack_start(self.label, False, False, 10)
		
#		hbox2 = gtk.HBox(True, 2)
#		words7_label = gtk.Label("Words using 7 letters:")
#		hbox2.add(words7_label)
#		vbox.add(hbox2)
		
		hbox_words = gtk.HBox(True, 1)
		
		vbox1 = gtk.VBox(False, 2)
		only_label = gtk.Label("Using only letters given: ")
		vbox1.pack_start(only_label, False, False, 5)
		self.words = gtk.ListStore(str, int, int)
		self.treeView = gtk.TreeView(self.words)
		self.treeView.set_rules_hint(True)
		self.create_columns(self.treeView)
		scrolled1 = gtk.ScrolledWindow()
		scrolled1.add(self.treeView)
		vbox1.pack_start(scrolled1, True, True, 10)
		hbox_words.pack_start(vbox1, True, True, 10)
		
		vbox2 = gtk.VBox(False, 2)
		extra_label = gtk.Label("Using 1 extra letter: ")
		vbox2.pack_start(extra_label, False, False, 5)
		self.words_extra = gtk.ListStore(str, int, int)
		self.extras = gtk.TreeView(self.words_extra)
		self.extras.set_rules_hint(True)
		self.create_columns(self.extras)
		scrolled2 = gtk.ScrolledWindow()
		scrolled2.add(self.extras)
		vbox2.pack_start(scrolled2, True, True, 10)
		hbox_words.pack_start(vbox2, True, True, 10)
		
		vbox.pack_start(hbox_words, True, True, 10)
		
		hbox7 = gtk.HBox(False, 2)
		entry = gtk.Entry()
		entry.add_events(2048)
		hbox7.pack_start(entry, True, True, 10)
		btn1 = gtk.Button("Find Words")
		hbox7.pack_start(btn1, False, False, 10)
		
		vbox.pack_start(hbox7, False, False, 10)
		
#		vbox.set_child_packing(hbox_words, 
		
		entry.grab_focus()
		entry.connect("activate", self.tiles_entered, entry)
		btn1.connect("clicked", self.tiles_entered, entry)
		
		self.connect("destroy", gtk.main_quit)
		self.add(vbox)
		self.show_all()
	
	def tiles_entered(self, widget, entry):
		self.tiles = entry.get_text()
		self.label.set_text("Letters in hand: " + self.tiles)
		results = find_words(self.tiles)
		self.words.clear()
		for result in results["only"]:
			self.words.append([result[0], result[1], result[2]])
		
		self.words_extra.clear()
		for result in results["extra"]:
			self.words_extra.append([result[0], result[1], result[2]])
#		print(results)
	
	def create_columns(self, treeView):
		rendererText = gtk.CellRendererText()
		column = gtk.TreeViewColumn("Word", rendererText, text=0)
		column.set_sort_column_id(0)
		treeView.append_column(column)
		
		rendererText = gtk.CellRendererText()
		column = gtk.TreeViewColumn("Points", rendererText, text=1)
		column.set_sort_column_id(1)
		treeView.append_column(column)

		rendererText = gtk.CellRendererText()
		column = gtk.TreeViewColumn("# of Tiles", rendererText, text=2)
		column.set_sort_column_id(2)
		treeView.append_column(column)		

PyApp()
gtk.main()
