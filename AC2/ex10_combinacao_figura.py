from transformacoes import translate, scale, reflect, plot_polygon, setup
import matplotlib.pyplot as plt

A, B, C, D = (1,1), (5,1), (5,3), (1,3)
ret = [A, B, C, D]

# 1) Translação (-2, 3)
ret1 = translate(ret, -2, 3)
# 2) Escala não uniforme: sx=1.5, sy=0.5 (em torno da origem)
ret2 = scale(ret1, sx=1.5, sy=0.5)
# 3) Reflexão no eixo y
ret3 = reflect(ret2, axis="y")

print("Ex10 - Retângulo original:", ret)
print("  após T(-2,3):", ret1.tolist())
print("  após Escala (1.5, 0.5):", ret2.tolist())
print("  após Reflexão (y):", ret3.tolist())
# Resultado final esperado: A(1.5,2), B(-4.5,2), C(-4.5,3), D(1.5,3)

fig, ax = plt.subplots()
plot_polygon(ax, ret,  "Original")
plot_polygon(ax, ret1, "Após T(-2,3)")
plot_polygon(ax, ret2, "Após Escala (1.5,0.5)")
plot_polygon(ax, ret3, "Após Reflexão (y)")
setup(ax, "Ex10: Combinação (T -> S -> Reflexão)")
plt.show()
