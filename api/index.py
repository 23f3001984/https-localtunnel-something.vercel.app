from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/email")
def get_email():
    return JSONResponse({
        "email": "23f3001984@ds.study.iitm.ac.in"
    })

# Vercel handler
handler = app