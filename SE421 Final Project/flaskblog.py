from flask import Flask, render_template ,request
from postdata import posts
from flask_mail import Mail,Message
from waitress import serve
from concurrent.futures import thread

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = "g4project.medicare@outlook.com"
app.config['MAIL_PASSWORD'] = "G4proj@MC421"

mail = Mail(app)

@app.route("/")
def index():
   return render_template('index.html')

@app.route("/service")
def service():
    return render_template('service.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/contact-us" , methods = ['GET','POST'])
def contactUs():
    if request.method == 'POST' : 
        email = request.form.get('email')
        message = request.form.get('message')

        msg = Message(subject=f"New Contact Form Submission", 
                      body = f"Users E-Mail: {email}\n\nUsers Message: {message}", 
                      sender="g4project.medicare@outlook.com", 
                      recipients=['g4project.medicare@gmail.com'])
        mail.send(msg)
        return "Your E-Mail has been sent sucessfully"
    return render_template('contact-us.html')

@app.route("/mobile")
def mobile():
    return render_template('mobile.html')

@app.route("/reqres-data")
def reqresData():
    return render_template('reqres-data.html')

@app.route("/posts")
def home():
    return render_template('post-all.html',
                           title='all posts',
                           posts=posts)

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    if post_id < len(posts):
       p = posts[post_id]
       return render_template('post-single.html',
       title= f"Post#{post_id}", p = p )
    else:
        return render_template('404.html'), 404
    
#debug tool
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=80, threads=2, url_prefix="/my-app")
