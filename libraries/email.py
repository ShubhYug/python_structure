from flask import url_for, render_template
from flask_babel import _
from flask_mail import Message, Mail
from app_name import app
import os

# Mail .env 
# Configure Flask-Mail for Gmail
# app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
# app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
# app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME') 
# app.config['MAIL_PASSWORD'] =  os.getenv('MAIL_PASSWORD')
# app.config['MAIL_USE_SSL'] = True

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465  # Use 465 for SMTP_SSL
app.config['MAIL_USERNAME'] = 'shubhamsameliyamindiii@gmail.com'
app.config['MAIL_PASSWORD'] = 'enei xjim uvgi tjuv'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False



# Mail
mail = Mail(app)

# @app.route("/mail")
def send_email(toEmail, subject, html_template):  
    msg = Message(subject, sender = os.getenv('MAIL_USERNAME') , recipients = [toEmail])
    msg.html = html_template
    # Send the email
    mail.send(msg)
    return 'Email sent successfully!'
    
