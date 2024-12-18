from flask import Flask, request, render_template
import csv
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        Today = request.form["Today"]
        Task = request.form["Task"]
        Details = request.form["Details"]
        with open("file.csv", "a", newline='') as f:
            writers = csv.writer(f)
            writers.writerow([Today, Task, Details])
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True) 