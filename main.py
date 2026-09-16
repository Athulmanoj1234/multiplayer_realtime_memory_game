from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def welcome_intro():
    return "welcome to my realtime multiplayer application"
    
