import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.geometry("500x350")

def opt1():
    print("Option 1")

def opt2():
    print("Option 2")

def opt3():
    print("Option 3")

def opt4():
    print("Option 4")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="NOR Scorer\nPlease choose an option", font=("Segoe UI", 24))
label.pack(pady=12, padx=10)

# entry1= customtkinter.CTkEntry(master=frame, placeholder_text="Username")
# entry1.pack(pady=12, padx=10)

# entry2= customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
# entry2.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame, text="Score an animal", command=opt1)
button1.pack(pady=6, padx=10)

button2 = customtkinter.CTkButton(master=frame, text="Show last scores", command=opt2)
button2.pack(pady=6, padx=10)

button3 = customtkinter.CTkButton(master=frame, text="Export as .csv", command=opt3)
button3.pack(pady=6, padx=10)

button4 = customtkinter.CTkButton(master=frame, text="Exit program", command=opt4, border_width=2, border_color="red")
button4.pack(pady=48, padx=10)

# checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
# checkbox.pack(pady=12, padx=10)

root.mainloop()