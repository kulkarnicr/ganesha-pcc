# Ganesha
"""Class for User"""
class User():
    def __init__(self, first_name: str, last_name: str, age: int, height: float) -> None:
        """define user attributes"""
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
    
    def describe_user(self) -> None:
        """method to print user info"""
        
        print("User information:")
        print(f"\tFirst name: {self.first_name}")
        print(f"\tLast name : {self.last_name}")
        print(f"\tAge       : {self.age}")
        print(f"\tHeight    : {self.height}")
    
    def greet_user(self) -> None:
        """method to print personalized greeting to the user"""
        
        print(f"Hi '{self.first_name} {self.last_name}', welcome to the user class.")
