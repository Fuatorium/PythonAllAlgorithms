from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

def voronoi_diagram(points):
    vor = Voronoi(points)
    fig = voronoi_plot_2d(vor)
    plt.show()

if __name__ == "__main__":
    points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
    voronoi_diagram(points)
