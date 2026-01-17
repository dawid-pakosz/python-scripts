import customtkinter as ctk

def add_item():
    item_text = entry.get()
    item_label = ctk.CTkLabel(scrollable_frame, text=item_text)
    item_label.pack()
    entry.delete(0,ctk.END)

root = ctk.CTk()
root.geometry("500x400")
root.title("Custom Tkinter Example App")

title_label = ctk.CTkLabel(root, text="Welcome to my App", font=ctk.CTkFont(size=20, weight="bold"))
title_label.pack(padx=10, pady=(20,10))

#frame with scrollable content
scrollable_frame = ctk.CTkScrollableFrame(root, width=200, height=100)
scrollable_frame.pack()

#entry field
entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add new item...")
entry.pack(fill="x")

#button to add items
add_button = ctk.CTkButton(root, text="Add Item", command=add_item)
add_button.pack( pady=10)   

root.mainloop()
