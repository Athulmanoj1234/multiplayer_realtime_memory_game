from fastapi import FastAPI, WebSocket


app = FastAPI()

@app.get("/")
def welcome_intro():
    return "welcome to my realtime multiplayer application"

#for accepting a realtime data the data should be sent to an websocket endpoint    
@app.websocket("/ws")
async def real_time_processing(websocket: WebSocket):
    # first should accept the connection reqwuests from the client
    await websocket.accept()
    
    # should start an infinite loop that continues streaming
    while True:
        # first should receive the messege if any message is sended by the client
        # here we are only accepting text so we only used the method receive text and the received data is returned
        data = await websocket.receive_text()
        # then the received messages will be broadcasted to all connected clients 
        await websocket.send_text(f"The received data is {data}")