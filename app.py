from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/foo/bar")
def foobar():
    return render_template("./foo/bar.html")


# for Build
#
@app.route("/output")
def output():
    templates = {"index.html": "", "foo/bar.html": "foo"}
    for template, directory in templates.items():
        html = render_template(template)
        output_dir = os.path.join("dist", directory)
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.join(output_dir, os.path.basename(template))
        with open(filename, "w") as f:
            f.write(html)
    return "Create HTML files as Static Files!! (^0^)/"


## for Browser Preview
#
if __name__ == "__main__":
    app.run(debug=True)
