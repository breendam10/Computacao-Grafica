from transformacoes import scale, plot_polygon, setup
import matplotlib.pyplot as plt

A, B, C = (1,1), (3,1), (2,4)
tri = [A, B, C]
tri2 = scale(tri, 2)  # fator 2 sobre a origem

print("Ex2 - Triângulo original:", tri)
print("Ex2 - Após escala uniforme 2:", tri2.tolist())
print("Observação: dimensões lineares dobram; área x4.")

fig, ax = plt.subplots()
plot_polygon(ax, tri, "Original")
plot_polygon(ax, tri2, "Escala 2")
setup(ax, "Ex2: Escala uniforme (fator 2)")
plt.show()
