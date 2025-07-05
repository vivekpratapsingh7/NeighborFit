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

df = pd.read_csv("data/Data.csv")

@app.get("/match")
def match_neighborhood(
    safety_weight: float = Query(1.0),
    rent_weight: float = Query(1.0),
    parks_weight: float = Query(1.0),
    walk_weight: float = Query(1.0),
):
    df_copy = df.copy()

    
    df_copy["norm_safety"] = df_copy["safety_score"] / 10
    df_copy["norm_rent"] = 1 - (df_copy["rent"] - df_copy["rent"].min()) / (df_copy["rent"].max() - df_copy["rent"].min())
    df_copy["norm_parks"] = df_copy["parks_score"] / 10
    df_copy["norm_walk"] = df_copy["walk_score"] / 100

    # Compute weighted score
    df_copy["match_score"] = (
        safety_weight * df_copy["norm_safety"] +
        parks_weight * df_copy["norm_parks"] +
        walk_weight * df_copy["norm_walk"] +
        rent_weight * df_copy["norm_rent"]
    )

    # Sort by score
    sorted_df = df_copy.sort_values(by="match_score", ascending=False)

    
    return sorted_df.head(5)[[
        "neighborhood", "safety_score", "rent", "parks_score", "walk_score", "match_score"
    ]].to_dict(orient="records")
