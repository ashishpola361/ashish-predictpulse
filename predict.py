import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# def forecast_traffic():
#     minutes = list(range(60))
#     traffic = [1000 + np.sin(i/6)*300 + np.random.randint(-100,100) for i in minutes]
#
#     model = LinearRegression()
#     model.fit(np.array(minutes).reshape(-1,1), traffic)
#
#     future = list(range(60,70))
#     prediction = model.predict(np.array(future).reshape(-1,1))
#
#     plt.plot(minutes, traffic, label="Past Traffic")
#     plt.plot(future, prediction, label="Predicted", linestyle="--")
#     plt.legend()
#     plt.title("Traffic Forecast")
#     plt.xlabel("Minutes")
#     plt.ylabel("Requests")
#     plt.show(block=False)
#
#     return prediction[-1]
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def forecast_traffic(show_plot=False):
    minutes = np.arange(60)
    traffic = [1000 + np.sin(i/6)*300 + np.random.randint(-100, 100) for i in minutes]

    model = LinearRegression()
    model.fit(minutes.reshape(-1, 1), traffic)

    future = np.arange(60, 70)
    prediction = model.predict(future.reshape(-1, 1))

    if show_plot:
        plt.plot(minutes, traffic, label="Past Traffic")
        plt.plot(future, prediction, linestyle="--", label="Forecast")
        plt.title("Traffic Forecast")
        plt.xlabel("Minutes")
        plt.ylabel("Requests")
        plt.legend()
        plt.tight_layout()
        plt.savefig("traffic_plot.png")
        plt.show(block=False)
        import time
        time.sleep(3)

    return prediction[-1]

