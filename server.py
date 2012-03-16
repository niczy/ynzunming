import tornado.ioloop 
import tornado.web 
from tornado import web
from controller import handlers

application = tornado.web.Application([
	(r"/", handlers.MainHandler),
    (r"/about", handlers.AboutHandler),
    (r"/job", handlers.JobHandler),
    (r"/favicon.ico", handlers.FavHandler),
	(r"/static/(.*)", web.StaticFileHandler, {"path": "./static/"})
], template_path = "./template", debug=True)

print application.settings.get("template_path")

if __name__ == "__main__":
    application.listen(19898)
    tornado.ioloop.IOLoop.instance().start()	
