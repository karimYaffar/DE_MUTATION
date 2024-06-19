import numpy as np
import matplotlib.pyplot as plt

def plot_radar_chart(data):
    labels = list(data.keys())
    num_vars = len(labels)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    for strategy, fitness_values in data.items():
        if len(fitness_values) < num_vars:
            fitness_values += [fitness_values[0]] * (num_vars - len(fitness_values))
        fitness_values += fitness_values[:1]  # Ensure the circle is closed
        print(f"Strategy: {strategy}, Angles: {len(angles)}, Fitness Values: {len(fitness_values)}")
        ax.plot(angles, fitness_values, linewidth=2, linestyle='solid', label=strategy)
        ax.fill(angles, fitness_values, alpha=0.1)

    ax.set_yticks([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_rlabel_position(0)
    ax.spines['polar'].set_visible(True)
    ax.grid(True)

    ax.set_title('Comparación de Estrategias de Mutación en Diferentes Problemas', size=20, color='blue', y=1.1)
    ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05), fontsize='small')

    plt.show()
