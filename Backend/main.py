from fastapi import FastAPI, Query
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


df = pd.read_csv("data\data.csv")

@app.get("/")
def home():
    return {"message": "NeighborFit API is running"}

@app.get("/match")
def match_neighborhood(
    min_safety: int = Query(6),
    max_rent: int = Query(20000),
    min_parks: int = Query(5)
):
    filtered = df[
        (df["safety_score"] >= min_safety) &
        (df["rent"] <= max_rent) &
        (df["parks_score"] >= min_parks)
    ]
    return filtered.to_dict(orient="records")
