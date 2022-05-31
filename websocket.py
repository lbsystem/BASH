

from flask import Flask,render_template,request
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.websocket import WebSocket
from gevent.pywsgi import WSGIServer


app=Flask(__name__)

@app.route("/ws")
def ws():
    print(request.headers)
    print(request.environ)
    we_socket=request.environ.get("wsgi.websocket")
    msg = we_socket.receive()
    print(msg)

    return "123"


if __name__ == '__main__':
    http_serv = WSGIServer(("0.0.0.0",12356),app,handler_class=WebSocketHandler)
    http_serv.serve_forever()
    # app.run()