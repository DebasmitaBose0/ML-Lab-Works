#WAP in Python to calculate Slope (m) and y-intercept (b) for a simple linear regression method for a dataset containing two features, CGPA and LPA where LPA is dependent variable and CGPA is independent variable.
#Note: The program needs to be implemented without using any Python library function and using the OLS (Ordinary Least Squares) method.
# Assignment - 1
# WAP in Python to calculate slope (m) and y-intercept (b)
# for a dataset containing two features: CGPA and LPA
# where LPA is dependent variable and CGPA is independent variable
# (Using OLS method, without any Python library function)

cgpa = []
lpa = []

# Reading dataset
file = open("placement.csv", "r")
lines = file.readlines()
file.close()

# Extracting values (skip header)
for i in range(1, len(lines)):
    row = lines[i].strip().split(",")
    cgpa.append(float(row[0]))
    lpa.append(float(row[1]))

n = len(cgpa)

# Step 1: Calculate means
sum_x = 0
sum_y = 0

for i in range(n):
    sum_x += cgpa[i]
    sum_y += lpa[i]

mean_x = sum_x / n
mean_y = sum_y / n

# Step 2: Apply OLS formula
numerator = 0
denominator = 0

for i in range(n):
    numerator += (cgpa[i] - mean_x) * (lpa[i] - mean_y)
    denominator += (cgpa[i] - mean_x) ** 2

m = numerator / denominator   # slope

# Step 3: Calculate intercept
b = mean_y - m * mean_x

print("Slope (m):", m)
print("Y-intercept (b):", b)

# Final Equation
print("Final Equation: Y =", m, "X +", b)