import numpy as np
import matplotlib.pyplot as plt


a = int(input(f"Введите параметр a - "))
b = int(input(f"Введите параметр b - "))
D = 4 * a**3 + 27 * b**2
if D > 0:
    print(f"D = {D}; D > 0")
elif D < 0:
    print(f"D = {D}; D < 0")
else:
    print(f"D = {D}")
print("Кривая сингулярная" if D == 0 else "Кривая не сингулярная")


x = np.linspace(-10, 10, 10000)
y = x ** 3 + a * x + b
y = np.where(y >= 0, y, np.nan)

plt.figure(figsize=(8, 6))
plt.plot(x, np.sqrt(y), color='black')
plt.plot(x, -np.sqrt(y), color='black')
plt.title('График функции $y^2 = x^3 + ax + b$')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.show()


