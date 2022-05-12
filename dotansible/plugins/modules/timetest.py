#!/usr/bin/env python3

import datetime
import json
from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = r'''
---
module: timetest

short_description: asdf

version_added: "2.3.4"

description: Hello documentation

author: 
 - Rob

'''

EXAMPLES = r'''
Hello Examples
'''

def now():
    return str(datetime.datetime.now())

def utc():
    return str(datetime.datetime.utcnow())

def main():
    fields = {
        "utc": {"required": False, "type": "bool", "default": False},
    }
    result = { "changed": False, "date":"" }
    module = AnsibleModule(argument_spec=fields)
    if module.params["utc"]:
        result["date"] = utc()
    else:
        result["date"] = now()

    module.exit_json(**result)

if __name__ == '__main__':
    main()
