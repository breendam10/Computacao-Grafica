import numpy as np
import math
import matplotlib.pyplot as plt

# ---------- Helpers geométricos ----------
def to_np(points):
    """Converte lista de tuplas/listas [(x,y), ...] em array Nx2."""
    arr = np.asarray(points, dtype=float)
    return arr.reshape(-1, 2)

def translate(points, dx, dy):
    P = to_np(points)
    T = np.array([dx, dy], dtype=float)
    return P + T

def scale(points, sx, sy=None, center=(0.0, 0.0)):
    """Escala em torno de 'center'. sy=sx se não for passado."""
    if sy is None:
        sy = sx
    P = to_np(points)
    cx, cy = center
    P0 = P - np.array([cx, cy])
    S = np.diag([sx, sy])
    P1 = P0 @ S.T
    return P1 + np.array([cx, cy])

def rotate(points, degrees, center=(0.0, 0.0)):
    """Rotação ao redor de 'center'. CCW positivo."""
    P = to_np(points)
    theta = math.radians(degrees)
    c, s = math.cos(theta), math.sin(theta)
    R = np.array([[c, -s],
                  [s,  c]])
    cx, cy = center
    P0 = P - np.array([cx, cy])
    P1 = P0 @ R.T
    return P1 + np.array([cx, cy])

def reflect(points, axis="x"):
    """Reflexão pelos eixos: 'x', 'y' ou 'origem'."""
    P = to_np(points)
    if axis == "x":
        M = np.array([[1, 0],[0, -1]])
    elif axis == "y":
        M = np.array([[-1, 0],[0, 1]])
    elif axis == "origem":
        M = -np.eye(2)
    else:
        raise ValueError("axis deve ser 'x', 'y' ou 'origem'")
    return P @ M.T

def shear_x(points, k):
    """Cisalhamento horizontal: x' = x + k*y."""
    P = to_np(points)
    M = np.array([[1, k],
                  [0, 1]])
    return P @ M.T

# ---------- Plot helpers ----------
def plot_points(ax, pts, label, marker="o", ls="none"):
    pts = to_np(pts)
    ax.plot(pts[:,0], pts[:,1], marker=marker, ls=ls, label=label)

def plot_polygon(ax, pts, label, close=True, ls="-"):
    pts = to_np(pts)
    if close:
        pts = np.vstack([pts, pts[0]])
    ax.plot(pts[:,0], pts[:,1], ls=ls, marker="o", label=label)

def setup(ax, title=""):
    ax.axhline(0, lw=0.8, color="gray")
    ax.axvline(0, lw=0.8, color="gray")
    ax.grid(True, ls=":")
    ax.set_aspect("equal", adjustable="box")
    ax.set_title(title)
    ax.legend()
