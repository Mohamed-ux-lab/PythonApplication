from tkinter import *
import webbrowser


def youtube_link():
    webbrowser.open_new("https://youtube.com/gravenilvectuto")


# creation de l'interface
root = Tk()

# personalisation de l'interface
root.title("My application")
root.geometry("720x480")
root.minsize(480, 320)
root.configure(background="#1e1f22")

# creation du frame
box = Frame(root, bg="#1e1f22")

# creation de label
label_title = Label(box, text="Bienvenue cher Abonner", font=("Roboto", 30), bg="#1e1f22", fg="#fff")
label_title.pack(expand=TRUE)

label_subtitle = Label(box, text="Bienvenue cher Abonner", font=("Roboto", 15), bg="#1e1f22", fg="#fff")
label_subtitle.pack(expand=TRUE)

# ajout de button
yt_button = Button(box, text="Chaine Youtube", font=("Courrier", 15), bg="#fff", fg="#111", command=youtube_link)
yt_button.pack()

# ajout du frame
box.pack(expand=TRUE)

# afficker l'interface
root.mainloop()
