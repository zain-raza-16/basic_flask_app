from flask import Flask, render_template ,url_for

app = Flask(__name__)

possible = [
    {
        "author": "Tony Robbins",
        "Title": "Awaken the giant Within",
        "Nationality": "American"
    },
    {
        "author": "Astreavan",
        "Title": "Climb",
        "Nationality": "Czech"
    }
]


@app.route('/')
def hello_world():
    return render_template('Wrong.html', posts=possible)


@app.route('/about')
def real():
    return render_template('about.html')

@app.route('/page')
def page():
    return render_template('page.html')



if __name__ == "__main__":
    app.run(debug=True)
