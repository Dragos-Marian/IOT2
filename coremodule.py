import time
import random
#import json
#import database as db
#import plotly as py
#import plotly.graph_objs as go
#from firebase import firebase

FEVER_START='FEVER_FEVER_START'
FEVER_END='FEVER_END_EVENT'
FEVER_THRESHOLD=37.2
NO_OF_TEMP=10
SLEEP_DURATION=30
SIMULATION_MODE=True


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

def handleFever(temperature):
    # print(temperature)
    if temperature > FEVER_THRESHOLD and handleFever.previousFever < NO_OF_TEMP:
        writeInFirebase(FEVER_START)
        # print(FEVER_START)
        AcceptValues=1
        writeInPlotly(temperature,AcceptValues) 
        handleFever.started=1        
        handleFever.previousFever = 1
        return

    if  handleFever.previousFever == NO_OF_TEMP and handleFever.started==1:
        writeInFirebase(FEVER_END) 
        # print(FEVER_END)
        AcceptValues=0
        writeInPlotly(temperature,AcceptValues)
        handleFever.previousFever = 0
        handleFever.started=0
        return

    if  handleFever.previousFever < NO_OF_TEMP and temperature <= FEVER_THRESHOLD and handleFever.started==1:
        AcceptValues=1
        writeInPlotly(temperature,AcceptValues)
        handleFever.previousFever += 1
    else:
        handleFever.previousFever=0     


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
    handleFever.previousFever = 0
    handleFever.started=0
    while True:
	temperature = random.uniform(37,42)
	print(temperature)
	#handleFever(temperature)
	#time.sleep(SLEEP_DURATION)

if __name__ == "__main__":
    main()








