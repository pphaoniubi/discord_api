import requests
import pandas as pd
import os
import time
from datetime import datetime

before = ''


headers = {
    'Authorization' : '',
}

name_list = []
text_list = []
time_list = []



for i in range(10000):
    time.sleep(0.1)
    name_list = []
    text_list = []
    time_list = []

    name_fuck_list = []
    url = 'https://discord.com/api/v9/channels/490687126774480916/messages?before={}&limit=100'.format(before)
    res = requests.get(url=url, headers=headers)

    data = res.json()
    
    try:
        before = data[99]['id']
        
    except:
        print('not 99')

    print('page: {} count {} before {}'.format(i, len(data), before))
    count = 0
    for i in data:
        text_list.append(i['content'])
        name_list.append(i['author']['username'])
        time_list.append(datetime.fromisoformat(i['timestamp']).strftime('%Y-%m-%d %H:%M:%S'))
        
    outfile = 'Discord.csv'

    df = pd.DataFrame({
        'Page': count + 1,
        'Text': text_list,
        'Username': name_list,
        'Time': time_list,
    })

    if os.path.exists(outfile):
        header = False
    else:
        header=True


    df.to_csv(outfile, mode = 'a+', encoding = 'utf_8_sig', index = False, header = header)

    count = count + 1

    try:
        data[99]['id']
        
    except:
        break