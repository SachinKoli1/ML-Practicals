from sklearn.linear_model import LinearRegression
import numpy as np

age=np.array([[1],[2],[3],[4],[5]])
speed=np.array([120,110,100,90,80])

model=LinearRegression()
model.fit(age,speed)

print(f"Coefficient {model.coef_}")
print(f"Intercept {model.intercept_}")

# The coefficient (or slope) of the model tells us how much the speed of the car changes when the car's age increases by one year.
# The intercept is the value of car speed when the car’s age is zero (where the line crosses the speed axis).