from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nilai = int(request.form["nilai"])
        waktu = int(request.form["waktu"])

        level = model.predict([[nilai, waktu]])[0]

        print("Nilai:", nilai)
        print("Waktu:", waktu)
        print("Level:", level)


        return render_template("result.html", level=level)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)