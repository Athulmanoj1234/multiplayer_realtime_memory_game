from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from WebSocketConnectionManager import WebSocketConnectionManager

app = FastAPI()

connection_manager = WebSocketConnectionManager()

@app.get("/")
def welcome_intro():
    return "welcome to my realtime multiplayer application"

#for accepting a realtime data the data should be sent to an websocket endpoint    
@app.websocket("/ws/{client_id}")
async def real_time_processing(websocket: WebSocket, client_id: int):
    # first should accept the connection reqwuests from the client
    # now we can use the helper method from the connection_manager class
    await connection_manager.connect(websocket)
    
    try:
    # should start an infinite loop that continues streaming
      while True:
        # first should receive the messege if any message is sended by the client
        # here we are only accepting text so we only used the method receive text and the received data is returned
        data = await websocket.receive_text()
        # then the received messages will be broadcasted to all connected clients 
        # now we can use the helper method to broadcast the messages ie message recieved from the client can be sent to multiple clients
        await connection_manager.broadcast(f"client - {client_id} send the message {data}")
        #   disconnection exception should be get handled 
    except WebSocketDisconnect:
        connection_manager.disconnect(websocket)
        # we need ot send the message to the all connected clients that the connected client 
        await connection_manager.broadcast(f"client - {client_id} gets disconnected from the connections")