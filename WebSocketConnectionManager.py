from fastapi import WebSocket

class WebSocketConnectionManager:
    def __init__(self):
        # later we need to append the list of websocket connectoins
        self.active_connections: list[WebSocket] = []
        
        
    # first we need to accept the websocket connection and we need to add to the list of the websocket connections
    async def connect(self, websocket: WebSocket):
        # accept the websocket connection which is tried to establish from the client
        await websocket.accept()
        # then we add to the list of active connections
        self.active_connections.append(websocket)
        
    
    # method for broadcasting the messages 
    #normal flow that is like senting to the individual client sent to the group of connections that contains websockets
    async def broadcast(self, text: str):
        for connection in self.active_connections:
            await connection.send_text(text)
            

    # when the websocket connection is disconnected then exeption occurs in
    # - websocket.receive_text() so we need to catch the exception and sent an broadcasting disconnection message
    
    def disconnect(self, websocket):
        self.active_connections.remove(websocket)
        