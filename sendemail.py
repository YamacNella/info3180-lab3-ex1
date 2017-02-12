import smtplib

from_addr = 'thingythingthing@gmail.com'
to_addr = 'kittystar123@someemail.com'
message = """From: {Camay} <wgs.camay.allen@gmail.com>
To: {Kitty} <kittystar123@someemail.com>
Subject: This Lab!
I miss you kitty. Be good.
"""

# Credentials (if needed)
username = 'thingythingthing@gmail.com'
password = 'password'
 
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message)
server.quit()