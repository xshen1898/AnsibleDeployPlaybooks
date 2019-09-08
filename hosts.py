#!/usr/bin/env python3

import json


inventory = {
    'webservers': {
        'hosts': ['webserver-0' + str(i) + '.demo.com' for i in range(1, 3)]
    },
    'dbservers': {
        'hosts': ['dbserver-01.demo.com']
    },
    'lbservers': {
        'hosts': ['lbserver-01.demo.com']
    },
    'nagiosservers': {
        'hosts': ['nagiosserver-01.demo.com']
    }
}
print(json.dumps(inventory, indent=4))
