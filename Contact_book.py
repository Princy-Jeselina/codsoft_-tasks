from tkinter import *
from tkinter import messagebox

# Store contacts
contacts = []

# ------------------- Functions -------------------

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone Number are required!")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    messagebox.showinfo("Success", "Contact Added Successfully!")
    clear_fields()
    view_contacts()


def view_contacts():
    listbox.delete(0, END)

    for contact in contacts:
        listbox.insert(END, f"{contact['name']} - {contact['phone']}")


def search_contact():
    keyword = search_entry.get().lower()

    listbox.delete(0, END)

    found = False

    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            listbox.insert(END, f"{contact['name']} - {contact['phone']}")
            found = True

    if not found:
        messagebox.showinfo("Search", "No Contact Found")


def load_selected(event):
    selected = listbox.curselection()

    if selected:
        index = selected[0]
        selected_contact = contacts[index]

        clear_fields()

        name_entry.insert(0, selected_contact["name"])
        phone_entry.insert(0, selected_contact["phone"])
        email_entry.insert(0, selected_contact["email"])
        address_entry.insert(0, selected_contact["address"])


def update_contact():
    selected = listbox.curselection()

    if not selected:
        messagebox.showerror("Error", "Select a contact first!")
        return

    index = selected[0]

    contacts[index] = {
        "name": name_entry.get(),
        "phone": phone_entry.get(),
        "email": email_entry.get(),
        "address": address_entry.get()
    }

    messagebox.showinfo("Success", "Contact Updated!")
    clear_fields()
    view_contacts()


def delete_contact():
    selected = listbox.curselection()

    if not selected:
        messagebox.showerror("Error", "Select a contact first!")
        return

    index = selected[0]

    del contacts[index]

    messagebox.showinfo("Deleted", "Contact Deleted!")

    clear_fields()
    view_contacts()


def clear_fields():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)


# ------------------- GUI -------------------

root = Tk()
root.title("Contact Book")
root.geometry("650x500")
root.configure(bg="lightblue")

Label(root, text="Contact Book", font=("Arial", 18, "bold"),
      bg="lightblue").pack(pady=10)

frame = Frame(root, bg="lightblue")
frame.pack()

Label(frame, text="Name", bg="lightblue").grid(row=0, column=0, padx=5, pady=5)
name_entry = Entry(frame, width=30)
name_entry.grid(row=0, column=1)

Label(frame, text="Phone", bg="lightblue").grid(row=1, column=0)
phone_entry = Entry(frame, width=30)
phone_entry.grid(row=1, column=1)

Label(frame, text="Email", bg="lightblue").grid(row=2, column=0)
email_entry = Entry(frame, width=30)
email_entry.grid(row=2, column=1)

Label(frame, text="Address", bg="lightblue").grid(row=3, column=0)
address_entry = Entry(frame, width=30)
address_entry.grid(row=3, column=1)

Button(frame, text="Add Contact", width=15,
       command=add_contact).grid(row=4, column=0, pady=10)

Button(frame, text="Update Contact", width=15,
       command=update_contact).grid(row=4, column=1)

Button(frame, text="Delete Contact", width=15,
       command=delete_contact).grid(row=5, column=0)

Button(frame, text="View Contacts", width=15,
       command=view_contacts).grid(row=5, column=1)

Label(root, text="Search (Name/Phone)", bg="lightblue").pack()

search_entry = Entry(root, width=35)
search_entry.pack()

Button(root, text="Search", command=search_contact).pack(pady=5)

listbox = Listbox(root, width=60, height=12)
listbox.pack(pady=10)

listbox.bind("<<ListboxSelect>>", load_selected)

root.mainloop()