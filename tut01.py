import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello Orion. This is Cherrypy!"


cherrypy.quickstart(HelloWorld())
