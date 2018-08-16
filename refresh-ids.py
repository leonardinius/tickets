#!/usr/bin/env python3

import requests
import os
import sys
import json


def main():
    auth_token = os.environ['AUTH_TOKEN']
    url = 'https://devternity-22e74.firebaseio.com/applications.json?auth=%s' % auth_token

    ticketsIds = dict()
    data = requests.get(url).json()
    for docid, doc in data.items():
        if doc['product'] != 'DT_RIX_18':
            continue
        for ticket in doc['tickets']:
            ticketsIds[ticket['id']] = docid

    with open('./src/data/tickets.json', 'w') as w:
        w.write(json.dumps(ticketsIds, indent=True))


if __name__ == "__main__":
    main()
