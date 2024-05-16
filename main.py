from flask import Flask, render_template, redirect, request
import datetime

app = Flask(__name__)
year = datetime.datetime.now().year


@app.route('/')
def home():
    return render_template('home_page.html', year=year)


@app.route('/<page>')
def render_page(page):
    valid_pages = ['cv', 'certificates', 'profile', 'about', 'contact']
    if page in valid_pages:
        return render_template(f'{page}.html', year=year)
    else:
        return render_template('404.html', year=year), 404


@app.route('/<web>')
def get_web(web):
    if web == 'twitter':
        return redirect('https://twitter.com/Mirek4g')
    elif web == 'facebook':
        return redirect('https://www.facebook.com/mirek.gregorowicz')
    elif web == 'github':
        return redirect('https://github.com/Mirek33g')
    elif web == 'linkedin':
        return redirect('https://www.linkedin.com/in/miroslaw-gregorowicz-29694a29a/')
    elif web == 'email':
        return redirect('mailto: mirek33g@gmail.com')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
