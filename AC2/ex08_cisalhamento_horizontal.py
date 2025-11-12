from transformacoes import shear_x, plot_points, setup
import matplotlib.pyplot as plt

P = [(2,3)]
Pp = shear_x(P, k=2)  # x' = x + 2*y = 8, y'=3

print("Ex8 - P original:", P)
print("Ex8 - P' após cisalhamento horizontal k=2:", Pp.tolist())

fig, ax = plt.subplots()
plot_points(ax, P, "Original")
plot_points(ax, Pp, "Shear k=2")
setup(ax, "Ex8: Cisalhamento horizontal")
plt.show()
