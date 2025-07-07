import csv
from datetime import datetime
from config import LOG_FILE

def log_to_csv(cpu, requests, prediction, decision, anomaly=False):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [current_time, cpu, requests, round(prediction, 2), decision, "Yes" if anomaly else "No"]

    try:
        with open(LOG_FILE, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Time", "CPU (%)", "Requests", "Predicted", "Decision", "Anomaly"])
    except FileExistsError:
        pass

    with open(LOG_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)