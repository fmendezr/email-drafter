# Email Helper

Email Helper is a program that assists users in generating email drafts through a user-friendly interface. It utilizes the power of the ChatGPT API and is built using the Tkinter library for the graphical user interface.

## Purpose

The purpose of this program is to simplify the process of drafting emails by providing a guided approach. It prompts the user for various details such as sender's email address, recipient's email address, subject, tone, goal, and other relevant information. Using the ChatGPT API, it generates a draft email message based on the provided inputs.

## Features

- User-friendly graphical interface powered by Tkinter.
- Interactive prompts to gather email details.
- Utilizes the ChatGPT API to generate email drafts.
- Customizable email fields such as sender's email address, recipient's email address, subject, tone, and goal.
- Ability to include background information and important details in the email.
- Inactive "sender.py" file for sending emails directly from the interface (due to Google's deactivation of third-party app access to Gmail accounts).

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/email-helper.git

2. Navigate to the project directory:

    cd email-helper

3. Install the required dependencies:

    pip install -r requirements.txt

4. Obtain an API key from the ChatGPT API provider.

5. Create a .env file in the project root directory.

6. Add the following line to the .env file, replacing ur_key with your API key:

    API_KEY = "ur_key"

## Usage 

1. Run the program:

    python main.py 


2. Fill in the prompted information in the graphical interface.

3. Click the "Generate Response" button to generate the email draft based on the provided inputs.

4. Copy the generated draft and use it as a basis for composing your email.

5. Please note that the "sender.py" file for directly sending emails from the interface is inactive due to Google's deactivation of third-party app access to Gmail accounts. You may need to manually copy the generated draft to your email client or make use of another email-sending solution.