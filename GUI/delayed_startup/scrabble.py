#!/usr/bin/python3

from gi.repository import Gtk, GObject, GLib, GdkPixbuf, Pango, Gdk
from findwords import *

class PyApp(Gtk.Window):
	def __init__(self):
		super(PyApp, self).__init__()
		
		tiles = "..."
		self.set_title("Anagram Creator")
		self.set_size_request(510, 500)
		self.set_position(1)
		
		vbox = Gtk.VBox(False, 3)

		self.label = Gtk.Label("Letters in hand: " + tiles)
		vbox.pack_start(self.label, False, False, 10)
		
#		hbox2 = Gtk.HBox(True, 2)
#		words7_label = Gtk.Label("Words using 7 letters:")
#		hbox2.add(words7_label)
#		vbox.add(hbox2)
		
		hbox_words = Gtk.HBox(True, 1)
		
		vbox1 = Gtk.VBox(False, 2)
		only_label = Gtk.Label("Using only letters given: ")
		vbox1.pack_start(only_label, False, False, 5)
		self.words = Gtk.ListStore(str, int, int)
		self.treeView = Gtk.TreeView(self.words)
		self.treeView.set_rules_hint(True)
		self.create_columns(self.treeView)
		scrolled1 = Gtk.ScrolledWindow()
		scrolled1.add(self.treeView)
		vbox1.pack_start(scrolled1, True, True, 10)
		hbox_words.pack_start(vbox1, True, True, 10)
		
		vbox2 = Gtk.VBox(False, 2)
		extra_label = Gtk.Label("Using 1 extra letter: ")
		vbox2.pack_start(extra_label, False, False, 5)
		self.words_extra = Gtk.ListStore(str, int, int)
		self.extras = Gtk.TreeView(self.words_extra)
		self.extras.set_rules_hint(True)
		self.create_columns(self.extras)
		scrolled2 = Gtk.ScrolledWindow()
		scrolled2.add(self.extras)
		vbox2.pack_start(scrolled2, True, True, 10)
		hbox_words.pack_start(vbox2, True, True, 10)
		
		vbox.pack_start(hbox_words, True, True, 10)
		
		hbox7 = Gtk.HBox(False, 2)
		entry = Gtk.Entry()
		entry.add_events(2048)
		hbox7.pack_start(entry, True, True, 10)
		btn1 = Gtk.Button("Find Words")
		hbox7.pack_start(btn1, False, False, 10)
		
		vbox.pack_start(hbox7, False, False, 10)
		
#		vbox.set_child_packing(hbox_words, 
		
		entry.grab_focus()
		entry.connect("activate", self.tiles_entered, entry)
		btn1.connect("clicked", self.tiles_entered, entry)
		
		self.connect("destroy", Gtk.main_quit)
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
		rendererText = Gtk.CellRendererText()
		column = Gtk.TreeViewColumn("Word", rendererText, text=0)
		column.set_sort_column_id(0)
		treeView.append_column(column)
		
		rendererText = Gtk.CellRendererText()
		column = Gtk.TreeViewColumn("Points", rendererText, text=1)
		column.set_sort_column_id(1)
		treeView.append_column(column)

		rendererText = Gtk.CellRendererText()
		column = Gtk.TreeViewColumn("# of Tiles", rendererText, text=2)
		column.set_sort_column_id(2)
		treeView.append_column(column)		

PyApp()
Gtk.main()
