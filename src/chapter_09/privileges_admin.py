# Ganesha
"""Class for Privileges, Admin"""
from user import User

class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can reset passwords for users periodically",
            "can unlock user"
        ]
    
    def show_privileges(self):
        """method to print admin privileges"""
        print("Admin privileges are:")
        for privilege in self.privileges:
            print(f"\t{privilege}")


class AdminWithPrivilegesAsAttribute(User):
    def __init__(self, first_name: str, last_name: str, age: int, height: float) -> None:
        super().__init__(first_name, last_name, age, height)
        self.privileges = Privileges()
