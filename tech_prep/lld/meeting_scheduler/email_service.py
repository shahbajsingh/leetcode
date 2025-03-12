class EmailService:
    @staticmethod
    def send_email(recipient, subject, body):
        print(f'Sending email to {recipient}')
        print(f'Subject: {subject}')
        print(f'Body: {body}')
        print('-' * 50)