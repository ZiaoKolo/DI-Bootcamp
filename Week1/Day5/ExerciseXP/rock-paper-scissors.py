from game import Game

def get_user_menu_choice():
    while True:
        try:
            choix = int(input("Entrez votre choix(1 : Jouer une nouvelle partie , 2 : Afficher les scores , 3 : Quitter) : "))
            if choix in [1, 2, 3]:
                return choix
            print("Choix invalide. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

def print_results(results):
    print(f"Résultats : {results['win']} victoires, {results['loss']} défaites, {results['draw']} matchs nuls")
    print("Merci pour votre participation !")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        entrer_utilisateur = get_user_menu_choice()
        if entrer_utilisateur == 1:
            game_result = game.play()
            results[game_result] += 1
        elif entrer_utilisateur == 2:
            print_results(results)
        elif entrer_utilisateur == 3:
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

game = Game()
main()