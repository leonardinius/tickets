#!/usr/bin/env python3

import requests
import os
import sys
import json


def main():
    auth_token = os.environ['AUTH_TOKEN']
    url = 'https://devternity.firebaseio.com/registrations.json?auth=%s' % auth_token

    ticketsIds = []
    errors = 0
    data = requests.get(url).json()
    for docid, doc in data.items():
        # if 'product' not in doc:
        #     print("Document error (product): %s\n" % docid)
        #     errors += 1
        #     continue

        # if doc['product'] != 'DT_RIX_18':
        #     continue

        # if 'tickets' not in doc:
        #     print("Document error (tickets): %s\n" % docid)
        #     errors += 1
        #     continue

        # for ticket in doc['tickets']:
        ticketsIds.append(doc['ID'])

    with open('./src/data/tickets.json', 'w') as w:
        w.write(json.dumps(ticketsIds, indent=True))
    
    print("Success: %d, Errors: %d" % (len(ticketsIds), errors))

if __name__ == "__main__":
    main()
