from transformacoes import reflect, plot_polygon, setup
import matplotlib.pyplot as plt

A, B, C = (2,3), (4,3), (3,5)
tri = [A, B, C]
tri2 = reflect(tri, axis="x")  # (x, -y)

print("Ex7 - Triângulo original:", tri)
print("Ex7 - Após reflexão no eixo x:", tri2.tolist())

fig, ax = plt.subplots()
plot_polygon(ax, tri, "Original")
plot_polygon(ax, tri2, "Reflexão (x)")
setup(ax, "Ex7: Reflexão triângulo")
plt.show()
