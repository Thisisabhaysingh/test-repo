from flask import Flask, render_template, request

app = Flask(__name__)

feedback_list = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
       
        feedback_list.append({"name": name,})

    return render_template("index.html", feedbacks=feedback_list)


if __name__ == "__main__":
    app.run(debug=True)
