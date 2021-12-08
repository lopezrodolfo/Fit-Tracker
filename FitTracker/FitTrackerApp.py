import tkinter as tk
from tkinter import messagebox
import Account

class ProgressScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Label = tk.Label(self, text="MyProgress", bg = "orange", font=("Arial Bold", 25))
        Label.place(x=40, y=150)
        
        my_tracker_button = tk.Button(self, text="LogData", font=("Arial", 15), command=lambda: controller.show_frame(LogDataScreen))
        my_tracker_button.place(x=400, y=450)
        
class AccountScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        account_label_frame = tk.LabelFrame(self, text='Account', bg='ivory', bd = 10, font=("Arial", 20))
        account_label_frame.pack(fill="both", expand="yes", padx = 50, pady=50)
        # account_label_frame.pack(fill="both", expand="yes")
        
        first_name_label = tk.Label(account_label_frame, text="First Name", font=("Arial Bold", 15), bg='ivory')
        first_name_label.place(x=50, y=20)

        first_name_entry = tk.Entry(account_label_frame, width = 30, bd = 5)
        # first_name_entry.insert(0, userAccount.getFirstName())
        first_name_entry.place(x=180, y=20)
        
        last_name_label = tk.Label(account_label_frame, text="Last Name", font=("Arial Bold", 15), bg='ivory')
        last_name_label.place(x=50, y=60)

        last_name_entry = tk.Entry(account_label_frame, width = 30, bd = 5)
        # last_name_entry.insert(0, userAccount.getLastName())
        last_name_entry.place(x=180, y=60)

        gender_label = tk.Label(account_label_frame, text="Gender", font=("Arial Bold", 15), bg='ivory')
        gender_label.place(x=50, y=100)

        gender_entry = tk.Entry(account_label_frame, width = 30, bd = 5)
        # gender_entry.insert(0, userAccount.getGender())
        gender_entry.place(x=180, y=100)

        height_label = tk.Label(account_label_frame, text="Height", font=("Arial Bold", 15), bg='ivory')
        height_label.place(x=50, y=140)

        height_entry = tk.Entry(account_label_frame, width = 30, bd = 5)
        # height_entry.insert(0, userAccount.getHeight())
        height_entry.place(x=180, y=140)

        weight_label = tk.Label(account_label_frame, text="Weight", font=("Arial Bold", 15), bg='ivory')
        weight_label.place(x=50, y=180)

        weight_entry = tk.Entry(account_label_frame, width = 30, bd = 5)
        # weight_entry.insert(0, userAccount.getWeight())
        weight_entry.place(x=180, y=180)

        age_label = tk.Label(account_label_frame, text="Age", font=("Arial Bold", 15), bg='ivory')
        age_label.place(x=50, y=220)

        age_entry = tk.Entry(account_label_frame, width = 30, bd = 5)
        # age_entry.insert(0, userAccount.getAge())
        age_entry.place(x=180, y=220)

        def ModifyAccount():
            if first_name_entry.get() != "" and last_name_entry.get() != "" and gender_entry.get() != "" and height_entry.get() != "" and weight_entry.get() != "" and age_entry.get() != "":       
                userAccount = Account.Account(first_name_entry.get(), last_name_entry.get(), gender_entry.get(), height_entry.get(), weight_entry.get(), age_entry.get())

                with open("personal_info.txt", "w") as f:
                    f.write(str(userAccount.calorie_budget))

        submit_button = tk.Button(account_label_frame, text="Submit", font=("Arial", 15), command=ModifyAccount)
        submit_button.place(x=320, y=300)
        
        my_tracker_button = tk.Button(self, text="LogData", font=("Arial", 15), command=lambda: controller.show_frame(LogDataScreen))
        my_tracker_button.place(x=400, y=450)

class LogDataScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Label = tk.Label(self, text="LogData", bg = "orange", font=("Arial Bold", 25))
        Label.place(x=40, y=150)
        
        my_account_button = tk.Button(self, text="MyAccount", font=("Arial", 15), command=lambda: controller.show_frame(AccountScreen))
        my_account_button.place(x=650, y=450)

        my_progress_button = tk.Button(self, text="MyProgress", font=("Arial", 15), command=lambda: controller.show_frame(ProgressScreen))
        my_progress_button.place(x=400, y=450)
        
        home_button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(StartScreen))
        home_button.place(x=100, y=450)

class StartScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        login_label_frame = tk.LabelFrame(self, text='Login', bg='ivory', bd = 10, font=("Arial", 20))
        login_label_frame.pack(fill="both", expand="yes", padx = 150, pady=150)
        
        username_label = tk.Label(login_label_frame, text="Username", font=("Arial Bold", 15), bg='ivory')
        username_label.place(x=50, y=20)
        username_entry = tk.Entry(login_label_frame, width = 30, bd = 5)
        username_entry.place(x=180, y=20)
        
        password_label = tk.Label(login_label_frame, text="Password", font=("Arial Bold", 15), bg='ivory')
        password_label.place(x=50, y=80)
        password_entry = tk.Entry(login_label_frame, width = 30, show='*', bd = 5)
        password_entry.place(x=180, y=80)
        
        def verify():
            try:
                with open("credential.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        u, p = e.split(",")
                        if u.strip() == username_entry.get() and p.strip() == password_entry.get():
                            controller.show_frame(LogDataScreen)
                            i = 1
                            break
                    if i==0:
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")
         
        submit_button = tk.Button(login_label_frame, text="Submit", font=("Arial", 15), command=verify)
        submit_button.place(x=320, y=115)
        
        def register():
            root = tk.Tk()
            root.resizable(0,0)
            root.configure(bg="deep sky blue")
            root.title("Register")
            username_label = tk.Label(root, text="Username:", font=("Arial",15), bg="deep sky blue")
            username_label.place(x=10, y=10)
            username_entry = tk.Entry(root, width=30, bd=5)
            username_entry.place(x = 200, y=10)
            
            password_label = tk.Label(root, text="Password:", font=("Arial",15), bg="deep sky blue")
            password_label.place(x=10, y=60)
            password_entry = tk.Entry(root, width=30, show="*", bd=5)
            password_entry.place(x = 200, y=60)
            
            confirm_password_label = tk.Label(root, text="Confirm Password:", font=("Arial",15), bg="deep sky blue")
            confirm_password_label.place(x=10, y=110)
            confirm_password_entry = tk.Entry(root, width=30, show="*", bd=5)
            confirm_password_entry.place(x = 200, y=110)
            
            def check():
                if username_entry.get()!="" or password_entry.get()!="" or confirm_password_entry.get()!="":
                    if password_entry.get()==confirm_password_entry.get():
                        not_val = False
                        with open("credential.txt", "r") as f:
                            info = f.readlines()
                            i  = 0
                            for e in info:
                                u, p = e.split(",")
                                if u.strip() == username_entry.get():
                                    not_val = True
                                    break
                        if not_val:
                            messagebox.showinfo("Error", "Username already exists. Try another")
                        else:
                            with open("credential.txt", "a") as f:
                                f.write(username_entry.get()+","+password_entry.get()+"\n")
                                messagebox.showinfo("Welcome","You are registered successfully!!")
                    else:
                        messagebox.showinfo("Error","Your password didn't get match!!")

                        
                else:
                    messagebox.showinfo("Error", "Please fill the complete field!!")
                    
            submit_button = tk.Button(root, text="Sign in", font=("Arial",15), bg="#ffc22a", command=check)
            submit_button.place(x=170, y=150)
            
            root.geometry("500x200")
            root.mainloop()
            
        register_button = tk.Button(self, text="Register", bg = "dark orange", font=("Arial",15), command=register)
        register_button.place(x=650, y=80)
       
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        # create root window
        tk.Tk.__init__(self, *args, **kwargs)
        
        # creating base frame
        root_frame = tk.Frame(self)
        root_frame.pack()
        
        root_frame.grid_rowconfigure(0, minsize = 500)
        root_frame.grid_columnconfigure(0, minsize = 800)
        
        # creating layered frames to act as dif screens
        self.frames = {}
        for F in (StartScreen, LogDataScreen, AccountScreen, ProgressScreen):
            frame = F(root_frame, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
        
        # initially show start screen (StartScreen frame is top frame)
        self.show_frame(StartScreen)
    
    def maxSize(self):
        self.maxsize(800,500)
    
    def run(self):
        self.mainloop()
        
    def show_frame(self, screen):
        frame = self.frames[screen]
        frame.tkraise()
        self.title("FitTracker")
        
if __name__ == "__main__":
    app = App()
    app.maxSize()
    app.run()