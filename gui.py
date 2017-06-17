import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import core

win = tk.Tk()
win.title("RegCMU AddBot")


####---Step 1 #####
def login():
    if semester.get().__len__() == 3 :
        core.openLogin(semester.get())

tabControl = ttk.Notebook(win)
tabEnroll = ttk.Frame(tabControl)
tabChangeOrder = ttk.Frame(tabControl)
tabControl.add(tabEnroll, text='Enroll')
tabControl.add(tabChangeOrder, text='CourseOrder')
tabControl.pack(expand=1, fill='both')

frameStep1 = ttk.LabelFrame(tabEnroll, text=' Step 1 ')
frameStep1.grid(column=0, row=0)

ttk.Label(frameStep1, text="Current semester").grid(column=0, row=0)
semester = tk.StringVar()
semesterBox = ttk.Entry(frameStep1, width=12, textvariable=semester)
semesterBox.grid(column=1, row=0)
semesterBox.focus()

ttk.Button(frameStep1, text="Login", command=login).grid(column=3, row=0)

####  end step 1 ####
#### step 2 #####
allCourse = []

courseCount = 0


def clearList():
    if len(allCourse) != 0:
        allCourse.pop()
        updateShowList()


def updateShowList():
    showCourse.configure(state='normal')
    showCourse.delete(1.0, tk.END)
    for course in allCourse:
        txt = course['id'] + "\t" + course['lec'] + "\t" + course['lab'] + "\n"
        showCourse.insert(tk.INSERT, txt)
    showCourse.configure(state='disabled')


def addCourse():
    if courseID.get() != '' and lecSec.get() != '' and labSec.get() != '':
        course = {'id': courseID.get(),
                  'lec': lecSec.get(),
                  'lab': labSec.get()}
        allCourse.append(course)
        updateShowList()


def run():
    core.addCourse(allCourse, semester.get())


frameStep2 = ttk.LabelFrame(tabEnroll, text=' Step 2 ')
frameStep2.grid(column=0, row=1)

# ---------------addCourse part
addFrame = ttk.LabelFrame(frameStep2, text=' Add Course to list ')
addFrame.grid(column=0, row=0)

ttk.Label(addFrame, text='CourseID ').grid(column=0, row=0)
courseID = tk.StringVar()
ttk.Entry(addFrame, width=8, textvariable=courseID).grid(column=1, row=0)

ttk.Label(addFrame, text='Lec ').grid(column=2, row=0)
lecSec = tk.StringVar()
ttk.Entry(addFrame, width=5, textvariable=lecSec).grid(column=3, row=0)

ttk.Label(addFrame, text='Lab ').grid(column=4, row=0)
labSec = tk.StringVar()
ttk.Entry(addFrame, width=5, textvariable=labSec).grid(column=5, row=0)

ttk.Button(addFrame, text="Add", command=addCourse).grid(column=7, row=0)

# ---------------------end addCourse

# ---course added
addedFrame = ttk.LabelFrame(frameStep2, text=' List ')
addedFrame.grid(column=0, row=1)

courseList = [ttk.Label(addedFrame, text="CID\tLEC\tLAB").grid(column=0, row=0)]
showCourse = scrolledtext.ScrolledText(addedFrame, width=20, height=10, wrap=tk.WORD)
showCourse.grid(column=0, row=1)
showCourse.configure(state='disabled')
ttk.Button(addedFrame, text="RUN!", command=run).grid(column=0, row=2)

ttk.Button(addedFrame, text="CLEAR", command=clearList).grid(column=1, row=2)

win.mainloop()
