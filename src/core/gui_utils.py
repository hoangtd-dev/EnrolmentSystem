import tkinter as tk
from tkinter import ttk

def create_input_field(master, label_text, is_focus=False, error_message=None, show=None):
		label = ttk.Label(master, text=label_text)
		label.pack(fill=tk.X, expand=True, ipadx=5, ipady=5)

		entry = ttk.Entry(master, show=show)
		entry.pack(fill=tk.X, expand=True, ipadx=5, ipady=5)
		
		if is_focus:
			entry.focus()

		error_label = None
		if error_message:
			error_label = ttk.Label(master, text=error_message, foreground='red')
			error_label.pack(fill=tk.X, expand=True, ipadx=5, ipady=5)
			error_label.pack_forget()

		return entry, lambda: error_label.pack(fill=tk.X, expand=True, ipadx=5, ipady=5)

def create_custom_table(master, columns, data):
	displayed_column = [column_key for column_key, _ in columns.items()]

	tree = ttk.Treeview(master, columns=displayed_column, show='headings')

	for column_key, displayed_name in columns.items():
		tree.heading(column_key, text=displayed_name)

	for row in data:
		tree.insert('', tk.END, values=row)

	tree.pack(fill=tk.BOTH, expand=True)