from transformacoes import translate, plot_points, setup
import matplotlib.pyplot as plt

P = [(2, 3)]
Pp = translate(P, 4, -2)  # esperado: (6, 1)

print("Ex1 - P original:", P)
print("Ex1 - P' após translação (4, -2):", Pp.tolist())

fig, ax = plt.subplots()
plot_points(ax, P, "Original")
plot_points(ax, Pp, "Transladado")
setup(ax, "Ex1: Translação simples")
plt.show()
