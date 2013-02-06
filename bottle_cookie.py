import bottle
@bottle.route('/cookie/set')
def get_cookie():
    return "cookie: "+bottle.request.get_cookie("cookie","it is a cookie")

@bottle.route('/cookie/get')
def set_cookie():
    bottle.response.set_cookie("cookie","it is a cookie")


bottle.debug(True)
bottle.run(host='localhost', port=8080)
