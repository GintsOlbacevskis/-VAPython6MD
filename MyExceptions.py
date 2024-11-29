#Define a custom exception
class InvalidAge(Exception):
    def __init__(self, age, message="Vecumam jābūt starp 50 un 110."):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} Jūs ievadījāt: {self.age}"

#Func to valid age
def validate_age(age):
    if not (0 <= age <= 110):
        raise InvalidAge(age)
    print(f"Vecums {age} ir atļauts.")

#Test the func with try-except
try:
    age = int(input("Ievadi vecumu: "))
    validate_age(age)
except InvalidAge as e:
    print(e)
except ValueError:
    print("Kļūda: Lūdzu ievadi ciparu")
finally:
    print("Validācijas process ir beidzies")