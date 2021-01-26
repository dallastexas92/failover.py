import redis
import random
import time
import sys

host = "redis-13630.dallas-east.demo.redislabs.com"
port = 13630
password = ""
r = redis.Redis(host = host, port = port, password = password)

loop = 0
i = 0
retry=0
connected = True

r.set("key", "-1")

while connected:
    try:
        while loop < 5000000:
            r.incr("key")
            #time.sleep(.005)
            print(r.get("key"))
            loop+=1
        break
    except redis.ConnectionError:
        print("Made it to except block")
        print("Connection Error, retry %s" % retry)
        #time.sleep(1)
        retry +=1
        r=redis.Redis(host=host, port=port, password=password)
print("'# of Retries: %s" % retry)
sys.exit()
