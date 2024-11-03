import tkinter.messagebox as msg
import random
import re
from tkinter import *

class PasswordGenerator(Tk):

    def __init__(self):
        super().__init__()
        # Centering the window when opened.
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        app_width = 500
        app_height = 350
        set_x = int((screen_width / 2) - (app_width / 2))
        set_y = int((screen_height / 2) - (app_height / 2))
        self.geometry(f'{app_width}x{app_height}+{set_x}+{set_y}')
        self.title("Cod's Password Generator")
        self.config(bg="#f0f4f8")
        self.resizable(False, False)

        # Application design
        self.app_heading_frame = self.create_app_heading_frame()
        self.create_heading_label()
        self.length_input_frame = self.create_length_input_frame()
        self.create_password_length_label()
        self.password_length_entry = self.create_password_length_entry()
        self.strength_input_frame = self.create_strength_input_frame()
        self.create_password_strength_label()
        self.choice = StringVar()
        self.choice.set("high")
        self.create_strength_radio_options()
        self.button_frame = self.create_button_frame()
        self.create_generate_button()
        self.create_footer_label()

    def create_app_heading_frame(self):
        frame = Frame(self, height=50, bg="#4a90e2")
        frame.pack(fill=X)
        return frame

    def create_heading_label(self):
        label = Label(self.app_heading_frame, text="Password Generator", font=("Helvetica", 23, "bold"), fg="#ffffff", bg="#4a90e2")
        label.pack()

    def create_length_input_frame(self):
        frame = Frame(self, bg="#e5e7ea", height=300, padx=20, pady=20)
        frame.pack(fill=BOTH)
        return frame

    def create_password_length_label(self):
        label = Label(self.length_input_frame, text="Set password length", font=("Helvetica", 16), bg="#e5e7ea", fg="#1a0944")
        label.pack(side=LEFT, padx=(0, 10))

    def create_password_length_entry(self):
        entry = Entry(self.length_input_frame, width=3, fg="#1e4976", font=("Helvetica", 13))
        entry.pack(side=LEFT, ipady=2, ipadx=2)
        return entry

    def create_strength_input_frame(self):
        frame = Frame(self, bg="#e5e7ea", height=300, padx=20, pady=20)
        frame.pack(fill=BOTH)
        return frame

    def create_password_strength_label(self):
        label = Label(self.strength_input_frame, text="Set password strength", font=("Helvetica", 16), bg="#e5e7ea", fg="#1a0944")
        label.pack(anchor=W)

    def create_strength_radio_options(self):
        option1 = Radiobutton(self.strength_input_frame, text="low", value="low", variable=self.choice, font=("Helvetica", 13), bg="#e5e7ea")
        option2 = Radiobutton(self.strength_input_frame, text="medium", value="medium", variable=self.choice, font=("Helvetica", 13), bg="#e5e7ea")
        option3 = Radiobutton(self.strength_input_frame, text="high", value="high", variable=self.choice, font=("Helvetica", 13), bg="#e5e7ea")
        option1.pack(side=LEFT, padx=(50, 0))
        option2.pack(side=LEFT, padx=(50, 0))
        option3.pack(side=LEFT, padx=(50, 0))

    def create_button_frame(self):
        frame = Frame(self, bg="#e5e7ea", height=100, padx=20, pady=20)
        frame.pack(fill=BOTH)
        return frame

    def create_generate_button(self):
        button = Button(self.button_frame, text="GENERATE", bg="#4caf50", fg="#ffffff", borderwidth=0, cursor="hand2", padx=20, pady=5, command=lambda: self.collect_password(self.password_length_entry.get(), self.choice.get()))
        button.pack()

    def show_generate_password_window(self, length, strength, password):
        show_generated_password_popup_window = Toplevel(self)
        show_generated_password_popup_window.geometry("700x250")
        show_generated_password_popup_window.resizable(False, False)
        show_generated_password_popup_window.title(f"Your Generated Password")
        show_generated_password_popup_window.config(bg="#f0f4f8")
        
        label = Label(show_generated_password_popup_window, text=f"GENERATED PASSWORD\nLENGTH: {length}\tSTRENGTH: {strength}", fg="#1d3b64", font=("Helvetica", 16), bg="#f0f4f8")
        label.pack(pady=10)
        
        pass_view = Text(show_generated_password_popup_window, height=3, width=70, fg="#1d3b64", bg="#e5e7ea", font=("Helvetica", 13))
        pass_view.insert(END, password)
        pass_view.config(state=DISABLED)
        pass_view.pack(pady=5)

        btn_close = Button(show_generated_password_popup_window, text="Close", width=13, bd=0, bg="#3c8bdf", fg="#ffffff", font=("Helvetica", 13, "bold"), command=show_generated_password_popup_window.destroy)
        btn_close.pack(side=RIGHT, padx=(0, 20))

    def create_footer_label(self):
        footer_label = Label(self, text="Made by Onkar", font=("Helvetica", 12), fg="#1a0944", bg="#f0f4f8")
        footer_label.pack(side=BOTTOM, pady=10)

    def generate_low_security_password(self, length):
        low_pass_char = list()
        for c in range(65, 91):
            low_pass_char.append(chr(c))
        for s in range(97, 123):
            low_pass_char.append(chr(s))
        return ''.join(random.choice(low_pass_char) for _ in range(length))

    def generate_medium_security_password(self, length):
        med_pass_char = list()
        for c in range(65, 91):
            med_pass_char.append(chr(c))
        for n in range(48, 58):
            med_pass_char.append(chr(n))
        for s in range(97, 123):
            med_pass_char.append(chr(s))

        p = ''.join(random.choice(med_pass_char) for _ in range(length))
        if not re.search('[0-9]', p):
            return self.generate_medium_security_password(length)
        return p

    def generate_high_security_password(self, length):
        high_pass_char = list()
        sp_chr = ['!', '@', '#', '$', '%', '^', '&', '*']
        for c in range(65, 91):
            high_pass_char.append(chr(c))
        for n in range(48, 58):
            high_pass_char.append(str(n))
        for sp in sp_chr:
            high_pass_char.append(sp)
        for s in range(97, 123):
            high_pass_char.append(chr(s))

        p = ''.join(random.choice(high_pass_char) for _ in range(length))
        if not re.search('[!@#$%^&*]', p) or not re.search('[0-9]', p):
            return self.generate_high_security_password(length)
        return p

    def collect_password(self, length, strength):
        try:
            length = int(length)
            if length > 80 or length < 4:
                msg.showwarning(title="WARNING", message="Password length must be less than 81 and greater than 3")
            else:
                if strength == "low":
                    password = self.generate_low_security_password(length)
                elif strength == "medium":
                    password = self.generate_medium_security_password(length)
                elif strength == "high":
                    password = self.generate_high_security_password(length)
                self.show_generate_password_window(length, strength, password)
        except ValueError:
            msg.showwarning(title="WARNING", message="Invalid password length\n(minimum 4 | maximum 80)")

    def run(self):
        self.mainloop()

if __name__ == '__main__':
    app = PasswordGenerator()
    app.run()
