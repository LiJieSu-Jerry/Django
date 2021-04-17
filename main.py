import datetime
import pprint
"""
a=datetime.timedelta(days=1, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
b=datetime.datetime.now()
c=datetime.timedelta(days=10)

print(b-a<b+c)

import json
import urllib.request

GEO_IP_API_URL  = 'http://ip-api.com/json/'

# Can be also site URL like this : 'google.com'
IP_TO_SEARCH    = '73.134.227.105'

# Creating request object to GeoLocation API
req= urllib.request.Request(GEO_IP_API_URL+IP_TO_SEARCH)
# Getting in response JSON
response= urllib.request.urlopen(req).read()
# Loading JSON from text to object
json_response   = json.loads(response.decode('utf-8'))

# Print country
print(json_response)

"""

"""
from functools import wraps
 
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging
 
@logit
def addition_func(x):
  
   return x + x
 
 
result = addition_func(4)
print(result)

"""

import re

phoneNumRegex = re.compile(r'^sn')
mo = phonenumregex.search('sndlejifjl kjdflk 111')
print(mo)
