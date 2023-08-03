import tkinter as tk
from tkinter import messagebox
import requests

root = tk.Tk()
root.title("Website Status Checker")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg='white')
dark_theme= False
def check_website_status():
    url = url_entry.get()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            messagebox.showinfo("Website Status", f"The website {url} is running.")
        else:
            messagebox.showwarning("Website Status", f"The website {url} returned a status code: {response.status_code}")
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Error accessing the website {url}: {e}")
def toggle_theme():
    global dark_theme
    if dark_theme:
        root.configure(bg='white')
    else:
        root.configure(bg='black')
    dark_theme = not dark_theme

label = tk.Label(root, text="Enter website URL:")
label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

check_button = tk.Button(root, text="Check Status", command=check_website_status)
check_button.pack()

bt2 = tk.Button(root, text= "Dark Mode", command=toggle_theme)
bt2.pack()

root.mainloop()
