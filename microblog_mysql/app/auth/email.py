from flask import render_template, current_app
from flask_babel import _
from app.email import send_email


# def send_email(subject, sender, recipients, text_body, html_body):
#     msg = Message(subject, sender=sender, recipients=resipients)
#     msg.body = text_body
#     msg.html = html_body
#     mail.send(msg)
#     time.sleep(80)

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Bright] Reset Your Password',
        sender=app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('email/reset_password.txt',
                user=user, token=token),
        html_body=render_template('email/reset_password.html',
                user=user, token=token))
