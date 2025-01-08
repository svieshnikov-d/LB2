from bottle import route, run, request, response

@route('/', method='GET')
def process_headers():
    content_type = request.get_header("Content-Type")
    if content_type == "application/json":
        response.content_type = "application/json"
        return {"currency": "USD", "rate": 41.5}
    elif content_type == "application/xml":
        response.content_type = "application/xml"
        return """<response><currency>USD</currency><rate>41.5</rate></response>"""
    else:
        return "USD - 41.5"

if __name__ == '__main__':
    run(host='localhost', port=8000)