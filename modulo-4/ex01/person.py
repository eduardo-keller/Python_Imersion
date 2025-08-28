
class Person:
    def __init__(self, name: str, age: int) -> None:
        'constructor'
        self.name = name
        self.age = age
    def birthday(self) -> int:
        'increase age'
        return (self.age + 1)
    # def __str__(self):
    #     return f"{self.name}({self.age})"

# p = Person("Edu", 30)
# print(p.birthday())
# print(p.birthday.__doc__)