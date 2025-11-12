from transformacoes import rotate, plot_points, setup
import matplotlib.pyplot as plt

P = [(1, 0)]
Pp = rotate(P, 90)

print("Ex4 - P original:", P)
print("Ex4 - P' após rotação 90° CCW:", Pp.tolist())  # esperado: (0,1)

fig, ax = plt.subplots()
plot_points(ax, P, "Original")
plot_points(ax, Pp, "Rot. 90°")
setup(ax, "Ex4: Rotação (ponto)")
plt.show()
