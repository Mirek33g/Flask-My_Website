from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)
year = datetime.datetime.now().year




@app.route('/')
def home():
    return render_template('home_page.html', year=year)


@app.route('/<web>', methods=['GET', 'POST'])
def get_web(web):
    if request.method == 'POST':
        if web == 'facebook':
            return redirect('https:/facebook.com/mirek.gregorowicz')
        elif web == 'github':
            return redirect('https://github.com/Mirek33g')
        elif web == 'twitter':
            return redirect('https://twitter.com/mirekgregorowicz')
        elif web == 'email':
            return redirect('mailto: email@gmail.com')
        else:
            return redirect('/')
    else:
        return redirect('/')


@app.route('/contact')
def contact():
    return render_template('contact.html', year=year)


@app.route('/about')
def about():
    return render_template('about.html', year=year)


if __name__ == '__main__':
    app.run(debug=True)
