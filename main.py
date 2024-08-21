import tkinter
from PIL import ImageTk, Image

scores = 0


def update_score():
    global scores
    scores += 1
    scores_text.configure(text=scores)


app = tkinter.Tk()
app.title("My HamsterCombat")
app.geometry("300x400")

welcome_text = tkinter.Label(app, text="Welcome to My Hamster Combat!")
welcome_text.pack()

button = tkinter.Button(app, text="TAP", width=25, height=2, command=update_score)
button.pack()

scores_text = tkinter.Label(app, text=scores)
scores_text.pack()

hamster_image_base = Image.open("hamster.jpg")
hamster_image_resized = hamster_image_base.resize((300, 300))
hamster_image = ImageTk.PhotoImage(hamster_image_resized)
image_label = tkinter.Label(app, image=hamster_image)
image_label.pack()


if __name__ == '__main__':
    app.mainloop()