
     Base diagram for the broadcasting messages to entire room and connected connections(clients) connected by the handshake listen to the room and recives ntificatons


[ Terminal 1 (User 100) ]            [ FastAPI Backend ]            [ Terminal 2 (User 200) ]
            │                                  │                                  │
            │  === TERMINAL 1 CONNECTS ===    │                                  │
            ├─────── Phase 1: Handshake ──────>│                                  │
            │        (HTTP Upgrade Request)    │                                  │
            │<────── Phase 2: Accept ──────────┤                                  │
            │        (Saved to connections)    │                                  │
            │                                  │                                  │
            │                                  │  === TERMINAL 2 CONNECTS ===    │
            │                                  │<────── Phase 1: Handshake ──────┤
            │                                  │        (HTTP Upgrade Request)    │
            │                                  ├─────── Phase 2: Accept ────────>│
            │                                  │        (Saved to connections)    │
            │                                  │                                  │
            │                                  │  === BROADCAST NOTICE ===       │
            │<────── Broadcast Notification ───┤─────── Broadcast Notification ──>│
            │        "User 200 joined"         │        "User 200 joined"         │
            │                                  │                                  │
            │  === ACTIVE CHAT STREAM ===      │                                  │
            ├─────── Send: "Hello World!" ────>│                                  │
            │                                  ├─────── Broadcast Msg ───────────>│
            │<────── Broadcast Msg ────────────┤        "User 100: Hello World!"  │
            │        "User 100: Hello World!"  │                                  │



   Flow A: Broadcast (The Room Intercom 📢)When Terminal 1 sends a message and your backend calls broadcast(), the operator doesn't choose a specific destination. Instead, they pick up a megaphone and read the message aloud to every single wire plugged into the wall.
   

   Terminal 1 ──"Hello"──► [ FASTAPI OPERATOR ]
                             │
                             ├──► (Copies to Line 100) ──► Terminal 1 receives copy
                             └──► (Copies to Line 200) ──► Terminal 2 receives copy



    Flow B: Targeted / Personal (The Patch Cable 🔌) when terminal 1(id - 100)  only wants to send messages to the terminal 2(id - 200) terminal 1 sends the data with key to the fastapi operator and performs a lookup for the terminal with key - 200 and send personally or whispers to them the data

    Terminal 1 ──"Secret"──► [ FASTAPI OPERATOR ]
                              │
                              └──► (Looks up 200) ──► Terminal 2 receives message only



code flow - 
await websocket(from WebSocket).accept() - it is used to accept connection from the client to server 
   -> it is because when a client tries to connect to websocket endpoint the the server needs to accept to establish websocket connection

while true:  - we opens an infinite loop because to keep the connection persistent open

data  = await websocket.receive_text() -> first The server pauses here and waits for the client to send a message as text. it returns the data that is send by the client in an websocket connected session 

await websocket.send_text(f"the response received {data}") -> send we send the received text to the sended client