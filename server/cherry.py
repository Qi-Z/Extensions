#!/usr/bin/python2.6

# -*- coding: utf-8 -*-

'''
see also:
http://tools.cherrypy.org/wiki/RestfulDispatch
http://www.redmine.org/projects/redmine/wiki/Rest_api
'''

import sys;
import cherrypy
import time;

# set the default encoding to utf-8
# reload sys model to enable the getdefaultencoding method.
reload(sys);
# using exec to set the encoding, to avoid error in IDE.
exec("sys.setdefaultencoding('utf-8')");
assert sys.getdefaultencoding().lower() == "utf-8";

# supprt crossdomain ajax script
def enable_crossdomain():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*";
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, POST, HEAD, PUT, DELETE";

class Stream(object):
    exposed = True;
    def __init__(self, stream_id):
        self.stream_id = stream_id;
    def GET(self):
        enable_crossdomain();
        print("[Stream][GET] get a stream. id=%s"%(self.stream_id));
        return "id=%s"%(self.stream_id);
    def PUT(self):
        enable_crossdomain();
        print("[Stream][PUT] update a stream. id=%s"%(self.stream_id));
        self.stream_id = cherrypy.request.body.read()
    def DELETE(self):
        enable_crossdomain();
        print("[Streams][DELETE] delete a stream. id=%s"%(self.stream_id));
    def POST(self):
        enable_crossdomain();
        print("[Streams][POST] create a stream. NotAllowed");
        raise cherrypy.HTTPError(405)
    def OPTIONS(self):
        enable_crossdomain();

class Streams(object):
    exposed = True
    def __init__(self):
        pass;
    def GET(self):
        enable_crossdomain();
        print("[Streams][GET] get all streams");
        return "all stream list";
    def PUT(self):
        enable_crossdomain();
        print("[Streams][PUT] update all streams. NotAllowed");
        raise cherrypy.HTTPError(405)
    def DELETE(self):
        enable_crossdomain();
        print("[Streams][DELETE] delete all streams. NotAllowed");
        raise cherrypy.HTTPError(405)
    def POST(self):
        enable_crossdomain();
        print("[Streams][POST] create a new streams");
        info = cherrypy.request.body.read()
        print("[Streams][POST] new stream created. info=%s"%(info));
        return "Message from server!!!!!!";
    def __getattr__(self, name):
        # stream operations.
        if name.isdigit():
            return Stream(name);
        return object.__getattr__(name);
    def OPTIONS(self):
        enable_crossdomain();
    
class Root(object):
    exposed = True
    def __init__(self):
        pass;
    def GET(self):
        file = open("data.txt");
        data = file.read();
        file.close();
        return data;
    

root = Root()

root.streams = Streams();

conf = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 11200,
        'tools.encode.on':True, 
        'tools.encode.encoding':'utf8', 
    },
    '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
    }
}

cherrypy.quickstart(root, '/', conf)