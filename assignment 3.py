import smtplib
import random
import datetime
import os


# Function for reading the quotes 

def read_quotes(filename):
    with open(filename, 'r') as file:
        quotes = file.readlines()
    return [quote.strip() for quote in quotes]

# function for reading email addresses 

def read_emails(filename):
    with open(filename, 'r') as file:
        emails = file.readlines()
    return [email.strip() for email in emails]

# function for  sending email

def send_email(to_email, subject, body):
    from_email = "yahyarizwan@gmail.com"  # write your email
    from_password = os.getenv('')  # Write your email password

    msg = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg)
        server.quit()
        print(f'Email sent to {to_email}')
    except Exception as e:
        print(f'Failed to send email to {to_email}. Error: {str(e)}')

# main  function 

def main():
    if datetime.datetime.today().weekday() == 0:
        quotes = read_quotes('quotes.txt')
        emails = read_emails('emails.txt')

        quote = random.choice(quotes)  

        for email in emails:
            send_email(email, "Monday Motivation", quote)
            
if __name__ == "__main__":
    main()
