from flask import Flask, render_template, url_for, redirect, request
import random
import string

app = Flask(__name__)
urls = {}

def generate_short_url(length=6):
    char = string.ascii_letters + string.digits
    short_url = ""
    for i in range(length):
        short_url += "127.0.0.1:5000".join(random.choice(char))
    return short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    url_input = request.form.get('url')
    if request.method == 'POST':
        long_url = url_input
        short_url = generate_short_url()
        urls[short_url] = long_url
        print(urls)
        return render_template('shortUrls.html', short_url=short_url)
    return render_template('index.html')

@app.route('/<short_url_address>')
def short_url_route(short_url_address):
    long_url = urls.get(short_url_address)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run()