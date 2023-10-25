from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def api(word):
    file = pd.read_csv("dictionary.csv")
    definition = file.loc[file[word] == word]
    result_dictionary = {"word": word, "definition": definition}
    return result_dictionary


if __name__ == "__main__":
    app.run(debug=True, port=5002)
