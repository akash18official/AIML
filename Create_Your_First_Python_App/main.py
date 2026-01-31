from fastapi import FastAPI
from mycode import MyProfile


app = FastAPI()
profile=MyProfile()

@app.get("/hello")
def hello():
    s=profile.viewprofile()
    return s 


