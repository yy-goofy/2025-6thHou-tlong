class OW_Character:
    def __init__(self, health, damage, ammo):
        self.health = health
        self.damage = damage
        self.ammo = ammo
    def buff_health_10_percent(self):
        self.health *= 11 / 10
    def nerf_damage_one_third(self):
        self.damage *= 2 / 3
reinhardt = OW_Character(600, 65, 0)
wreckingball = OW_Character(675, 25, 100)
print(f"Reinhardt HP:", reinhardt.health)
print(f"Reinhardt DMG:", reinhardt.damage)