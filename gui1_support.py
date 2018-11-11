#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Nov 11, 2018 03:57:06 PM CET  platform: Windows NT

import sys
import gui1

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global wrn
    wrn = tk.StringVar()

def ananas():
    print('gui1_support.ananas')
    sys.stdout.flush()
    input=w.Entry2.get()
    w.Scrolledtext3.insert('insert', "mytext"+ input)


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import gui1.py
    gui1.py.vp_start_gui()



