import random
class Game:
    
    def get_user_item(self):
        while True:
            entrer_utilisateur = input("Entrez votre choix (pierre, feuille, ciseaux): ")
            if entrer_utilisateur in ["pierre", "feuille", "ciseaux"]:
                return entrer_utilisateur
            print("Choix invalide. Veuillez réessayer.")
    
    def get_computer_item(self):
        return random.choice(["pierre", "feuille", "ciseaux"])
    
    
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "pierre" and computer_item == "ciseaux") or \
             (user_item == "feuille" and computer_item == "pierre") or \
             (user_item == "ciseaux" and computer_item == "feuille"):
            return "Win"
        else:
            return "loss"
        
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        game_result = self.get_game_result(user_item, computer_item)
        print(f"You selected {user_item}. The computer selected {computer_item}. You {game_result}!") # “You selected paper. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew"
        return game_result