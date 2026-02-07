"""
DEMO DATABASE MODULE

In production:
- Uses PostgreSQL
- Uses connection pooling
- Handles timezone-safe inserts

Here:
- Logic is mocked to demonstrate structure
"""

def set_user_state(user_id, team_id, state):
    print(f"[DEMO] Setting state {state} for user {user_id} in team {team_id}")

def get_user_state(user_id):
    print(f"[DEMO] Fetching state for {user_id}")
    return 1

def upsert_standup(user_id, team_id, field, text):
    print(f"[DEMO] Saving {field} for {user_id}: {text}")
