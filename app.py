from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def home():
    a = {
        'Shreyas':1,
        'Jon':2,
        'Komal':3,
        'Hemanth':4
    }
    return render_template('index.html',dictionary=a)

if __name__ == '__main__':
    app.run(debug=True)