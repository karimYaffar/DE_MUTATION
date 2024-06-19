import matplotlib.pyplot as plt

def generar_boxplot(soluciones_reflex, soluciones_ABC, nombre_archivo):
    data = [soluciones_reflex, soluciones_ABC]
    labels = ['DE Reflex', 'DE ABC']

    plt.boxplot(data, patch_artist=True, labels=labels)
    plt.xlabel('Mejor Fitness')
    plt.title('Comparación de DE Reflex y DE ABC')
    plt.grid(True)
    plt.savefig(nombre_archivo)  # Guardar el boxplot como imagen
    plt.show()




def plot_box_plot(data, problema, restriccion):
    # Crear un box plot con los datos recolectados
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.boxplot(data.values())
    
    ax.set_xticklabels(data.keys(), fontsize=10)
    plt.suptitle('Comparación de Estrategias de Mutación (Fitness)', size=20, color='blue')
    ax.set_title(f'Problema: {problema}, Restricción de límite: {restriccion}', fontsize=12, color='gray')
    ax.set_ylabel('Fitness')
    ax.set_xlabel('Estrategias de Mutación')

    plt.show()
