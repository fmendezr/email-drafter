import tkinter as tk
from response_generator import get_response

class Gui():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Email Helper")

        # Labels
        self.subject_label = tk.Label(self.root, text="Subject:")
        self.recipient_address_label = tk.Label(self.root, text="How to Address the Recipient:")
        self.sender_name_label = tk.Label(self.root, text="Sender's Name:")
        self.tone_label = tk.Label(self.root, text="Tone of the Email:")
        self.goal_label = tk.Label(self.root, text="Goal:")
        self.background_label = tk.Label(self.root, text="Background Information:")
        self.important_label = tk.Label(self.root, text="Important Points:")
        self.length_label = tk.Label(self.root, text="Approximate Length:")
        self.language_label = tk.Label(self.root, text="Language of response (english):")
    
        # Entry fields
        self.subject_entry = tk.Entry(self.root, width=60)
        self.recipient_address_entry = tk.Entry(self.root, width=60)
        self.sender_name_entry = tk.Entry(self.root, width=60)
        self.tone_entry = tk.Entry(self.root, width=60)
        self.goal_entry = tk.Entry(self.root, width=60)
        self.background_entry = tk.Text(self.root, height=15)
        self.important_entry = tk.Text(self.root, height=15)
        self.length_entry = tk.Entry(self.root, width=60)
        self.language_entry = tk.Entry(self.root, width=60)
        self.draft = tk.Text(self.root, height=6, width=100)
       
        # Button
        self.generate_button = tk.Button(self.root, text="Generate Response", command=self.on_generate)
      
        # Grid layout
        self.subject_label.grid(row=3, column=0, sticky="e")
        self.recipient_address_label.grid(row=4, column=0, sticky="e")
        self.sender_name_label.grid(row=5, column=0, sticky="e")
        self.tone_label.grid(row=6, column=0, sticky="e")
        self.goal_label.grid(row=7, column=0, sticky="e")
        self.background_label.grid(row=8, column=0, sticky="e")
        self.important_label.grid(row=9, column=0, sticky="e")
        self.length_label.grid(row=10, column=0, sticky="e")
        self.language_label.grid(row=11, column=0, sticky="e")

        self.subject_entry.grid(row=3, column=1)
        self.recipient_address_entry.grid(row=4, column=1)
        self.sender_name_entry.grid(row=5, column=1)
        self.tone_entry.grid(row=6, column=1)
        self.goal_entry.grid(row=7, column=1)
        self.background_entry.grid(row=8, column=1)
        self.important_entry.grid(row=9, column=1)
        self.length_entry.grid(row=10, column=1)
        self.language_entry.grid(row=11, column=1)

        self.generate_button.grid(row=12, columnspan=2)

        self.draft.grid(row=13, column=0, columnspan=2)

        # initiate main loop
        self.root.mainloop()

    # execute when button is clicked
    def on_generate(self):
        subject = self.subject_entry.get()
        recipient_address = self.recipient_address_entry.get()
        sender_name = self.sender_name_entry.get()
        tone = self.tone_entry.get()
        goal = self.goal_entry.get()
        background = self.background_entry.get("1.0", tk.END)
        important = self.important_entry.get("1.0", tk.END)
        length = self.length_entry.get()
        language = self.language_entry.get()
        draft_response = get_response(subject, sender_name, recipient_address, tone, goal, background, important, length, language)
        self.show_draft(draft_response)

    # handle inserting the resposne from the model into the text box
    def show_draft(self, draft_response):  
        self.draft.delete("1.0", tk.END)  # Delete existing text
        self.draft.insert(tk.END, draft_response)  # Insert new text
        


gui = Gui()