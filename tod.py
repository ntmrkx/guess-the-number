import tkinter as tk

def add_task():
    task = main_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        main_task.delete(0, tk.END)
    else:
        lable_2.config(text='Enter a task')

def remove_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        lable_2.config(text='Task isn\'t selected.')

win = tk.Tk()
photo = tk.PhotoImage(file='todo.png')
win.iconphoto(False, photo)
win.config(bg='#AFA9A9')
win.title('To-Do App')
win.geometry('500x600+100+200')
win.resizable(True, True)
win.minsize(300, 400)
win.maxsize(700, 800)

main_task = tk.Entry(win, width=40)

lable_1 = tk.Label(win, text='Your To-Do List',
                   bg='#AFA9A9',
                   fg='black',
                   font=('Arial', 10, 'bold'),
                   width=25,
                   height=2,
                   anchor='n',
                   )

lable_2 = tk.Label(win, text='',
                   fg='red',
                   bg='#AFA9A9'
                   )

btn1 = tk.Button(win, text='Add Task',
                 width=15,
                 command=add_task
                 )

btn2 = tk.Button(win, text='Remove Task',
                 width=15,
                 command=remove_task
                 )

listbox_tasks = tk.Listbox(win, width=50)

lable_1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
main_task.grid(row=1, column=0, padx=10, pady=10)
btn1.grid(row=1, column=1, padx=10, pady=10)
listbox_tasks.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
btn2.grid(row=3, column=0, padx=10, pady=10)
lable_2.grid(row=3, column=1, padx=10, pady=10)

win.mainloop()

