from transformacoes import reflect, plot_points, setup
import matplotlib.pyplot as plt

P = [(2,5)]
Pp = reflect(P, axis="y")  # esperado: (-2,5)

print("Ex6 - P original:", P)
print("Ex6 - P' após reflexão no eixo y:", Pp.tolist())

fig, ax = plt.subplots()
plot_points(ax, P, "Original")
plot_points(ax, Pp, "Refletido (y)")
setup(ax, "Ex6: Reflexão (ponto)")
plt.show()
