from transformacoes import translate, rotate, scale, plot_points, setup
import matplotlib.pyplot as plt

P = [(3,2)]

# 1) translação (1, -1)
P1 = translate(P, 1, -1)
# 2) rotação 90° CCW
P2 = rotate(P1, 90)
# 3) escala uniforme fator 2
P3 = scale(P2, 2)

print("Ex9 - P:", P)
print("  após translação:", P1.tolist())
print("  após rotação 90°:", P2.tolist())
print("  após escala x2 :", P3.tolist())  # esperado final: (-2, 8)

fig, ax = plt.subplots()
plot_points(ax, P,  "Original")
plot_points(ax, P1, "Após T(1,-1)")
plot_points(ax, P2, "Após Rot90")
plot_points(ax, P3, "Após Escala2")
setup(ax, "Ex9: Composição (T -> R -> S)")
plt.show()
