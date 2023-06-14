import customtkinter as ctk

#Note: can use pack, grid, or place to implement widgets

def add_run():
    run = entry.get() #retrieves text from the entry field
    label = ctk.CTkLabel(scrollable_frame, text=run)
    label.pack()
    entry.delete(0, ctk.END) #removes text from entry field


#-----------Overall Appearence--------------
ctk.set_appearance_mode("Dark")
root = ctk.CTk() #main widget (box that contains every other widget)
root.geometry("750x450") #window size, has to be called before mainloop
root.title("StarRez Delete Automation")


#-------------Widget Information-------------

#Title
title_label = ctk.CTkLabel(root, text="Enter Item Information", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=10)

#------Scrollable Frame---------
scrollable_frame = ctk.CTkScrollableFrame(root, width=550, height=250)
scrollable_frame.pack()

#Titles And Entry Fields
label = ctk.CTkLabel(scrollable_frame, text="Item Name", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(anchor="w")
entry = ctk.CTkEntry(scrollable_frame)
entry.pack(fill="x")

label = ctk.CTkLabel(scrollable_frame, text="Number of Items to Remove", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(pady=(15, 0), anchor="w")
entry = ctk.CTkEntry(scrollable_frame)
entry.pack(fill="x")

#Radio Settings
# deleted = 1
# notDeletableHidden = 2
# notDeletableView = 3
# notDeletableViewModify = 4
#Radio Buttons
label = ctk.CTkLabel(scrollable_frame, text="Edit Item to:", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(pady=(15, 0), anchor="w")

selection = ctk.StringVar() #need this to link all radiobuttons together
radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Deleted", value=1, font=ctk.CTkFont(size=15), variable=selection)
radiobutton.pack(pady=10, anchor="w")

radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Not Deletable Hidden", value=2, font=ctk.CTkFont(size=15), variable=selection)
radiobutton.pack(pady=(0, 10), anchor="w")

radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Not Deletable View", value=3, font=ctk.CTkFont(size=15), variable=selection)
radiobutton.pack(pady=(0, 10), anchor="w")

radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Not Deletable View Modify", value=4, font=ctk.CTkFont(size=15), variable=selection)
radiobutton.pack(pady=(0, 10), anchor="w")

#--------Run Action Button----------
#when "add_button is clicked, the add_run function is run."
add_button = ctk.CTkButton(root, text="Run", width=300, font=ctk.CTkFont(size=15, weight="bold"), command=add_run) 
add_button.pack(pady=20)


#------Start Application-------
root.mainloop() #constantly running so long as the interface is running

