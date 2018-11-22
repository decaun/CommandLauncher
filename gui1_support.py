#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Nov 11, 2018 03:57:06 PM CET  platform: Windows NT

import sys
import gui1
import subprocess
import threading, time
import psutil,time
import base64
global block,checking_system,input2parsed,iterations,run_block,thread_limit

MEMORY_LIMIT_PERCENT=50
CPU_LIMIT_PERCENT=30
block=False
run_block=False
thread_limit=50

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


def ananas():
    global CREATE_NO_WINDOW,block,input2parsed,run_block,querry,user,passw,CHECK_PER
    CREATE_NO_WINDOW = 0x08000000
    CHECK_PER=10
    if not run_block:
        querry=w.Scrolledtext2.get(0.0,"end").replace('\n', ';')
        user=w.Entry1.get()
        passw=w.Entry2.get().encode('base64')
        input2=w.Scrolledtext1.get(0.0,"end").encode("ascii")
        if len(input2)>1 and len(passw)>0 and len(user)>0 and len(querry)>1:
            run_block=True
            w.Scrolledtext3.delete(1.0,"end")
            w.Button1.configure(text="Running...")
            input2parsed=input2.splitlines()
            threading.Thread(target=check_system).start()
            threading.Thread(target=launcher).start()

        

def launcher():
    global input2parsed,iterations,CHECK_PER,block,thread_limit
    iterations=0
    for line in input2parsed:
        if len(line)>0:
            if block or threading.activeCount()>thread_limit:
                while threading.activeCount()>6:
                    time.sleep(1)
            thread = threading.Thread(target=procedure,args=(line.splitlines()))
            thread.start()
        else:
            pass
        iterations+=1



def procedure(dest):
    global iterations,input2parsed,run_block,querry,user,passw
    try:
        output2 = subprocess.check_output("sqlcmd -S "+dest+" -U "+user+" -P "+passw.decode('base64')+" -Q "+'"'+querry+'"&&exit', shell=True, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, creationflags=CREATE_NO_WINDOW).decode("utf-8")
        w.Scrolledtext3.insert("end",'\n'+"++++++++++++++++++++++++++++++++++++++++"+'\n'+"--------------------"+"Output from: "+dest+'\n'+output2)
        w.Scrolledtext3.see("end")
    except subprocess.CalledProcessError as e:
        w.Scrolledtext3.insert("end",'\n'+"++++++++++++++++++++++++++++++++++++++++"+'\n'+"--------------------"+"Output from: "+dest+ " (ERROR!)"+'\n'+e.output)
        w.Scrolledtext3.see("end")
    if iterations>=len(input2parsed):
        w.Button1.configure(text='''GO''')
        run_block=False
    else:
        run_block=True



def check_system():
    global run_block,block,thread_limit
    while run_block:
        current_cpu=psutil.cpu_percent(interval=0.2, percpu=False)
        if psutil.virtual_memory().percent<MEMORY_LIMIT_PERCENT and current_cpu<CPU_LIMIT_PERCENT and threading.activeCount()<thread_limit:
            block=False
            if thread_limit<25:
                thread_limit=thread_limit+abs((current_cpu-CPU_LIMIT_PERCENT))
        else:
            block=True
            thread_limit=thread_limit-abs((current_cpu-CPU_LIMIT_PERCENT))



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




