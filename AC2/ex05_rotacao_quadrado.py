from transformacoes import rotate, plot_polygon, setup
import matplotlib.pyplot as plt

A, B, C, D = (1,1), (1,4), (4,4), (4,1)
quad = [A, B, C, D]

# Rotação de 45° no sentido horário = -45° em torno da origem
quad2 = rotate(quad, -45)

print("Ex5 - Quadrado original:", quad)
print("Ex5 - Após rotação -45° (horário, centro=origem):", quad2.tolist())
# Se quiser girar ao redor do centro do quadrado, use center=(2.5, 2.5)

fig, ax = plt.subplots()
plot_polygon(ax, quad, "Original")
plot_polygon(ax, quad2, "Rot. -45°")
setup(ax, "Ex5: Rotação quadrado (horário)")
plt.show()
