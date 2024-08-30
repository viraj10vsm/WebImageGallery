from flask import Flask, render_template
import os 
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    array = os.listdir("C:/Users/viraj/OneDrive/Python/Day 44 Web Dev 4 CSS/6.4 Motivation Meme Project/static/assets/images")
    image_name = random.choice(array)
    print(image_name)
    return render_template("index.html", image_name=image_name)

if __name__ == "__main__":
    app.run(debug=True)