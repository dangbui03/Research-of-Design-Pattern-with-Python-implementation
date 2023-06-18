import abc

class Gun(metaclass=abc.ABCMeta):
    """
    Define the base interface for a gun.
    """
    @abc.abstractmethod
    def assemble(self):
        pass

class BaseGun(Gun):
    """
    Define the base implementation of a gun.
    """
    def assemble(self):
        print("Assembling the base gun.")

class GunDecorator(Gun, metaclass=abc.ABCMeta):
    """
    Define the base decorator class that wraps a Gun object.
    """
    def __init__(self, gun):
        self.gun = gun

    def assemble(self):
        self.gun.assemble()

class Scope(GunDecorator):
    """
    Add a scope attachment to the gun.
    """
    def assemble(self):
        super().assemble()
        print("Adding a scope attachment.")

class Silencer(GunDecorator):
    """
    Add a silencer attachment to the gun.
    """
    def assemble(self):
        super().assemble()
        print("Adding a silencer attachment.")

class ExtendedMagazine(GunDecorator):
    """
    Add an extended magazine to the gun.
    """
    def assemble(self):
        super().assemble()
        print("Adding an extended magazine.")

def main():
    # Assemble a base gun
    base_gun = BaseGun()
    base_gun.assemble()
    print("")

    # Assemble a gun with scope and silencer
    scoped_silenced_gun = Silencer(Scope(BaseGun()))
    scoped_silenced_gun.assemble()
    print("")

    # Assemble a gun with extended magazine
    extended_mag_gun = ExtendedMagazine(BaseGun())
    extended_mag_gun.assemble()
    print("")

    # Assemble a gun with all attachments
    fully_customized_gun = ExtendedMagazine(Silencer(Scope(BaseGun())))
    fully_customized_gun.assemble()

if __name__ == "__main__":
    main()
