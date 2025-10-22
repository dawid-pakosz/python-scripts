from mimesis.enums import Gender
from mimesis import Person

person = Person("pl")

user = {
    "name": person.full_name(gender=Gender.MALE),
    "height": person.height(),
    "phone": person.telephone(),
    "occupation": person.occupation()
}

print(user)