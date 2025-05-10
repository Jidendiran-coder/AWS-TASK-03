from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Flask App</h1>"

@app.route('/about')
def about():
    return "<p>This application demonstrates multiple routes using Flask on AWS EC2.</p>"

@app.route('/contact')
def contact():
    return "<p>Contact: your.email@example.com</p>"

@app.route('/status')
def status():
    return "<p>Status: Running smoothly ✅</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
