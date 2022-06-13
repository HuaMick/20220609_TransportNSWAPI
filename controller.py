import pickle
import datetime

def Unpickle_JSON():
    with open('json_response.pickle', 'rb') as handle:
        json_response = pickle.load(handle)
    return json_response

def Unpack_JSON(json_response):
    Response = {}
    Response['Header'] = [{k:v} for k,v in json_response.items()][0]
    Response['Contents'] = [{k:v} for k,v in json_response.items()][1]['entity']
    Response['Alerts'] = {v['id']:v['alert'] for v in Response['Contents']}
    return Response

def DF_Container(header):
    container = {h:[] for h in header}
    return container
    
def JSON_Timestamp(key, activePeriod = None):
    if key in activePeriod:
        return datetime.datetime.fromtimestamp(int(activePeriod[key]))
    else:
        return None

def DF_Populate(alerts, df_container):
    for n0, (id, alert) in enumerate(alerts.items()):
        for n1, (rout) in enumerate(alert['informedEntity']):
            packet = {
                'alert_id':id
                , 'start':JSON_Timestamp('start', alert['activePeriod'][0])
                , 'end':JSON_Timestamp('end', alert['activePeriod'][0])
                , 'effect':alert['effect']
                , 'cause':alert['cause']
                , 'url': alert['url']['translation'][0]['text']
                , 'routeId':rout['routeId']
                , 'directionId':rout['directionId']
            }
            for k,v in packet.items():
                df_container[k].append(v)
    return df_container