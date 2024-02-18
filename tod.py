import tkinter as tk

def add_task(task):
    task = main_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        main_task.delete(0, tk.END)
    else:
        lable_2.config(text = 'Enter a task')

def remove_task(task):
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        lable_2.config(text = 'Task isn\'t selected.')


win = tk.Tk()
photo = tk.PhotoImage(file='idk.png')
win.iconphoto(False, photo)
win.config(bg= '#C08EFA')
win.title('To-Do App')
win.geometry('500x600+100+200')
win.resizable(True, True)
win.minsize(300, 400)
win.maxsize(700, 800)


main_task = tk.Entry(win, width=40)


lable_1 = tk.Label(win, text='Your To-Do List',
                   bg='#C08EFA',
                   fg='black',
                   font=('Arial',10,'bold'),
                   width=25,
                   height=3,
                   anchor='n',
                   )


lable_2 = tk.Label(win, text = '',
                   fg='cyan'
                   )


btn1 = tk.Button(win, text= 'Add Task',
                 width = 15,
                 command = add_task
                 )


btn2 = tk.Button(win, text = 'Remove Task',
                 width = 15,
                 command = remove_task
                 )


listbox_tasks = tk.Listbox(win, width = 50)


main_task.grid(row=0, column=0, padx=0, pady=0)

btn1.grid(row=0, column=1, padx=5, pady=5)

btn2.grid(row=2, column=0, padx=5, pady=5)

lable_1.grid(row=0, column=0,padx=0, pady=0)

lable_2.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

listbox_tasks.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


win.mainloop()
