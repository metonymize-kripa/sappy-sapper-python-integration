from datetime import datetime, timedelta
from wallstreet import Call, Put, Stock
from http.server import BaseHTTPRequestHandler
from urllib import parse
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        curr_date = str(datetime.date(datetime.now()))
        if "sym" in dic:
            try:
                message = str(int(Stock(dic["sym"]).price))
            except:
                message = "-1"
        else:
            message = "Hello, stranger!"
        self.wfile.write(message.encode())
        return
