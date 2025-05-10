# AWS Task 3: Add Routes to the Flask Application

## Objective

Enhance the Flask application deployed in Task 2 by adding multiple routes to display different pages.

---

## Task Steps

### 1. Prerequisite

Complete [Task 2](../task-2/) to deploy the basic Flask application on an EC2 instance.

### 2. Add Routes in `app.py`

Update your `app.py` to include the following routes:

- `/` — Homepage: Welcome message
- `/about` — About Page: Info about the application
- `/contact` — Contact Page: Contact info
- `/status` — Status Page: Health or uptime check

Example implementation:

```python
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
