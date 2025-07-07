# def decide_scaling(cpu, predicted_traffic):
#     if cpu > 75 or predicted_traffic > 2500:
#         return "Scale Up"
#     elif cpu < 30 and predicted_traffic < 1200:
#         return "Scale Down"
#     else:
#         return "Hold"
from config import *

def decide_scaling(cpu, predicted_requests):
    if cpu > SCALE_UP_CPU_THRESHOLD or predicted_requests > SCALE_UP_REQUESTS_THRESHOLD:
        return "Scale Up"
    elif cpu < SCALE_DOWN_CPU_THRESHOLD and predicted_requests < SCALE_DOWN_REQUESTS_THRESHOLD:
        return "Scale Down"
    else:
        return "Hold"
