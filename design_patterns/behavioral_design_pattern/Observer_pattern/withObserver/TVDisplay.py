from Observer import Observer 

class TVDisplay(Observer):

    def update(self, temp):
        print(f"TV temperature updated to {temp}")