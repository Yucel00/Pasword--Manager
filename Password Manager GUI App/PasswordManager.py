from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    password=password.join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)#olusturdugumuz passwordu otomatik kopyalamamiizi sagliyo
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=username_entry.get()
    password=password_entry.get()
    if len(website)==0:
        messagebox.showinfo(message=f"Please Enter Website Name")
        website_entry.focus()
    elif len(email)==0:
        messagebox.showinfo(message=f"Please Enter Email/Username Name")
        username_entry.focus()

    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entred:\nEmail:{email}\nPassword:{password}\n Is it ok to save?")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0,END) #fonksiyon calistiktan sonra icini silicek
                username_entry.delete(0,END)
                password_entry.delete(0,END)
                website_entry.focus()
                messagebox.showinfo(message="Saved")

        else:
            messagebox.showinfo(message="Canceled")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=300, height=300 ,highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=lock_image)
canvas.grid(column=1,row=0)

# labels
website=Label(text="Website:")
website.grid(row=1,column=0)
username=Label(text="Email/Username:")
username.grid(row=2,column=0)
password=Label(text="Password:")
password.grid(row=3,column=0)

#entries
website_entry=Entry(width=30)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
username_entry=Entry(width=30)
username_entry.grid(row=2,column=1,columnspan=2)
password_entry=Entry(width=30)
password_entry.grid(row=3,column=1,columnspan=2)

# buttons
generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=4,column=2)
add_button=Button(text="Add",width=15,command=save)
add_button.grid(row=5,column=2)
window.mainloop()
