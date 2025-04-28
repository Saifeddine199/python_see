from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser les appels du frontend React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # à restreindre plus tard
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to OP Monitoring API"}
