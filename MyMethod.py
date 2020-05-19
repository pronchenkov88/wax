from http.server import BaseHTTPRequestHandler
import urllib.parse
from urllib.parse import urlparse
import json
import requests
class MyHandler(BaseHTTPRequestHandler):

    def do_GET(s):
        base_url = "http://jsonplaceholder.typicode.com/"
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write(b"<html><head><title>Title goes here.</title></head>")
        s.wfile.write(b"<body><p>OK.</p>")
        query_components = urllib.parse.parse_qs(urlparse(s.path).query)
        json_string = json.dumps(query_components)
        s.wfile.write(bytes(json_string.encode(encoding='utf_8')))
        s.wfile.write(b"</body></html>")
        data = query_components.get("q", "")
        newUrl = base_url+data[0]
        print(newUrl)
        response = requests.get(base_url+data[0])
        print(response.text)
        s.wfile.write(bytes(json.dumps(response.text).encode()))




