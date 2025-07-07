import random

def get_metrics():
    # Simulated metrics
    return {
        "cpu": random.randint(20, 90),
        "requests": random.randint(500, 3000)
    }
