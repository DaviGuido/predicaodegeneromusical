from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import uvicorn
from fastapi.middleware.cors import CORSMiddleware 

model = joblib.load("model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

app = FastAPI()

origins = [
    "http://localhost",  
    "http://localhost:8000",  
    "http://localhost:8080",  
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class MusicInput(BaseModel):
    letra: str  

@app.post("/predict")
async def predict(data: MusicInput):
    letra = data.letra
    if not letra:
        raise HTTPException(status_code=400, detail="A letra da música não pode estar vazia.")
    
    letra_transformed = vectorizer.transform([letra])
    
    genero_predito = model.predict(letra_transformed)[0]
    
    return {"genero": genero_predito}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
