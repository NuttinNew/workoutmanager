#!/usr/bin/env python3
path = '/home/eric/work/python/workout/key.db'
key = open(path, 'r')
db_dict = key.read()
#db_dict = dict(key.read())
print(db_dict.type())
        
