# -*- coding:utf-8 -*-

import urllib2
import simplejson

if __name__=="__main__":
	_dict = {"a":"b","c":"d"}
	json= simplejson.dumps(_dict,sort_keys=True)
	print _dict,type(_dict)
	print json,type(json)