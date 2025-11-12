from transformacoes import scale, plot_polygon, setup
import matplotlib.pyplot as plt

A, B, C = (1,1), (3,1), (2,4)
tri = [A, B, C]
tri2 = scale(tri, sx=2, sy=0.5)

print("Ex3 - Triângulo original:", tri)
print("Ex3 - Após escala não uniforme (sx=2, sy=0.5):", tri2.tolist())

fig, ax = plt.subplots()
plot_polygon(ax, tri, "Original")
plot_polygon(ax, tri2, "sx=2, sy=0.5")
setup(ax, "Ex3: Escala não uniforme")
plt.show()
