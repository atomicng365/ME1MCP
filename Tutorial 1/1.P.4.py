#%%
"""Compute surface area vs radius for a capsule-like shape and plot the result.

This file now wraps the logic in a main() function and handles headless
environments by switching to the 'Agg' backend and saving the figure to
`1.P.4_plot.png` if no display is available. In environments with a GUI
display, plt.show() will still be called so the plot appears.
"""
import os
import matplotlib
import matplotlib.pyplot as plt

r1 = []
h1 = []
V1 = []
A1 = []
PI = 3.141592654

def Vol(h, r):
    V = PI * (h - 2 * r) * r ** 2 + PI * r ** 3 * 4 / 3
    return V

def SA(h, r):
    A = PI * (h - 2 * r) * r * 2 + 4 * PI * r ** 2
    return A


def main(save_if_headless=True):
    # If no DISPLAY (common in headless containers), use Agg and save the plot
    has_display = bool(os.environ.get("DISPLAY")) or os.environ.get("WAYLAND_DISPLAY")
    if not has_display and save_if_headless:
        matplotlib.use("Agg")

    r = 0.1
    h = 2 * r
    # build lists of r, h, V, A where V reaches at least 0.9
    while Vol(h, r) < 0.9:
        r = r + 0.05
        h = 2 * r
        while Vol(h, r) < 0.9:
            h = h + 0.05
        r1.append(r)
        h1.append(h)
        V1.append(Vol(h, r))
        A1.append(SA(h, r))
        h = 2 * r

    min_area = min(A1)
    min_area_index = A1.index(min_area)
    print(min_area_index)
    print("min_area_index= ", min_area_index)
    print("surface area = ", min_area)
    print("Volume", V1[min_area_index])
    print("height = ", h1[min_area_index])
    print("radius = ", r1[min_area_index])

    plt.plot(r1, A1)
    plt.xlabel("Radius,m")
    plt.ylabel("Surface Area,m^2")
    plt.title("surface area vs radius")

    # show in interactive environments; otherwise save to file
    if has_display:
        plt.show()
    else:
        out_path = os.path.join(os.path.dirname(__file__), "1.P.4_plot.png")
        plt.savefig(out_path)
        print(f"No display detected — saved plot to: {out_path}")


if __name__ == "__main__":
    main()