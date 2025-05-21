class SpaceShip:
    __armor = 50

    def __init__(self, life=100):
        self.__life = life

    @classmethod
    def upgrade_armor(cls):
        cls.__armor += 0.1 * cls.__armor

    @classmethod
    def get_armor(cls):
        return cls.__armor

    @staticmethod
    def blowup_animation():
        print("EvilSpaceShip blow up")

    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, value):
        if value > 0:
            self.__life = value


if __name__ == '__main__':
    sp1 = SpaceShip()
    sp2 = SpaceShip(50)
    print("armor init:", SpaceShip.get_armor())
    SpaceShip.upgrade_armor()
    print("armor after upgrade:", SpaceShip.get_armor())
