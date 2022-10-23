from flask import Flask, redirect, url_for, render_template, request
import RandomPhoto



app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def welcome():
    return render_template('index.html', RandomPhoto = RandomPhoto.GenerateRandomPhoto())




if __name__ == '__main__':
    app.run(debug= True)

