from tornado import web
class MainHandler(web.RequestHandler): 
    def get(self):
        self.render('index.html')


class JobHandler(web.RequestHandler):
    def get(self):
        self.render("job.html");

class AboutHandler(web.RequestHandler):
    def get(self):
        self.render("about.html");

class BusinessHandler(web.RequestHandler):
    def get(self):
        self.render("business.html");
        
class ExampleHandler(web.RequestHandler):
    def get(self):
        self.render("example.html");

class ContactHandler(web.RequestHandler):
    def get(self):
        self.render("contact.html");

class LinkHandler(web.RequestHandler):
    def get(self):
        self.render("link.html");

class FavHandler(web.RequestHandler):
    def get(self):
        self.redirect("/static/image/icon_small.png")


