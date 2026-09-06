from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory task storage
tasks = []


# Home page - GET request
@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)


# Add task - POST request
@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")

    if task:
        tasks.append(task)

    return redirect(url_for("home"))


# Delete task
@app.route("/delete/<int:index>")
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
