import random
import string
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
from flask import Flask, request, render_template_string

app = Flask(__name__)
# Define the HTML template
template = """
<html>
    <body>
        <h1>Result</h1>
        <p>Name: {{ name }}</p>
        <p>Email: {{ email }}</p>
    </body>
</html>
"""

@app.route('/', methods=['GET'])

def index():
    return render_template_string("""
    <html>
      <body>
         <form action="/submit" method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>
            <label for="email">Email:</label>
            <input type="text" id="email" name="email"><br><br>
            <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """)

def generate_otp(length=6):
    return ''.join(random.choices(string.digits,k=length))
otp =generate_otp()
print(otp)

###textMessage = client.messages.create(
     #   body= f'Hello, Your OTP is {otp}',
    #    from_= "+15074486696",
  ##      to = "+16592532221"
   # )
##print(textMessage.body)

myPassword = 'eztf zjdn xhlw nqvc'
myEmail = 'caseyyoung1985@gmail.com'

@app.route('/submit', methods=['POST'])

def submit():
    name = request.form['name']
    email = request.form['email']
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(myEmail, myPassword)

    msg = MIMEText(f'Hello {name}, Your OTP is {otp}')
    
    server.sendmail(myEmail, email, msg.as_string())

    msg['Subject'] = 'OTP for verification'
    msg['From'] = myEmail
    msg['To'] = email
    server.quit()
    print(msg)
    return render_template_string("""
    <html>
      <body>
         <h1>Check Your email</h1>
      </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)
    


def verify_otp(user_input):
    if user_input == otp:
        return True
    return False