#!/usr/bin/env python
import urlfetch
import logging
import json
import os
from datetime import date, datetime, timedelta
# See inspiration from https://github.com/Flet/dailyconnect

# Uses ENV vars:
# * DC_EMAIL: Your login to DailyConnect
# * DC_PASS: Your password to DailyConnect
# * DC_STARTDATE: The first date to gather photos
# * DC_ENDDATE: The last date to gather photos

s = urlfetch.Session()
r = s.post('https://www.dailyconnect.com/Cmd?cmd=UserAuth', data={"email": os.environ['DC_EMAIL'], "pass": os.environ['DC_PASS']})
r = s.post('https://www.dailyconnect.com/CmdW', data={"cmd": "UserInfoW"})
j = json.loads(r.body)
myKids = j['myKids']
start_date = datetime.strptime(os.environ['DC_STARTDATE'], "%y%m%d")
end_date = datetime.strptime(os.environ['DC_ENDDATE'], "%y%m%d")
delta = end_date - start_date

for d in (start_date + timedelta(n) for n in range(delta.days+1)): 
  pdt = d.strftime("%y%m%d") 
  print(pdt)
  for kid in myKids:
    r = s.post('https://www.dailyconnect.com/CmdListW', data={"cmd": "StatusList", "Kid": kid['Id'], "fmt": "long", "pdt": pdt})
    j = r.json
    for post in j['list']:
      if 'Photo' in post:
        pid = post['Photo']
        print(pid)
        if not os.path.exists(f"{kid['Id']}"):
          os.mkdir(f"{kid['Id']}")
        with s.get(f'https://www.dailyconnect.com/GetCmd?cmd=PhotoGet&id={pid}') as r:
          with open(f"{kid['Id']}/{post['Pdt']}_{pid}.jpg", 'wb') as f:
            for chunk in r:
              f.write(chunk)
        with open(f"{kid['Id']}/{post['Pdt']}_{pid}.txt", 'w') as f:
          f.write(post['Txt'])
    
