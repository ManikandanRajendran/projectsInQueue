from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def homepage():
    # with open('static/data.csv', 'r') as file:
        # reader = csv.reader(file)
        # for row in reader:
        #     print(row)
    return render_template('index.html')

if __name__ == "__main__":    
    app.run(debug=True)
