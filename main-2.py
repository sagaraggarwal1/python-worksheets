#project1:-

# import numpy as np

# # Load CSV safely (skip header row)
# data = np.genfromtxt("sensor_data/sensor_data.csv", delimiter=",", skip_header=1)

# time = data[:, 0]
# temperature = data[:, 1]
# distance = data[:, 2]
# battery = data[:, 3]

# avg_temp = np.mean(temperature)
# min_temp = np.min(temperature)
# max_temp = np.max(temperature)

# avg_dist = np.mean(distance)
# min_dist = np.min(distance)
# max_dist = np.max(distance)

# avg_batt = np.mean(battery)
# min_batt = np.min(battery)
# max_batt = np.max(battery)

# time_max_temp = time[np.argmax(temperature)]
# low_batt_count = np.sum(battery < 30)

# results = [
#     ["Sensor", "Average", "Minimum", "Maximum"],
#     ["Temperature", avg_temp, min_temp, max_temp],
#     ["Distance", avg_dist, min_dist, max_dist],
#     ["Battery", avg_batt, min_batt, max_batt],
#     ["Time of Max Temp", time_max_temp, "-", "-"],
#     ["Battery < 30 count", low_batt_count, "-", "-"]
# ]

# results = np.array(results, dtype=str)

# np.savetxt("sensor_data/processed_results.csv", results, fmt="%s", delimiter=",")

# print("Processing complete. Results saved to sensor_data/processed_results.csv")
