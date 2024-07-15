📧 Motivational Quotes Email Sender 📧
Description 📝
This Python script sends motivational quotes to email addresses every Monday. It reads quotes from a text file and email addresses from another file, and then sends a randomly selected quote to each email address using Gmail's SMTP server.

Features ✨
Read Quotes: Reads motivational quotes from a file (quotes.txt).
Read Emails: Reads email addresses from a file (emails.txt).
Send Emails: Sends motivational quotes to the email addresses every Monday.
Random Quote Selection: Selects a random quote to send to each recipient.

How It Works 🛠️
Reads Quotes: The script reads quotes from quotes.txt, where each line contains one quote.
Reads Emails: The script reads email addresses from emails.txt, where each line contains one email address.
Check Day: The script checks if today is Monday.
Send Emails: If it's Monday, the script selects a random quote and sends it to each email address using Gmail's SMTP server.

Prerequisites 📋
Python 3.x
Required Libraries: smtplib, random, datetime, os
Environment Variable: GMAIL_PASSWORD must be set to your Gmail password.

