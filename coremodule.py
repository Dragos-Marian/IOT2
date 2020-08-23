#!/usr/bin/env python3
import time
import random
#import json
#import database as db
#import plotly as py
#import plotly.graph_objs as go
#from firebase import firebase

FEVER_START='FEVER_FEVER_START'
FEVER_END='FEVER_END_EVENT'
FEVER_THRESHOLD=41
NO_OF_TEMP=9
SLEEP_DURATION=2
SIMULATION_MODE=True
FeverStarted=0
NrOfTemp=0


#FIREBASE_URL="https://iotproject-45a41.firebaseio.com/"
#FIREBASE_EVENTS="/iotproject-45a41/Events"
#firebase = firebase.FirebaseApplication(FIREBASE_URL,None)


#def getTimestamp():
  #  return int(time.time() * 1000)

"""
def readTemperature():
    if SIMULATION_MODE:
        temperature = random.randrange(30, 42)
    else:
        try:
            import Adafruit_DHT
        except ImportError:
            raise ImportError('Failed to import Adafruit_DHT')
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    return temperature

def writeInFirebase(event):
    timestamp = getTimestamp()
    data = {
        'Time':timestamp,
        'Event':event
    }
    firebase.post(FIREBASE_EVENTS, data)


def writeInPlotly(temperature,AcceptValues):
    timestamp = getTimestamp()
    if AcceptValues ==1:
        writeInPlotly.temp=[]
        writeInPlotly.time=[]
        writeInPlotly.temp.append(temperature)
        writeInPlotly.time.append(timestamp)

    if AcceptValues ==0:
        layout = go.Layout(
            title='Temperature events plot',
            yaxis=dict(
                title='Temperature'
                ),
            xaxis=dict(
                title='Time'
            )
        )

        data=[go.Scatter(
            x=writeInPlotly.time,
            y=writeInPlotly.temp,
            mode='lines'
            
        )]
        fig=go.Figure(data=data, layout=layout)
        py.offline.plot(fig, filename='graph.html')
"""
def TestFever(temperature):
        global NrOfTemp
        global FeverStarted	
        if NrOfTemp==NO_OF_TEMP:
	        NrOfTemp=NrOfTemp+1
	        print(NrOfTemp)
	        NrOfTemp=0
	        print(NrOfTemp)
	        print(temperature)
	        print("END")
	        #writeInFirebase(FEVER_END)
        elif temperature > FEVER_THRESHOLD:
	        NrOfTemp=0
	        FeverStarted=1
	        NrOfTemp=NrOfTemp+1
	        print( NrOfTemp)
	        print(temperature)
	        #writeInFirebase(FIVER_START)
        elif FeverStarted==1:
	        NrOfTemp=NrOfTemp+1
	        print(NrOfTemp)
	        print(temperature)
        else:
	        NrOfTemp=NrOfTemp
		

"""
def write_to_db(temperature):
    timestamp = int(time.time() * 1000)
    event = 'NONE'
    if temperature > FEVER_THRESHOLD and handleFever.previousFever < NO_OF_TEMP:
        event = FEVER_START
    elif handleFever.previousFever == NO_OF_TEMP and handleFever.started==1:
        event = FEVER_END
    # print(timestamp, temperature, event)
    conn = db.create_connection(db.DB_FILE)
    with conn:
        db.insert_row(conn, timestamp, temperature, event)


def startMonitoringTemperature():
    handleFever.previousFever = 0
    handleFever.started=0

    while True:
        temperature = readTemperature()
        write_to_db(temperature)
        handleFever(temperature)
        time.sleep(SLEEP_DURATION)

"""
def main():
    #conn = db.create_connection(db.DB_FILE)
   # with conn:
      #  db.create_db(conn)
    # startMonitoringTemperature()
    while True:
        temperature=round(random.uniform(36,42),2)
        TestFever(temperature)
        time.sleep(SLEEP_DURATION)

if __name__ == "__main__":
    main()








