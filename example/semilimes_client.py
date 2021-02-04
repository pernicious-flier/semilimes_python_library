import websocket
from semilimes import semilimes

semilimes_wss_server = "wss://cloud.semilimes.net/CloudServer/wsclient"
AuthToken = "... insert here your Auth Token ..."
ReceiverID = "... insert here the Channel ID ..."

user = 0
channel = 1

try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send(semilimes.SendTxtMsg(AuthToken ,ReceiverID ,channel ,"Hello!! Python here :)"))
        time.sleep(5)        
        
        options = [["a",1],["b",2]]
        ws.send(semilimes.SendSelectOpt(AuthToken ,ReceiverID ,channel ,"Selection", options))
        time.sleep(5)        
        
        latitude = "10.8169596";
        longitude = "106.6837259";
        ws.send(semilimes.SendLocation(AuthToken, ReceiverID, channel, "Location: ", latitude, longitude))
        time.sleep(5)        
        
        
        Body = "<html> \
        <body> \
        <h1>HTML from Python</h1> \
        <p>yahooo!</p> \
        </body> \
        </html>";
        ws.send(semilimes.SendHTML(AuthToken, ReceiverID, channel, Body))
        time.sleep(5)        
        
        Body = "Pick a Date";
        ws.send(semilimes.ReceiveDate(AuthToken, ReceiverID, channel, Body))
        time.sleep(5)        
        
        Body = "Pick a Time";
        ws.send(semilimes.ReceiveTime(AuthToken, ReceiverID, channel, Body))
        time.sleep(5)        
        
        Body = "Pick a Location";
        ws.send(semilimes.ReceiveLocation(AuthToken, ReceiverID, channel, Body))
        time.sleep(60)        
        
        ws.close()
    thread.start_new_thread(run, ())
    
if __name__ == "__main__":
    #websocket.enableTrace(True) #echo the sent msgs
    ws = websocket.WebSocketApp(semilimes_wss_server,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open    
    ws.run_forever()
