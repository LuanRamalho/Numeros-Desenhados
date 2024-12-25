import tkinter as tk

def draw_number(canvas, x, y, number, size=40):
    """
    Desenha um número no canvas usando coordenadas predefinidas.

    :param canvas: Canvas tkinter onde o número será desenhado
    :param x: Coordenada x superior esquerda
    :param y: Coordenada y superior esquerda
    :param number: Número a ser desenhado (0 a 9)
    :param size: Tamanho do número (escala)
    """
    # Coordenadas base para números de 0 a 9
    numbers_coords = {
        0: [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)],  # Retângulo (0)
        1: [(0.5, 0), (0.5, 1)],  # Linha vertical (1)
        2: [(0, 0), (1, 0), (1, 0.5), (0, 0.5), (0, 1), (1, 1)],  # Forma de 2
        3: [(0, 0), (1, 0), (1, 0.5), (0, 0.5), (1, 0.5), (1, 1), (0, 1)],  # Forma de 3
        4: [(0, 0), (0, 0.5), (1, 0.5), (1, 0), (1, 1)],  # Forma de 4
        5: [(1, 0), (0, 0), (0, 0.5), (1, 0.5), (1, 1), (0, 1)],  # Forma de 5
        6: [(1, 0), (0, 0), (0, 1), (1, 1), (1, 0.5), (0, 0.5)],  # Forma de 6
        7: [(0, 0), (1, 0), (1, 1)],  # Forma de 7
        8: [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0), (0, 0.5), (1, 0.5)],  # Forma de 8
        9: [(1, 1), (1, 0), (0, 0), (0, 0.5), (1, 0.5)]  # Forma de 9
    }

    coords = numbers_coords.get(number, [])
    scaled_coords = [(x + px * size, y + py * size) for px, py in coords]

    # Desenhar linhas conectando os pontos
    for i in range(len(scaled_coords) - 1):
        canvas.create_line(scaled_coords[i], scaled_coords[i + 1], width=2)

def main():
    root = tk.Tk()
    root.title("Desenhando números")

    canvas_width = 600
    canvas_height = 200
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    # Posição inicial e espaçamento entre números
    start_x = 20
    start_y = 50
    spacing = 50

    # Desenhar números de 0 a 9
    for i in range(10):
        draw_number(canvas, start_x + i * spacing, start_y, i, size=40)

    root.mainloop()

if __name__ == "__main__":
    main()
