# from sklearn.ensemble import IsolationForest
# import numpy as np
#
# def detect_anomaly(data):
#     model = IsolationForest()
#     data = np.array(data).reshape(-1, 1)
#     model.fit(data)
#     return model.predict(data)  # -1 = anomaly
import numpy as np

def detect_anomaly(request_values, current_value, threshold=2.5):
    mean = np.mean(request_values)
    std = np.std(request_values)

    if std == 0:
        return False  # no variation, so can't detect anomaly

    z_score = (current_value - mean) / std
    return abs(z_score) > threshold
