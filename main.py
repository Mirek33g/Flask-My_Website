from flask import Flask, render_template, redirect
import datetime

app = Flask(__name__)
year = datetime.datetime.now().year


@app.route('/')
def home():
    return render_template('home_page.html', year=year)


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


@app.route('/profile')
def profile():
    return render_template('profile.html', year=year)


@app.route('/about')
def about():
    return render_template('about.html', year=year)


@app.route('/contact')
def contact():
    return render_template('contact.html', year=year)


if __name__ == '__main__':
    app.run(debug=True)


