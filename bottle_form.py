import bottle

@bottle.route("/")
def form():
    return "<form action='\\form' method=POST><input type=text name=t><br><input type=submit></input></form>"


@bottle.post("/form")
def form2():
    text=bottle.request.forms.get("t")
    return "you have intered the text: "+text

bottle.debug(True)
bottle.run(host='localhost', port=8080)
