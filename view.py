import model
import controller
import pandas as pd

import streamlit as st

APPINFO = st.container()

if 'API_JSON' not in st.session_state:
    st.session_state['API_JSON'] = None

APPINFO.subheader('Application Info')
#APPINFO.write(st.session_state)

st.title('NSW Transport API')
OVERVIEW = st.container()
OVERVIEW.subheader('Project Overview')
OVERVIEW.write('This is a learning project where I dive into the Transport of NSW API') 
OVERVIEW.write('I am using streamlit to build this web application as a blog') 

STEP1 = st.container()
STEP1.subheader('Getting Data From The API')
STEP1.write('Objective: Pull the transport alerts data using the NSW API') 
STEP1.write('We just register on the transport nsw website. Then we cam use the python requests module.')
STEP1.write('Once regstered you will be provided an API Key. Then just pass this in the header of your request:')
url = 'https://api.transport.nsw.gov.au/v2/gtfs/alerts/buses?format=json'
text_code_snippet = (
    f'response = requests.get("{url}"'
    ', headers={"Authorization": "apikey rG3u..."}') 
STEP1.code(text_code_snippet, language="python")
STEP1.write('We do not want to make too many requests so have stored this in a pickle file.')
STEP1.write('This way when ever I start a new session no need to make a new request, just unpickle my data')

API_SAMPLE = STEP1.expander('API JSON')
api_response_raw = controller.Unpickle_JSON()
API_SAMPLE.write(str(api_response_raw)[:600]+'...')

STEP2 = st.container()
STEP2.subheader('Interpret the API Data')
STEP2.write('Objective: review the API data, figure out which bits we want.') 
STEP2.write('The response module decodes the data into JSON for us, but its still pretty messy.') 
STEP2.write('Using list comprehension magic to traverse the JSON we can break it into more digestable parts.')

api_response = controller.Unpack_JSON(api_response_raw)
API_HEADER = STEP2.expander('API Header')
api_header = api_response['Header']
API_HEADER.write(api_header)
API_ALERTS = STEP2.expander('API Alerts')
api_alerts = api_response['Alerts']
API_ALERTS.write(list({k:v} for k,v in api_alerts.items())[0])
STEP2.write('The Information we want sits inside the "alert" branches of the hierarchy')

STEP3 = st.container()
STEP3.subheader('Transform API Data')
STEP3.write('Objective: Convert the API data into a dataframe')
STEP3.write('The alerts data is what we want but its not really usable as a complex hierarchy.') 
STEP3.write('lets convert the data into a dataframe and pull the bits we want.') 
STEP3.write('We going to need something more complicated than simple list comprehension...') 

STEP3.write('First lets create the container for the dataframe in the form of a dictionary') 
df_header = ['alert_id', 'start', 'end', 'effect', 'cause', 'url','routeId', 'directionId']
df_container = controller.DF_Container(df_header)
DF_ASDICT = STEP3.expander('Dataframe Container')
DF_ASDICT.write(df_container)

STEP3.write('Now we can fill the dataframe by traversing the API Data') 
STEP3.write('Theres a 1:many relationship between the alerts and the routs that are impacted')
df_container = controller.DF_Populate(api_alerts,df_container)
df = pd.DataFrame.from_dict(df_container)   
STEP3.write(df)







#def UNPICKLE_JSON(Container):
#    try:
#        st.session_state['API_JSON'] = controller.Unpickle_JSON()
#        Container.write(str(st.session_state['API_JSON']))
#    except Exception as e:
#        Container.error(e)
#JSON_SAMPLE.button('SHOW ME!', on_click=UNPICKLE_JSON, args=(JSON_SAMPLE, ))












