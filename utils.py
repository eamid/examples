import matplotlib.pyplot as plt

def plot_results(maps, labels, index=[], extension=''):
    fig = plt.figure()
    fig.set_figheight(5)
    fig.set_figwidth(15)
    ax1 = fig.add_subplot(141); ax1.axis('off')
    ax2 = fig.add_subplot(142); ax2.axis('off')
    ax3 = fig.add_subplot(143); ax3.axis('off')
    ax4 = fig.add_subplot(144); ax4.axis('off')
    ax1.scatter(maps[0][:,0], maps[0][:,1], s=0.1, c=labels)
    ax2.scatter(maps[1][:,0], maps[1][:,1], s=0.1, c=labels)
    ax3.scatter(maps[2][:,0], maps[2][:,1], s=0.1, c=labels)
    ax4.scatter(maps[3][:,0], maps[3][:,1], s=0.1, c=labels)
    if index:
        ax1.scatter(maps[0][index,0], maps[0][index,1], s=80, c='red', marker='x')
        ax2.scatter(maps[1][index,0], maps[1][index,1], s=80, c='red', marker='x')
        ax3.scatter(maps[2][index,0], maps[2][index,1], s=80, c='red', marker='x')
        ax4.scatter(maps[3][index,0], maps[3][index,1], s=80, c='red', marker='x')
    ax1.title.set_text('t-SNE ' + extension)
    ax2.title.set_text('UMAP ' + extension)
    ax3.title.set_text('TriMap ' + extension)
    ax4.title.set_text('PCA ' + extension)
    plt.show()
