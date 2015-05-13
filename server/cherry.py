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
import json;
import re
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
    #cherrypy.response.headers["Access-Control-Allow-Headers"] = "Cache-Control, X-Proxy-Authorization, X-Requested-With";
    #cherrypy.response.headers["Access-Control-Max-Age"] = "604800";

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
        return "response from GET";
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
        #print("[Streams][POST] new stream created. info=%s"%(info));

        list_of_comments = json.loads(info)
        print(type(list_of_comments))
        #print("from json!----"+list_of_comments["0"])
        for key in list_of_comments:
            #sentences_list = []
            sentences = list_of_comments[key]
            #print('------'+sentences+'-------')
            sentences_list = re.split(r' *[\.\?!][\'"\)\]]* *', sentences)
            
            print(sentences_list[0])
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
    
# http://192.168.20.94:1970/
root = Root()
# http://192.168.20.94:1970/streams
# http://192.168.20.94:1970/streams/100
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