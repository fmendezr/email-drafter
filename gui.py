import tkinter as tk

'''
 Hey chat gpt I need u to devlop a gui using tkinter. the window should be titled Email Helper. add seperate input fields and labels
 for the following things (initiated by -):
 - users email address 
 - the password to that 
 - the email address of the recipient 
 - the subject of the email
 - how to address the recipient 
 - what name should  sign the email 
 - tone of the email
 - goal (request, inform, send documents, etc)
 - background information if necessary   
 - important things that should be included in the email
 - approximate length (words)
 Additionally there should be a button with the text content "generate response" that when clicked calls a function called 
 generate_message with the contents of each of the inputs fields as seperate input parameters. 
 You should style everything approapiatley for it to look profesional, sleek, and elegant.   
'''

'''
 Chatgpt I need u to compose an email with addressing  {recipient},it shuold be signed by {user}.
 Follow the guidlines inside the parethensis for instructions on how to write this email.
    (
        subject: {subject}
        tone: {tone}
        goal: {goal}:  
        background information: {background_info}
        important things that must be included: {import_info}
        approximate length of body: {length}
    )   
'''
class Gui():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Email Helper")

        # Labels
        self.email_label = tk.Label(self.root, text="User's Email Address:")
        self.password_label = tk.Label(self.root, text="Password:")
        self.recipient_email_label = tk.Label(self.root, text="Recipient's Email Address:")
        self.subject_label = tk.Label(self.root, text="Subject:")
        self.recipient_address_label = tk.Label(self.root, text="How to Address the Recipient:")
        self.sender_name_label = tk.Label(self.root, text="Sender's Name:")
        self.tone_label = tk.Label(self.root, text="Tone of the Email:")
        self.goal_label = tk.Label(self.root, text="Goal:")
        self.background_label = tk.Label(self.root, text="Background Information:")
        self.important_label = tk.Label(self.root, text="Important Points:")
        self.length_label = tk.Label(self.root, text="Approximate Length (words):")
    
        # Entry fields
        self.email_entry = tk.Entry(self.root)
        self.password_entry = tk.Entry(self.root, show="*")
        self.recipient_email_entry = tk.Entry(self.root)
        self.subject_entry = tk.Entry(self.root)
        self.recipient_address_entry = tk.Entry(self.root)
        self.sender_name_entry = tk.Entry(self.root)
        self.tone_entry = tk.Entry(self.root)
        self.goal_entry = tk.Entry(self.root)
        self.background_entry = tk.Entry(self.root)
        self.important_entry = tk.Entry(self.root)
        self.length_entry = tk.Entry(self.root)
       
        # Button
        self.generate_button = tk.Button(self.root, text="Generate Response", command=self.on_generate)
      
        # Grid layout
        self.email_label.grid(row=0, column=0, sticky="e")
        self.password_label.grid(row=1, column=0, sticky="e")
        self.recipient_email_label.grid(row=2, column=0, sticky="e")
        self.subject_label.grid(row=3, column=0, sticky="e")
        self.recipient_address_label.grid(row=4, column=0, sticky="e")
        self.sender_name_label.grid(row=5, column=0, sticky="e")
        self.tone_label.grid(row=6, column=0, sticky="e")
        self.goal_label.grid(row=7, column=0, sticky="e")
        self.background_label.grid(row=8, column=0, sticky="e")
        self.important_label.grid(row=9, column=0, sticky="e")
        self.length_label.grid(row=10, column=0, sticky="e")

        self.email_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)
        self.recipient_email_entry.grid(row=2, column=1)
        self.subject_entry.grid(row=3, column=1)
        self.recipient_address_entry.grid(row=4, column=1)
        self.sender_name_entry.grid(row=5, column=1)
        self.tone_entry.grid(row=6, column=1)
        self.goal_entry.grid(row=7, column=1)
        self.background_entry.grid(row=8, column=1)
        self.important_entry.grid(row=9, column=1)
        self.length_entry.grid(row=10, column=1)

        self.generate_button.grid(row=11)

        # initiate main loop
        self.root.mainloop()

    def on_generate(self):
    # Function to handle the "Generate Response" button click
        email_address = self.email_entry.get()
        password = self.password_entry.get()
        recipient_email = self.recipient_email_entry.get()
        subject = self.subject_entry.get()
        recipient_address = self.recipient_address_entry.get()
        sender_name = self.sender_name_entry.get()
        tone = self.tone_entry.get()
        goal = self.goal_entry.get()
        background = self.background_entry.get()
        important = self.important_entry.get()
        length = self.length_entry.get()   
        


gui = Gui()