import tkinter as tk
import random

#  MODEL 

class GameModel:
    def __init__(self):
        self.player_hp = 20
        self.enemy_hp = 15

    def attack_enemy(self):
        dmg = random.randint(1, 6)
        self.enemy_hp -= dmg
        return dmg

    def enemy_attack(self):
        dmg = random.randint(1, 4)
        self.player_hp -= dmg
        return dmg

    def is_enemy_dead(self):
        return self.enemy_hp <= 0

    def is_player_dead(self):
        return self.player_hp <= 0


#  VIEW 

class GameView:
    def __init__(self, root):
        self.root = root
        root.title("Prosta RPG")

        self.text = tk.Label(root, text="Witaj w RPG!", font=("Arial", 14))
        self.text.pack(pady=10)

        self.btn_attack = tk.Button(root, text="Atakuj", width=20)
        self.btn_attack.pack(pady=5)

        self.btn_quit = tk.Button(root, text="Wyjście", width=20, command=root.quit)
        self.btn_quit.pack(pady=5)

    def update_text(self, msg):
        self.text.config(text=msg)


#  CONTROLLER 

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.btn_attack.config(command=self.attack)

        self.view.update_text("Potwór atakuje! Co robisz?")

    def attack(self):
        dmg = self.model.attack_enemy()

        if self.model.is_enemy_dead():
            self.view.update_text(f"Zadałeś {dmg} dmg!\nPokonałeś potwora!")
            return

        enemy_dmg = self.model.enemy_attack()

        if self.model.is_player_dead():
            self.view.update_text(
                f"Zadałeś {dmg} dmg, ale potwór zadał {enemy_dmg}!\nPrzegrałeś!"
            )
            return

        self.view.update_text(
            f"Zadałeś {dmg} dmg!\n"
            f"Potwór ma {self.model.enemy_hp} HP\n"
            f"Potwór zadał Ci {enemy_dmg} dmg!\n"
            f"Masz {self.model.player_hp} HP"
        )


#  start

if __name__ == "__main__":
    root = tk.Tk()
    model = GameModel()
    view = GameView(root)
    controller = GameController(model, view)
    root.mainloop()