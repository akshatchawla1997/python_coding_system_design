from Observer import Observer

class MobileDisplay(Observer):
    
    def update(self, temp):
        print(f"Mobile temperature updated to {temp}")