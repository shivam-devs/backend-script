import requests
import time
while 1:
    requests.get('https://backend-96qf.onrender.com/api/questions')
    time.sleep(15)
    print("Once More")