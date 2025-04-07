from tkinter import *
from tkinter import filedialog
from tkinter import ttk 
import time

class myClass(object):
    @staticmethod
    def myMethod():
        return "Insert notes here:"

class Application(ttk.Frame):  
    def __init__(self, master):
        super().__init__(master)
        self.grid(padx=15, pady=15)
        self.createWidgets()

    def createWidgets(self):

        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Segoe UI", 10))
        self.style.configure("TButton", font=("Segoe UI", 10))
        self.style.configure("TEntry", font=("Segoe UI", 10))


        self.txtLabel = ttk.Label(self, text="Notes:")
        self.txtLabel.grid(row=0, column=0, sticky=W, pady=(0, 5))

        self.txtBox = Text(self, width=60, height=12, wrap=WORD, font=("Segoe UI", 10))
        self.txtBox.grid(row=1, column=0, columnspan=3, pady=(0, 15))

        self.txtBox.insert("1.0", myClass.myMethod())

    
        self.filenameLabel = ttk.Label(self, text="Filename:")
        self.filenameLabel.grid(row=2, column=0, sticky=W)

        self.filenameEntry = ttk.Entry(self, width=40)
        self.filenameEntry.grid(row=2, column=1, sticky=W, padx=5)

 
        self.saveBtn = ttk.Button(self, text="Save Text", command=self.save_text)
        self.saveBtn.grid(row=3, column=0, pady=10, sticky=W)

       
        self.loadBtn = ttk.Button(self, text="Browse Files", command=self.load_file)
        self.loadBtn.grid(row=3, column=1, pady=10, sticky=W)

      
        self.status = ttk.Label(self, text="", foreground="green")
        self.status.grid(row=4, column=0, columnspan=3, sticky=W)

    def save_text(self):
        user_text = self.txtBox.get("1.0", END).strip()
        filename_input = self.filenameEntry.get().strip()

        if not filename_input:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename_input = f"user_notes_{timestamp}"

        if not filename_input.endswith(".txt"):
            filename_input += ".txt"

        try:
            with open(filename_input, "w") as file:
                file.write(user_text)
            self.status.config(text=f"Saved as {filename_input}", foreground="green")
        except Exception as e:
            self.status.config(text=f"Error: {e}", foreground="red")

    def load_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt")],
            title="Select a text file"
        )

        if file_path:
            try:
                with open(file_path, "r") as file:
                    contents = file.read()
                self.txtBox.delete("1.0", END)
                self.txtBox.insert("1.0", contents)
                self.status.config(text=f"Loaded: {file_path.split('/')[-1]}", foreground="blue")
            except Exception as e:
                self.status.config(text=f"Error loading file: {e}", foreground="red")


root = Tk()
root.title("Ben's Notes")  
root.geometry("700x400")

app = Application(root)
app.mainloop()
