import datetime
import requests
response = requests.get(
    'https://api.transport.nsw.gov.au/v2/gtfs/alerts/buses?format=json'
    , headers={'Authorization': 'apikey rG3uaQgSxI8LbkMvtwS9fp61tZdQmxDOcqNj'})
json_response = response.json()

import pickle
with open('json_response.pickle', 'wb') as handle:
    pickle.dump(json_response, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('20220611.pickle', 'rb') as handle:
    json_response = pickle.load(handle)

import pandas as pd
pd.read_json(json_response)

header = [{k:v} for k,v in json_response.items()][0]
content = [{k:v} for k,v in json_response.items()][1]['entity']
alerts = {v['id']:v['alert'] for v in content}

df_dictionary = {
    'alert_id': []
    , 'start': []
    , 'end': []
    , 'effect': []
    , 'cause': []
    , 'url': []
    , 'routeId':[]
    , 'directionId':[]
}

for n0, (id, alert) in enumerate(alerts.items()):
    if n0 > 20:
        break
    for n1, (rout) in enumerate(alert['informedEntity']):
        if n1 > 20:
            break
        packet = {
            'alert_id':id
            , 'start':datetime.datetime.fromtimestamp(alert['activePeriod'][0]['start'])
            , 'end':datetime.datetime.fromtimestamp(alert['activePeriod'][0]['end'])
            , 'effect':alert['effect']
            , 'cause':alert['cause']
            , 'url': alert['url']['translation'][0]['text']
            , 'routeId':rout['routeId']
            , 'directionId':rout['directionId']
        }
        print(str(n0)+':'+str(n1)+':'+str(packet))
        for k,v in packet.items():
            df_dictionary[k].append(v)

df = pd.DataFrame.from_dict(df_dictionary)   

"""Scrap Pad"""
#alerts[0]['activePeriod'] = [{'start': '1654902822', 'end': '1654956462'}]
#alerts[0]['informedEntity'] = [{'agencyId': 'NSWTrains', 'routeId': 'SCO_1a', 'directionId': 0}]
#alerts[0]['cause'] = 'OTHER_CAUSE'
#alerts[0]['effect'] = 'NO_SERVICE'
#alerts[0]['url'] = {'translation': [{'text': 'https://transportnsw.info/alerts/details#/ems-5927', 'language': 'en'}]}
#alerts[0]['headerText'] = {'translation': [{'text': 'F7 Ferry cancellations', 'language': 'en'}]}
#alerts[0]['descriptionText'] = {'translation': [{'text': 'The following services are cancelled due to staff shortages.\n10 57 p m ferry from Circular Quay to Double Bay and 11 20 p m Double Bay to Circular Quay service.\xa0\nPassengers should make alternative travel arrangements.\xa0', 'language': 'en'}, {'text': '<div>The following services are cancelled due to staff shortages.<br />10:57pm ferry from Circular Quay to Double Bay and 11:20pm Double Bay to Circular Quay service.&nbsp;<br />Passengers should make alternative travel arrangements.&nbsp;</div>', 'language': 'en/html'}]}

"""Spare Code"""
#quickly list dictionary header
#list(json_response.items())[0] 