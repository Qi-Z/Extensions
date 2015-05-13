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
import re;

import s2v as s2v
import numpy as np
import pickle


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

# class Stream(object):
#     exposed = True;
#     def __init__(self, stream_id):
#         self.stream_id = stream_id;
#     def GET(self):
#         enable_crossdomain();
#         print("[Stream][GET] get a stream. id=%s"%(self.stream_id));
#         return "id=%s"%(self.stream_id);
#     def PUT(self):
#         enable_crossdomain();
#         print("[Stream][PUT] update a stream. id=%s"%(self.stream_id));
#         self.stream_id = cherrypy.request.body.read()
#     def DELETE(self):
#         enable_crossdomain();
#         print("[Streams][DELETE] delete a stream. id=%s"%(self.stream_id));
#     def POST(self):
#         enable_crossdomain();
#         print("[Streams][POST] create a stream. NotAllowed");
#         raise cherrypy.HTTPError(405)
#     def OPTIONS(self):
#         enable_crossdomain();

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
        clf = pickle.load(open("./lr.p", "rb"))
        enable_crossdomain();
        print("[Streams][POST] create a new streams");
        info = cherrypy.request.body.read()
        # #print("[Streams][POST] new stream created. info=%s"%(info));

        list_of_comments = json.loads(info)
        print(type(list_of_comments))
        #print("from json!----"+list_of_comments["0"])
        for key in list_of_comments:
            #sentences_list = []
            sentences = list_of_comments[key]
            #print('------'+sentences+'-------')
            sentences_list = re.split(r' *[\.\?!][\'"\)\]]* *', sentences)
            vect = []
            #print sentences_list
            for each_sent in sentences_list:

                s2v.gen_feature_test(each_sent, vect)
            test_instance = np.array(vect)
            #print test_instance
            #print len(test_instance), len(test_instance[0])
            prediction = clf.predict(test_instance)
            comment_string = ''
            for i in range(len(prediction)):
                if int(prediction[i]) == 2:
                    comment_string += '<mark class = \"mark_as_praise\">'+sentences_list[i]+'</mark>' + '.'
                else:
                    comment_string += sentences_list[i] + '.'
            list_of_comments[key] = comment_string
            comment_string = ''
            #print "predicts", prediction
            #print(sentences_list[0])
        return json.dumps(list_of_comments);
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