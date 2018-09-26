"""
试试imap
"""
import email, getpass, imaplib, os

user = "sepjudy@gmail.com"
pwd = "ADSZadsz123"
m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user, pwd)
resp, items = m.search(None, "ALL")
items = items[0].split()
print(items)