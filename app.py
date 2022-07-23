from logging import debug
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def homepage():
    return "<p>Hello, World! My Friend</p>"


@app.route("/userinput", methods=["POST", "GET"])
def userinput():
    if request.method == "POST":
        first_name = request.form['fname']
        last_name = request.form['lname']
        return f"{first_name} {last_name}"
    else:  # GET REQUEST
        return render_template("index.html")


@app.route("/file_upload", methods=["POST", "GET"])
def user_image_upload():
    if request.method == "POST":
        uploaded_file = request.files['up-file']
        filename_file = uploaded_file.filename
        file_path = f"./uploads/{filename_file}"
        uploaded_file.save(file_path)
        return f"The uploaded file [{filename_file}] is at {file_path}"
    else:  # GET REQUEST
        return render_template("file_upload.html")


if __name__ == "__main__":
    app.run(debug=True)
