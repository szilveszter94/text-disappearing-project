import tkinter as tk

# SET CONSTANTS
COUNT = 1
INIT_TEXT = ""


# SET THE MAIN CLASS
class App(tk.Tk):
    # SET ATTRIBUTES
    def __init__(self):
        super().__init__()
        # CONFIG THE SCREEN
        self.title('The Most Dangerous Writing App')
        self.config(padx=50, pady=30, bg='#F7F7F7')

        # SET THE TITLE LABEL
        self.title_label = tk.Label(text="The Most Dangerous Writing App", font=("Arvo", 22, "bold"),
                                    highlightthickness=1, bg='#F7F7F7')
        self.title_label.grid(column=0, row=0, pady=20)

        # SET THE SUBTITLE LABEL
        self.subtitle_label = tk.Label(text='Don’t stop writing, or all progress will be lost.', highlightthickness=1,
                                       bg='#F7F7F7',
                                       font=("Arvo", 12, "bold"))
        self.subtitle_label.grid(column=0, row=1, pady=20)

        # SET THE TEXT INPUT FIELD
        self.input_text = tk.Text(font=("Arvo", 12, "bold"), height=15, width=68, fg='#212121')
        self.input_text.grid(column=0, row=5)

    # SET THE CLASS METHOD
    def countdown(self, count):
        global INIT_TEXT
        # START THE COUNTER
        self.after(1000, self.countdown, count + 1)
        # AFTER 6 sec, and after every 2 sec, compare the init text vs input text
        if count > 4 and count % 2 == 0:
            text = self.input_text.get("1.0", "end-1c")
            # if the length of the input text is equal or less than init text, change text color
            if len(text) <= len(INIT_TEXT):
                self.input_text.config(fg='#9D9D9D')
        # every 4 sec compare the init text vs input text
        if count % 4 == 0:
            text = self.input_text.get("1.0", "end-1c")
            # if the length of the input text is greater than input text, change text color
            if len(text) > len(INIT_TEXT):
                INIT_TEXT = text
                self.input_text.config(fg='#212121')
            # if the length of the input text is less than input text, change text color
            else:
                INIT_TEXT = ""
                self.input_text.delete('1.0', "end")
                self.input_text.config(fg='#212121')


# start the app
if __name__ == "__main__":
    app = App()
    app.countdown(COUNT)
    app.mainloop()
