from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from form import ContactForm

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'hello123'
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '179eb4affa4a89'
app.config['MAIL_PASSWORD'] = '527d07f36863d2'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route('/')
def home_page():
    return render_template('index.html')



def send_mail(form):
    sender = "zarafsha.u@gmail.com"
    receiver = "uzarafsha@yahoo.com"
    mes = form.message.data
    name = form.name.data
    email = form.email.data
    msg = Message(f'New Message from {name} ', sender=sender, recipients=[receiver])
    msg.body = f"Name:{name}\nMessage:{mes}\nEmail:{email}"
    mail.send(msg)
    print("Message Sent")


@app.route('/contact', methods=['GET', 'POST'])
def contact_me():
    form = ContactForm()
    if request.method=='POST':
        send_mail(form)
        return redirect(url_for('success'))
    return render_template('contact.html', form=form)


@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == "__main__":
    app.run(debug=True)