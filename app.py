from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/grid-system/bootstrap-v5.3.0")
def grid_system_bs():
    return render_template("./grid-system/bootstrap-v5.3.0.html")


@app.route("/grid-system/tailwind-v3.3.2")
def grid_system_tw():
    return render_template("./grid-system/tailwind-v3.3.2.html")


# for Build
#
@app.route("/output")
def output():
    templates = {
        "index.html": "",
        "grid-system/tailwind-v3.3.2.html": "grid-system",
        "grid-system/bootstrap-v5.3.0.html": "grid-system",
    }

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
