#!/usr/bin/env python3

import json
import sys
from dateutil import parser

watson_log = json.load(sys.stdin)
header = 'Email,Client,Project,Start date,Start time,Duration,Tags'
email = 'bpomerantz@maizeanalytics.com'
clients = {'hendrick': 'Hendrick Health', 'chhs': 'Children\'s Hospital of Wisconsin', 'infirmary': 'Infirmary Health'}
print(header)

for log in watson_log:
    if log['project'] not in clients:
        continue

    start_time = parser.parse(log['start'])
    stop_time = parser.parse(log['stop'])
    delta = stop_time - start_time
    duration = '{:0>8}'.format(str(delta))
    
    print('{email},{project},{project},{start_date},{start_time},{duration},{tag}' \
        .format(email=email, project=clients[log['project']], start_date=start_time.strftime('%Y-%m-%d'),
                start_time=start_time.strftime('%H:%M:%S'), duration=duration, tag=log['tags'][0].capitalize()))
