import tkinter as tk
from tkinter import messagebox


class Form(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.pack()

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.tryLogin)
        self.login_button.pack()

        self.register_button = tk.Button(self, text="Register", command=self.showRegisterForm)
        self.register_button.pack()

        self.accounts = {}  

    def showRegisterForm(self):
        self.register_window = tk.Toplevel(self.master)  
        self.register_window.title("Form Registrasi")
        self.register_window.minsize(400, 200)

        self.register_label = tk.Label(self.register_window, text="Register Akun Baru!")
        self.register_label.pack()

        self.new_username_label = tk.Label(self.register_window, text="Username:")
        self.new_username_label.pack()

        self.new_username_entry = tk.Entry(self.register_window)
        self.new_username_entry.pack()

        self.new_password_label = tk.Label(self.register_window, text="Password:")
        self.new_password_label.pack()

        self.new_password_entry = tk.Entry(self.register_window, show="*")
        self.new_password_entry.pack()

        self.register_confirm_button = tk.Button(
            self.register_window, text="Register", command=self.registerAccount
        )
        self.register_confirm_button.pack()

    def registerAccount(self):
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()

        if new_username in self.accounts:
            messagebox.showerror("Registration Gagal!", "Username sudah terdaftar!")
        elif not new_username or not new_password:
            messagebox.showerror("Register Gagal!", "Masukkan Username dan Password!")
        else:
            self.accounts[new_username] = new_password
            messagebox.showinfo("Register akun berhasil!", "Akun dibuat!")
            self.register_window.destroy() 

    def tryLogin(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.accounts and self.accounts[username] == password:
            messagebox.showinfo("Login Berhasil!", "Halo!")
            self.master.destroy()
        else:
            messagebox.showerror("Login Gagal!", "Data Login invalid!")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Login Form")
    window.minsize(400, 200)
    login_page = Form(window)
    window.mainloop()
