def send_email(subject, body, recipient=None):
    if recipient is None:
        recipient = "support@example.com"
    print(f'{subject}, {body}, {recipient}')

send_email('fafs', "afasf", 111)


