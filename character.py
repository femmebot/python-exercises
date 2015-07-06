class Character(object):
    experience = 0
    hit_points = 10

    def get_weapon(self):
        weapon_choice = input("Weapon ([S]word, [A]xe, [B]ow): ").lower()

        if weapon_choice in 'sab':
            if weapon_choice == 's':
                return 'sword'
            elif weapon_choice == 'a':
                return 'axe'
            else:
                return 'bow'
        else:
            return self.get_weapon() 

    def __init__(self, **kwargs):
        self.name = input("Name: ")
        self.weapon = input("Weapon ([S]word, [A]xe, [B]ow): ")

        for key, value in kwargs.items():
            setattr(self, key, value)
