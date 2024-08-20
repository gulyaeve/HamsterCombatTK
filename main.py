import tkinter

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


if __name__ == '__main__':
    app.mainloop()