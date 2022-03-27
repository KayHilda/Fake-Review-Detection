from flask import Flask, escape, request, render_template
import pickle

vector = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/review', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        reviews = str(request.form['reviews'])
        print(reviews)

        predict = model.predict(vector.transform([reviews]))[0]
        print(predict)

        return render_template("review.html", prediction_text="reviews is -> {}".format(predict))


    else:
        return render_template("review.html")


if __name__ == '__main__':
    app.debug = True
    app.run()