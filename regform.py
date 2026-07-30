import tkinter as tk

root=tk.Tk()
root.title('REG FORM')
root.geometry('600x4001+100+100')

tk.Label(root,text='Registration Form').pack(padx=20,pady=20)

e1=tk.Label(root,text='Name:')
e1.config(fg='blue')
e1.pack(padx=20,pady=20,row=0,col=0)
tk.Entry(root,width='75').pack(row=0,col=1)

tk.Label(root,text='E-mail:').pack(padx=20,pady=20)
tk.Entry(root,width='75').pack()

tk.Label(root,text='Password:').pack(padx=20,pady=20)
tk.Entry(root,width='75',show='*').pack()

tk.Button(root,text="submit").pack(padx=20,pady=20)

tk.mainloop()



