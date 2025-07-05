## Overview
A **weighted scoring algorithm** combines multiple features:
- Safety Score
- Rent (inverse)
- Parks Score
- Walk Score

## Formula (Simplified)
match_score = (safety_score * safety_weight) +
((max_rent - rent) * rent_weight / 1000) +
(parks_score * parks_weight) +
(walk_score * walk_weight)