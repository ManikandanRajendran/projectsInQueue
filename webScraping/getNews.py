import news
from flask import Flask

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    response = news.fetch_response()
    if response.status_code == 200:
        value = news.fetch_using_bs4(response)
        return render_template("index.html", message=value)
    else:
        return render_template("error.html", message="Unable to fetch news")


if __name__ == '__main__':
    app.run(debug=True)

