from person import Person


def test_person() -> None:
    p = Person("Edu", 35)
    assert p.name == "Edu"
    assert p.age == 35
    assert p.birthday() == 36
    p = Person("Edu", -1)
    assert p.name == "Edu"
    assert p.age == -1
    assert p.birthday() == 0
