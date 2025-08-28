import cardnames

def test_fit_jr():
    given = 'João Vitor Souza de Oliveira JUNIOR'
    expected = 'João Vitor Souza de Oliveira JR'
    result = cardnames.fit_jr(given)
    assert result == expected

def test_first_name_jr():
    given = 'JUNIOR Vitor Souza de Oliveira JUNIOR'
    expected = 'JUNIOR Vitor Souza de Oliveira JR'
    result = cardnames.fit_jr(given)
    assert result == expected

def test_is_upper():
    given = 'João Vitor Souza de Oliveira JUNIOR'
    expected = "JOÃO VITOR SOUZA DE OLIVEIRA JUNIOR"
    result = cardnames.fit_to_upper(given)
    assert result == expected

def test_size_ok():
    given = 'JUNIOR VITOR SOUZA'
    expected = True
    result = cardnames.name_size(given)
    assert result == expected

def test_size_ok():
    given = 'João Vitor Souza de Oliveira JUNIOR blablablabla'
    expected = False
    result = cardnames.name_size(given)
    assert result == expected

def test_fit():
    given = 'JUNIOR Vitori Souza de Oliveira Neto Filho JUNIOR'
    expected = "JUNIOR V SOUZA O N. F. JR"
    result = cardnames.fit(given)
    assert result == expected

def test_particles():
    given = 'JUNIOR Vitor Souza DE DA DOS Oliveira JUNIOR'
    expected = "JUNIOR Vitor Souza Oliveira JUNIOR"
    result = cardnames.remove_particles(given)
    assert result == expected

def test_sufix():
    given = 'JUNIOR Vitor Souza NETO FILHO Oliveira JUNIOR'
    expected = "JUNIOR Vitor Souza N. F. Oliveira JUNIOR"
    result = cardnames.remove_sufix(given)
    assert result == expected

def test_reduce_size():
    given = 'JUNIOR Vitor Souza NETO FILHO Oliveira JUNIOR'
    expected = "JUNIOR Vitor Souza NETO FI"
    result = cardnames.reduce_size(given)
    assert result == expected

def test_reduce_name():
    given = 'JUNIOR Souza NETO FILHO Oliveira JUNIOR'
    expected = "JUNIOR Souza NETO FILHO O JUNIOR"
    result = cardnames.reduce_name(given)
    assert result == expected

def test_reduce_name2():
    given = 'JUNIOR Souza Souza Souza NETO FILHO Oliveira JUNIOR'
    expected = "JUNIOR S S S N F O JUNIOR"
    result = cardnames.reduce_name2(given)
    assert result == expected