import matplotlib.pyplot as plt

# Define un estilo personalizado con las configuraciones deseadas
custom_style = {
    'figure.figsize': (10, 18),
    'figure.subplot.left': 0.091,
    'figure.subplot.bottom': 0.674,
    'figure.subplot.right': 0.985,
    'figure.subplot.top': 0.924,
    'figure.subplot.wspace': 0.498,
    'figure.subplot.hspace': 0.31,
}

plt.style.use(custom_style)  # Aplica el estilo personalizado

def generar_grafico_personalizado():
    # Crea tus gráficos aquí
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Gráfico Personalizado')
    plt.show()

# Llama a la función para generar el gráfico personalizado
generar_grafico_personalizado()
