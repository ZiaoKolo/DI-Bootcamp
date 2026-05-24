from game import Game

def get_user_menu_choice():
    choix = int(input("Entrez votre choix(1 : Jouer une nouvelle partie , 2 : Afficher les scores , 3 : Quitter) : "))
    return choix

def print_results(results):
    print(f"Résultats : {results['win']} victoires, {results['loss']} défaites, {results['draw']} matchs nuls")
    print("Merci pour votre participation !")

def main():
    while True:
        entrer_utilisateur = get_user_menu_choice()
        if entrer_utilisateur == 1:
            game.play()
        elif entrer_utilisateur == 2:
            print_results(game.get_results())
        elif entrer_utilisateur == 3:
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

game = Game()
main()