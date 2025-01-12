# Path: flask_app/app.py
from flask import Flask, request, jsonify, render_template
import io
import contextlib

app = Flask(__name__)

@app.route("/")
def index():
    """
    Renders the main HTML page.
    """
    return render_template("index.html")

@app.route("/execute", methods=["POST"])
def execute_code():
    """
    Endpoint to execute Python code sent via a POST request.

    Captures the code, executes it, and returns the output or an error message.
    """
    code = request.json.get("code", "")  # Get code from the request
    output = io.StringIO()  # StringIO to capture print output

    try:
        # Redirect stdout to capture print statements
        with contextlib.redirect_stdout(output):
            exec(code, {})  # WARNING: Avoid using exec() in production!
        return jsonify({"output": output.getvalue()})
    except Exception as e:
        # Return the error message if execution fails
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
