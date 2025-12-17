# rate_limiter.py
# Simple Rate Limiter using time window logic

import time

MAX_REQUESTS = 5       # allowed attempts
TIME_WINDOW = 30       # seconds

requests = {}

def is_allowed(user):
    current_time = time.time()

    if user not in requests:
        requests[user] = []

    # keep only recent requests
    requests[user] = [
        t for t in requests[user]
        if current_time - t < TIME_WINDOW
    ]

    if len(requests[user]) >= MAX_REQUESTS:
        return False

    requests[user].append(current_time)
    return True


if __name__ == "__main__":
    print("🚦 Rate Limiter Demo")
    print("--------------------")

    user = input("Enter username: ")

    while True:
        action = input("Press Enter to make request (q to quit): ")
        if action.lower() == "q":
            break

        if is_allowed(user):
            print("✅ Request allowed")
        else:
            print("❌ Rate limit exceeded. Try later.")
