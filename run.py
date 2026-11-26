from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit
from api.workspace import handler as WorkspaceHandler
ROOT=Path(__file__).resolve().parent/'public'

class LocalHandler(SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,directory=str(ROOT),**kwargs)
    def allowed(self):
        if self.headers.get('Host') in ('127.0.0.1:8765','localhost:8765'):return True
        self.send_error(403);return False
    def respond(self,status,value):
        WorkspaceHandler.respond(self,status,value)
    def do_GET(self):
        if not self.allowed():return
        if urlsplit(self.path).path=='/api/workspace':return WorkspaceHandler.do_GET(self)
        super().do_GET()
    def do_POST(self):
        if not self.allowed():return
        if urlsplit(self.path).path=='/api/workspace':return WorkspaceHandler.do_POST(self)
        self.send_error(404)

if __name__=='__main__':
    server=ThreadingHTTPServer(('127.0.0.1',8765),LocalHandler)
    print('Open http://127.0.0.1:8765/')
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()
