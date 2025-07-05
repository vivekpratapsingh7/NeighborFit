## Manual Test Cases
| Input Example                      | Expected Outcome                     |
|-----------------------------------|--------------------------------------|
| Safety 9, Rent 10000              | 0-1 matches or "No results" message  |
| Safety 5, Rent 20000, Parks 7     | Top 5 ranked neighborhoods           |

## Edge Cases
- [x] No matching results
- [x] Extremely low/high weights
- [x] Missing input handling (frontend)

## Validations
- Match scores correctly reflect preferences
- Consistent results across refresh
