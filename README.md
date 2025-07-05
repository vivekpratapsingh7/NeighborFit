# NeighborFit: Neighborhood-Lifestyle Matching App

 A full-stack web application that helps users find the best neighborhoods based on their lifestyle preferences, using real-world data, systematic research, and algorithmic matching.

---

## Problem Statement

Modern home search platforms focus on price and location, ignoring lifestyle fit. NeighborFit bridges this gap by matching people to neighborhoods based on personal priorities like safety, walkability, affordability, and amenities.

---

## Project Goals

- Identify core lifestyle-neighborhood mismatches through research
- Analyze existing platforms and their limitations
- Collect and process real-world neighborhood data
- Build an algorithm to match users with suitable neighborhoods
- Deploy a working app with documented technical decisions

---

## Research & Problem-Solving

### User Research
- Conducted interviews/surveys with X participants
- Key priorities discovered: Safety, Commute, Parks, Affordability

### Existing Solution Analysis
| Platform     | Strengths                | Gaps Identified                    |
|--------------|--------------------------|------------------------------------|
| Niche.com    | Good data visualization  | Lacks personalization              |
| Walk Score   | Accurate walkability     | No holistic lifestyle focus        |
| Zillow       | Strong for pricing       | No lifestyle indicators            |

### Hypotheses Formed
- Users prefer lifestyle fit over proximity to work
- Safety and public amenities are top-ranked features

## Matching Algorithm

### Inputs:
- User preferences (e.g. safety: high, budget: low)

### Features Considered:
- Safety Score, Rent, Parks Score, walk score.

### Method:
- Feature normalization
- Weighted scoring (user-defined)


## Tech Stack

| Layer        | Technology             |
|--------------|------------------------|          
| Frontend     | HTML + CSS + js        |
| Backend      | FastAPI                |
| Data         | Pandas                 |
| Deployment   | Render / Vercel        |
| Version Ctrl | Git + GitHub           |
