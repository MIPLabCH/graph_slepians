from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d


def plot_mesh(vertices, f_index, f_colors, title="The Bear"):
    """
    Information:
    ------------
    Plot 1 mesh given vertices and faces and faces colors

    Parameters
    ----------    
    vertices::[2darray<float>]
        Vertex positions in 3d
    f_index ::[2darray<int>]
        array of faces with faces being 3 vertices' index in vertices array
    f_colors::[1darray<float>]
        color to faces

    Returns
    -------
    None
    """

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    norm = plt.Normalize(f_colors.min(), f_colors.max())
    colors = plt.cm.viridis(norm(f_colors))

    # pc = art3d.Poly3DCollection(indexed_pts[faces_index],
    #                             facecolors=colors, edgecolor="blue")
    pc = art3d.Poly3DCollection(vertices[f_index],
                                facecolors=colors)

    ax.add_collection(pc)
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(0,1.5)
    ax.set_title(title)

    plt.show()

def lowfreq_9mesh(vertices, f_index, graphsig, scores):
    """
    Information:
    ------------
    Plot 9 mesh given vertices and faces and computed slepian vectors

    Parameters
    ----------    
    vertices::[2darray<float>]
        Vertex positions in 3d
    f_index ::[2darray<int>]
        array of faces with faces being 3 vertices' index in vertices array
    graphsig::[1darray<float>]
        usually slepian vector
    scores  ::[list]
        lambda, concentration, cut
    Returns
    -------
    None
    """

    lbda, conc, cut = scores
    fig = plt.figure(figsize=(25,25))

    for i in range(9):
        ax = fig.add_subplot(3,3,i+1, projection="3d")

        # convert slepians eigenvectors into face coloring 
        # by averaging vertex signal for a face
        coloring = graphsig[:,i][f_index].mean(axis=1)
        norm = plt.Normalize(coloring.min(), coloring.max())
        colors = plt.cm.Spectral(norm(coloring))

        pc = art3d.Poly3DCollection(vertices[f_index],facecolors=colors)
        
        ax.add_collection(pc)
        ax.set_xlim(-1,1)
        ax.set_ylim(-1,1)
        ax.set_zlim(0,1.5)
        ax.text2D(.8, 0.7, "λ={}".format(lbda[i]), transform=ax.transAxes, fontsize=12,
                bbox=dict(facecolor='white', alpha=1, edgecolor='black', linewidth=0.2, boxstyle='square'))
        ax.text2D(.8, 0.65, "μ={}".format(conc[i]), transform=ax.transAxes, fontsize=12,
                bbox=dict(facecolor='white', alpha=1, edgecolor='black', linewidth=0.2, boxstyle='square'))
        ax.text2D(.8, 0.6, "ξ={}".format(cut[i]), transform=ax.transAxes, fontsize=12,
                bbox=dict(facecolor='white', alpha=1, edgecolor='black', linewidth=0.2, boxstyle='square'))

    plt.show()
