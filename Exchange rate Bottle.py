from bottle import route, run, request

@route('/currency', method='GET')
def currency():
    today = request.query.today
    key = request.query.key
    return "USD - 41.5" if today and key else "Invalid request"

if __name__ == '__main__':
    run(host='localhost', port=8000)
