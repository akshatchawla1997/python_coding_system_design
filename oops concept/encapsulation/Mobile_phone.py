class Mobile_phone:
    def __init__(self, storage, battery):
        self.__storage = storage
        self.__battery = battery

    def charge(self, amount):
        self.__battery += amount
        print(f"Charged {amount} into the phone")

    def use(self, amount):
        self.__battery -= amount
        print(f"Used {amount} from the phone")
    def get_storage(self):
        return self.__storage
    def get_battery(self):  
        return self.__battery
    def new_app(self, app):
        if self.__storage + app > 100:
            print("Storage full")
            return False
        else:
            self.__storage += app
            print(f"New app {app} installed")
            return True
    def remove_app(self, app):
        if self.__storage - app < 0:
            print("Storage empty")
            return False
        else:
            self.__storage -= app
            print(f"App {app} removed")
            return True
        
mobile_phone1 = Mobile_phone(100, 100)
mobile_phone1.new_app(50)
mobile_phone1.remove_app(20)
print(f"Storage: {mobile_phone1.get_storage()}")
print(f"Battery: {mobile_phone1.get_battery()}")
print(f"New app installed: {mobile_phone1.new_app(50)}")
print(f"App removed: {mobile_phone1.remove_app(20)}")
print(f"Storage: {mobile_phone1.get_storage()}")
print(f"Battery: {mobile_phone1.get_battery()}")
print(f"New app installed: {mobile_phone1.new_app(50)}")
print(f"App removed: {mobile_phone1.remove_app(20)}")
print(f"Storage: {mobile_phone1.get_storage()}")
print(f"Battery: {mobile_phone1.get_battery()}")