# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "App is running and being monitored!"
#
# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template
from monitor import get_metrics
from predict import forecast_traffic
from decision import decide_scaling
from executor import execute_action
from logger import log_to_csv
from anomaly import detect_anomaly

app = Flask(__name__)

# Dummy historical data for anomaly detection
request_history = [1000 + i * 5 + (-1)**i * 80 for i in range(60)]

@app.route("/")
def home():
    metrics = get_metrics()
    cpu = metrics["cpu"]
    requests = metrics["requests"]
    is_anomaly = detect_anomaly(request_history, requests)
    predicted = forecast_traffic(show_plot=False)
    decision = decide_scaling(cpu, predicted)
    execute_action(decision)
    log_to_csv(cpu, requests, predicted, decision, is_anomaly)
    return render_template("index.html",
                           cpu=cpu,
                           requests=requests,
                           predicted=round(predicted, 2),
                           decision=decision,
                           is_anomaly=is_anomaly)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
