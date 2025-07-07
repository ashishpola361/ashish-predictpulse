from config import *

def decide_scaling(cpu, predicted_requests):
    if cpu > SCALE_UP_CPU_THRESHOLD or predicted_requests > SCALE_UP_REQUESTS_THRESHOLD:
        return "Scale Up"
    elif cpu < SCALE_DOWN_CPU_THRESHOLD and predicted_requests < SCALE_DOWN_REQUESTS_THRESHOLD:
        return "Scale Down"
    else:
        return "Hold"
