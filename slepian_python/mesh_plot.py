from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d


def plot_mesh(vertices, f_index, f_colors, title="The Panther"):
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

    pc = art3d.Poly3DCollection(vertices[f_index],
                                facecolors=colors)

    ax.add_collection(pc)
    ax.set_xlim(-.5,.5)
    ax.set_ylim(-.5,.5)
    ax.set_zlim(0.2,.8)
    ax.set_title(title)
    ax.axis('off')

    ax.view_init(0, -136)
    plt.show()


def slepian_filterexample(vertices, f_index, graphsig, figsize=(20,20)):
    """
    Information:
    ------------
    Plot 4 mesh given vertices and faces and computed slepian vectors

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

    fig = plt.figure(figsize=figsize)
    colorings = [graphsig[:,i][f_index].mean(axis=1) for i in range(graphsig.shape[1])]

    for i in range(4):
        ax = fig.add_subplot(2,2,i+1, projection="3d")

        # convert slepians eigenvectors into face coloring 
        # by averaging vertex signal for a face
        coloring = colorings[i]
        m, M = np.min(coloring), np.max(coloring)
        
        norm = plt.Normalize(m, M)
        colors = plt.cm.jet(norm(coloring))

        pc = art3d.Poly3DCollection(vertices[f_index], facecolors=colors)
        
        ax.add_collection(pc)
        ax.set_xlim(-.5,.5)
        ax.set_ylim(-.5,.5)
        ax.set_zlim(0.2,.8)
        
        ax.view_init(0, -136)

        ax.axis('off')
    plt.show()

def lowfreq_9mesh(vertices, f_index, graphsig, scores, figsize=(20,20), bold=None):
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
    fig = plt.figure(figsize=figsize)
    colorings = [graphsig[:,i][f_index].mean(axis=1) for i in range(graphsig.shape[1])]
    BOLDS = [None, None, None]
    if not (bold is None):
        BOLDS[bold] = 'bold'


    for i in range(9):
        ax = fig.add_subplot(3,3,i+1, projection="3d")

        # convert slepians eigenvectors into face coloring 
        # by averaging vertex signal for a face
        coloring = colorings[i]
        if (lbda[i] < 1e-7):
            m, M = np.min(colorings), np.max(colorings)
        else:
            m, M = np.min(coloring), np.max(coloring)
        norm = plt.Normalize(m, M)
        colors = plt.cm.jet(norm(coloring))

        pc = art3d.Poly3DCollection(vertices[f_index], facecolors=colors)
        
        ax.add_collection(pc)
        ax.set_xlim(-.5,.5)
        ax.set_ylim(-.5,.5)
        ax.set_zlim(0.2,.8)
        
        ax.view_init(0, -136)
        
        ax.text2D(.8, 0.3, "λ={}".format(lbda[i]), transform=ax.transAxes, fontsize=12,
                bbox=dict(facecolor='white', alpha=1, edgecolor='black', linewidth=0.2, boxstyle='square'), weight=BOLDS[0])
        ax.text2D(.8, 0.25, "μ={}".format(conc[i]), transform=ax.transAxes, fontsize=12,
                bbox=dict(facecolor='white', alpha=1, edgecolor='black', linewidth=0.2, boxstyle='square'), weight=BOLDS[1])
        ax.text2D(.8, 0.2, "ξ={}".format(cut[i]), transform=ax.transAxes, fontsize=12,
                bbox=dict(facecolor='white', alpha=1, edgecolor='black', linewidth=0.2, boxstyle='square'), weight=BOLDS[2])
        ax.axis('off')
    plt.show()