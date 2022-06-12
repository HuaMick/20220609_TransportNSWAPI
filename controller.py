import pickle

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
