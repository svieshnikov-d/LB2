from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def process_headers():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        return jsonify({"currency": "USD", "rate": 41.5})
    elif content_type == "application/xml":
        return """<response><currency>USD</currency><rate>41.5</rate></response>"""
    else:
        return "USD - 41.5"

if __name__ == '__main__':
    app.run(port=8000)