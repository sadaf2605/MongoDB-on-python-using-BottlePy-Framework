import bottle

@bottle.route('/')
def home_page():
    return "hello world\n"

@bottle.route('/testage')
def test_page():
    return "this is a test page"

bottle.debug(True)
bottle.run(host='localhost', port=8080)
