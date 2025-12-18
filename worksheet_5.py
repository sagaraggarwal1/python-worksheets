#sagar aggarwal 1024230105 

# Q1
import numpy as np
from scipy import stats

arr = np.random.rand(20)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Variance:", np.var(arr))


# Q2
from scipy.fftpack import fft2

arr2d = np.random.rand(4, 4)
print("2D FFT:\n", fft2(arr2d))


# Q3
from scipy import linalg

A = np.array([[4, 2], [3, 1]])
print("Determinant:", linalg.det(A))
print("Inverse:\n", linalg.inv(A))
print("Eigenvalues:", linalg.eigvals(A))


# Q4
from scipy.interpolate import interp1d

x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2, 1, 3, 2])
f = interp1d(x, y, kind='cubic')
x_new = np.linspace(0, 4, 50)
print("Interpolated Values:\n", f(x_new))


# Q5
from scipy.signal import butter, filtfilt

t = np.linspace(0, 1, 100)
signal = np.sin(2*np.pi*5*t) + np.random.normal(0, 0.5, 100)
b, a = butter(2, 0.2)
filtered_signal = filtfilt(b, a, signal)
print("Filtered Signal:\n", filtered_signal)


# Q6
sales = np.random.randint(1000, 5000, (12, 4))
total_sales = np.sum(sales)
avg_sales = np.mean(sales)
max_sales = np.max(sales)
min_sales = np.min(sales)
monthly_sales = np.sum(sales, axis=1)
print("Total Sales:", total_sales)
print("Average Sales:", avg_sales)
print("Maximum Sales:", max_sales)
print("Minimum Sales:", min_sales)
print("Best Month:", np.argmax(monthly_sales) + 1)
print("Worst Month:", np.argmin(monthly_sales) + 1)


# Q7
marks = np.array([
    [85, 78, 92, 88],
    [79, 82, 74, 90],
    [90, 85, 89, 92],
    [66, 75, 80, 78],
    [70, 68, 75, 85]
])
total = np.sum(marks, axis=1)
average = np.mean(marks, axis=1)
print("Total Marks:", total)
print("Average Marks:", average)
print("Top Performer Index:", np.argmax(total))
print("Bottom Performer Index:", np.argmin(total))
print("Passing Percentage:", np.sum(average >= 40) / len(average) * 100)


# Q8
from scipy.optimize import curve_fit

time = np.array([0, 1, 2, 3, 4, 5])
velocity = np.array([2, 3.1, 7.9, 18.2, 34.3, 56.2])

def quadratic(t, a, b, c):
    return a*t**2 + b*t + c

params, _ = curve_fit(quadratic, time, velocity)
print("Curve Fit Parameters (a, b, c):", params)


# Q9
import matplotlib.pyplot as plt

plt.bar(["Arin","Aditya","Chirag","Gurleen","Kunal"], average)
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Average Marks of Students")
plt.show()


# Q10
t_fit = np.linspace(0, 5, 100)
v_fit = quadratic(t_fit, *params)
plt.plot(time, velocity, 'o', label="Original Data")
plt.plot(t_fit, v_fit, label="Fitted Curve")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.legend()
plt.grid()
plt.show()


# Q11
from scipy.stats import pearsonr

years = np.array([2000, 2005, 2010, 2015, 2020])
population = np.array([50, 55, 70, 80, 90])

corr, _ = pearsonr(years, population)
f_pop = interp1d(years, population)
print("Pearson Correlation:", corr)
print("Estimated Population in 2008:", f_pop(2008))

plt.plot(years, population, 'o-')
plt.xlabel("Year")
plt.ylabel("Population (Thousands)")
plt.show()


# Q12
coeff = [3, -5, 2, -8]
roots = np.roots(coeff)
x_val = np.linspace(-3, 3, 200)
y_val = 3*x_val**3 - 5*x_val**2 + 2*x_val - 8

plt.plot(x_val, y_val)
plt.scatter(roots.real, np.zeros_like(roots.real))
plt.show()
print("Roots:", roots)


# Q13
sizes = [200, 400, 600, 800, 1000]
times = []
for s in sizes:
    text = ''.join(random.choices(string.ascii_lowercase, k=s*1000))
    start = time.time()
    text.upper()
    times.append(time.time() - start)

plt.plot(sizes, times)
plt.xlabel("File Size (MB)")
plt.ylabel("Time (seconds)")
plt.show()


# Q14
f = lambda x: x**4 - 3*x**3 + 2
res = minimize_scalar(f)
x_plot = np.linspace(-2, 3, 200)
plt.plot(x_plot, f(x_plot))
plt.scatter(res.x, f(res.x))
plt.show()
print("Local Minima at x =", res.x)


# Q15
from scipy.integrate import odeint

def system(y, t):
    theta, omega = y
    return [omega, -0.2*omega - theta]

t = np.linspace(0, 20, 400)
solution = odeint(system, [1, 0], t)
theta = solution[:, 0]

plt.plot(t, theta)
plt.xlabel("Time (s)")
plt.ylabel("Theta (rad)")
plt.show()

print("Max Displacement:", np.max(theta))
print("Time at Max Displacement:", t[np.argmax(theta)])
