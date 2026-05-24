"""
Module pour dessiner visuellement les cercles triés avec Turtle.

Ce script importe la classe Circle de challenge.py et utilise le module
turtle de Python pour afficher les cercles à l'écran.
"""

import turtle
from challenge import Circle


def draw_sorted_circles(circles, scale=20, spacing=80):
    """
    Dessine une liste de cercles triés par ordre croissant de rayon.
    
    Args:
        circles (list): Liste d'objets Circle à dessiner.
        scale (float): Facteur d'échelle (pixels par unité de rayon). Par défaut: 20.
        spacing (float): Espacement horizontal entre les cercles. Par défaut: 80.
    
    La fenêtre Turtle s'affiche avec les cercles dessinés avec leurs rayons
    en labels sous chaque cercle. Cliquez sur la fenêtre pour la fermer.
    """
    if not circles:
        print("Aucun cercle à dessiner.")
        return
    
    # Tri des cercles
    sorted_circles = sorted(circles)
    
    # Configuration de l'écran Turtle
    screen = turtle.Screen()
    screen.setup(width=1000, height=600)
    screen.title("Cercles triés par rayon")
    screen.bgcolor("white")
    
    # Création de la tortue de dessin
    t = turtle.Turtle()
    t.hideturtle()
    t.speed('fastest')
    
    # Position de départ (centré horizontalement)
    num_circles = len(sorted_circles)
    start_x = -(num_circles - 1) * spacing / 2
    y = 0
    
    # Couleurs pour varier l'apparence (cycle de couleurs)
    colors = ["red", "blue", "green", "orange", "purple", "brown", "pink", "cyan"]
    
    for i, circle in enumerate(sorted_circles):
        x = start_x + i * spacing
        radius_pixels = circle.radius * scale
        color = colors[i % len(colors)]
        
        # Dessiner le cercle
        t.penup()
        t.goto(x, y - radius_pixels)  # Position au bas du cercle
        t.pendown()
        t.pencolor(color)
        t.pensize(2)
        t.circle(radius_pixels)
        
        # Ajouter le label (rayon)
        t.penup()
        t.goto(x, y - radius_pixels - 30)
        t.pencolor("black")
        t.write(f"r = {circle.radius:.1f}", align="center", font=("Arial", 10, "normal"))
    
    # Instruction de fermeture
    t.penup()
    t.goto(0, -250)
    t.pencolor("gray")
    t.write("Cliquez pour fermer", align="center", font=("Arial", 12, "normal"))
    
    # Attendre un clic pour fermer
    screen.exitonclick()


if __name__ == "__main__":
    # Créer quelques cercles de test
    circles = [
        Circle(1),
        Circle(2.5),
        Circle(0.8),
        Circle(3),
        Circle(1.5),
    ]
    
    print("=== Cercles créés ===")
    for i, c in enumerate(circles, 1):
        print(f"{i}. {c}")
    
    print("\n=== Tri des cercles ===")
    sorted_circles = sorted(circles)
    print("Rayons triés:", [f"{c.radius:.1f}" for c in sorted_circles])
    
    print("\nDessin des cercles triés avec Turtle...")
    draw_sorted_circles(circles)
