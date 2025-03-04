import matplotlib.pyplot as plt
def create_logo():
    fig, ax = plt.subplots()
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Draw a circle
    circle = plt.Circle((0, 0), 1, color='white', fill=True, ec='black', lw=2)
    ax.add_patch(circle)
    
    # Add text
    ax.text(0, 0, 'ARUDRA', fontsize=20, fontweight='bold', color='red',
            ha='center', va='center', family='sans-serif')
    
    # Save and show the logo
    plt.savefig("arudra_logo.png", dpi=300, bbox_inches='tight')
    plt.show()

create_logo()

