from db import DB
import tkinter as tk
from tkinter import ttk

groups = [
    ("MH-11",),
    ("MH-21",)
]

students = [
    ("Bob", 2025, 1),
    ("Rob", 2025, 1),
    ("Ted", 2024, 2),
    ("Mad", 2024, 2)
]

teachers = [
    ("Prof-1",),
    ("Prof-2",)
]

courses = [
    ("Math", 180, 1),
    ("Physics", 160, 1),
    ("Chemistry", 120, 2),
    ("Programming", 140, 2)
]

groups_courses = [
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 1),
    (2, 2)
]

def selectStudents(db, txt):
    txt.delete("1.0", tk.END)
    res = db.selectStudents()
    if not res:
        txt.insert(tk.END, "No students found.\n")
    else:
        for student in res:
            txt.insert(tk.END, f"ID: {student[0]}, Name: {student[1]}, Year: {student[2]}\n")

def selectCourses(db, txt, group):
    txt.delete("1.0", tk.END)
    res = db.selectCourses(group)
    if not res:
        txt.insert(tk.END, "No courses found.\n")
    else:
        for course in res:
            txt.insert(tk.END, f"Course: {course[0]}, Teacher: {course[1]};\n")

def main():
    
    db = DB("db.db")
    
    root = tk.Tk()
    root.title("University")
    root.geometry("700x500+300+100")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=0)
    root.columnconfigure(1, weight=1)
    
    ### FRAME MANAGE ###
    
    frameManage = ttk.LabelFrame(root, text="Manage", width=100)
    btnConnect = ttk.Button(frameManage, text="Connect DB", command=lambda: (db.connect(), txt.insert(tk.END, "Connected to database.\n")))
    btnCreateTables = ttk.Button(frameManage, text="Create Tables", command=lambda: (db.createTables(), txt.insert(tk.END, "Tables created successfully.\n")))
    btnSeedData = ttk.Button(frameManage, text="Seed Data", command=lambda: (db.seedData(groups, students, teachers, courses, groups_courses), txt.insert(tk.END, "Data seeded successfully.\n")))
    btnClearData = ttk.Button(frameManage, text="Clear Data", command=lambda: (db.close(),db.dropDB(), txt.insert(tk.END, "Data cleared successfully.\n")))
    btnSelectStudents = ttk.Button(frameManage, text="Select Students", command=lambda: selectStudents(db, txt))
    btnSelectCourses = ttk.Button(frameManage, text="Select Courses", command=lambda: selectCourses(db, txt, groups[0][0]))
    
    ### FRAME RESULT ###
    
    frameResult = ttk.LabelFrame(root, text="Result")
    txt = tk.Text(frameResult)
    btnClearTxt = ttk.Button(frameResult, text="Clear", command=lambda: txt.delete("1.0", tk.END))
    txt.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    btnClearTxt.pack(padx=5, pady=5)
    
    
    frameManage.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)
    frameResult.grid(column=1, row=0, sticky=tk.NSEW, padx=10, pady=10)
    frameResult.rowconfigure(0, weight=1)
    frameResult.columnconfigure(0, weight=1)
    btnConnect.grid(row=0, column=0, padx=5, pady=5)
    btnCreateTables.grid(row=1, column=0, padx=5, pady=5)
    btnSeedData.grid(row=2, column=0, padx=5, pady=5)
    btnClearData.grid(row=3, column=0, padx=5, pady=5)
    btnSelectStudents.grid(row=4, column=0, padx=5, pady=5)
    btnSelectCourses.grid(row=5, column=0, padx=5, pady=5)
    
    root.mainloop()
    
main()