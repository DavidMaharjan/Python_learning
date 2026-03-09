
# Importing the datetime module to work with date and time
import datetime


# The Email class represents a single email message
class Email:
    def __init__(self, sender, receiver, subject, body):
        # sender: User object who sends the email
        # receiver: User object who receives the email
        # subject: Subject line of the email (string)
        # body: Main content of the email (string)
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        # Store the time when the email is created
        self.timestamp = datetime.datetime.now()
        # Track if the email has been read
        self.read = False

    def mark_as_read(self):
        # Mark this email as read
        self.read = True

    def display_full_email(self):
        # Print all details of the email and mark it as read
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self):
        # String representation for listing emails (shows if read/unread)
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
# The Inbox class stores and manages all emails for a user
class Inbox:
    def __init__(self):
        # List to store Email objects
        self.emails = []

    def receive_email(self, email):
        # Add a new email to the inbox
        self.emails.append(email)

    def list_emails(self):
        # Print a summary list of all emails in the inbox
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    def read_email(self, index):
        # Display the full content of a specific email by its number
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1  # Convert to 0-based index
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()

    def delete_email(self, index):
        # Delete a specific email by its number
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1  # Convert to 0-based index
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')

# The User class represents a person who can send and receive emails
class User:
    def __init__(self, name):
        # name: The user's name (string)
        self.name = name
        # Each user has their own inbox
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        # Create an Email object and send it to another user's inbox
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self):
        # Show a summary of all emails in the user's inbox
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        # Read a specific email by its number
        self.inbox.read_email(index)

    def delete_email(self, index):
        # Delete a specific email by its number
        self.inbox.delete_email(index)


# # The main function demonstrates how the classes work together
# def main():
#     # Create two users
#     tory = User('Tory')
#     ramy = User('Ramy')        
    
#     # Tory sends an email to Ramy
#     tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
#     # Ramy replies to Tory
#     ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
#     # Ramy checks his inbox and reads the first email
#     ramy.check_inbox()
#     ramy.read_email(1)
#     # Tory checks his inbox
#     tory.check_inbox()

# # This checks if the script is being run directly (not imported)
# if __name__ == '__main__':
#     main()