import tornado.ioloop 
import tornado.web 
from tornado import web

class MainHandler(tornado.web.RequestHandler): 
    def get(self):
        self.render('index.html')

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/static/(.*)", web.StaticFileHandler, {"path": "./static/"})
], template_path = "./template")

print application.settings.get("template_path")

if __name__ == "__main__":
    application.listen(19898)
    tornado.ioloop.IOLoop.instance().start()	
