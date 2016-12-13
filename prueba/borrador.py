'''
Created on Nov 10, 2016

@author: seiscomp
'''

from obspy.clients.fdsn import Client
import os
import sys
'''
Parametros configurables

'''
servidorFDSN='apps.igepn.edu.ec'
puerto='8080'

start='2016-09-06T00::00'
end='2016-11-10T00:00:00'
latitude='-0.472'
longitude='-81.848'
minRadius='0.0'
maxRadius='2.744'

def getCatalogo():
    try:
        cliente=Client("http://%s:%s" %(servidorFDSN,puerto))
        try:
            catalogo=cliente.get_events(orderby='time-asc',starttime=start,endtime=end,latitude=latitude,longitude=longitude,minradius=minRadius,maxradius=maxRadius)
            if catalogo:
                return catalogo
            else:
                return None
        except Exception,e:
                print(str(e))
    except Exception ,e:
        print(str(e))
    pass


##test 

calogoDB=[]

catalogo=None

catalogo=getCatalogo()

archivo=open('/home/seiscomp/igAftershocks.txt','w')
if catalogo:
    for evento in catalogo:
        
        if evento['event_type'] == "earthquake" and evento['preferred_magnitude_id'] != None :
            #print evento
            #'''
            eventID = '%s' %evento['resource_id']
            diccionaryEvent={}

            diccionaryEvent={
                 'eventID':'%s' %eventID[12:],
                 'latitude':'%s' %evento.origins[0]['latitude'],
                 'longitude':'%s' %evento.origins[0]['longitude'],
                 'description':'%s' %evento.event_descriptions[0]['text'],
                 'magVal': '%s' %evento.magnitudes[0]['mag'],
                 'magType': '%s' %evento.magnitudes[0]['magnitude_type'],
                 'time': '%s' %evento.origins[0]['time'],
                 'depth': '%s' %evento.origins[0]['depth'],
                 'status':'%s' %evento.origins[0]['evaluation_mode'],
                 'phasesCount': '%s' %evento.origins[0]['quality']['associated_phase_count'],
                 'magnitudesCount':'%s' %evento.magnitudes[0]['station_count']
                 }
            #'''

            '''
            print ('%s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' %( diccionaryEvent['eventID'] ,diccionaryEvent['time'],diccionaryEvent['latitude'],
                                             diccionaryEvent['longitude'], diccionaryEvent['depth'],diccionaryEvent['magType'],diccionaryEvent['magVal'],
                                             diccionaryEvent['description'],diccionaryEvent['phasesCount'],diccionaryEvent['magnitudesCount']
                                             ))
            '''
            #'''
            archivo.write('%s | %s | %s | %s | %s | %s | %s | %s | %s | %s \n' %( diccionaryEvent['eventID'] ,diccionaryEvent['time'],diccionaryEvent['latitude'],
                                             diccionaryEvent['longitude'], diccionaryEvent['depth'],diccionaryEvent['magType'],diccionaryEvent['magVal'],
                                             diccionaryEvent['description'],diccionaryEvent['phasesCount'],diccionaryEvent['magnitudesCount']
                                             ))
            #'''







