
def fit_to_upper(name: str) -> str:
    return name.upper()

def fit_jr(name: str) -> str:
    """treat junior to jr"""
    names = name.split(" ")
    for i in range(1,len(names)):
        if names[i] == "JUNIOR":
            names[i] = 'JR'
    return(" ".join(names))

def name_size(name: str) -> bool:
    if len(name) < 27:
        return True
    return False 

def remove_particles(name: str) -> str:
    particles = ["DE", "DOS", "DA"]
    names = name.split(" ")
    names = [item for item in names if item not in particles]
    return(" ".join(names))

def remove_sufix(name: str) -> str:
    names = name.split(" ")
    for i in range(1,len(names)):
        if names[i] == "FILHO":
            names[i] = 'F.'
        if names[i] == "NETO":
            names[i] = 'N.'
    return(" ".join(names))

def reduce_size(name:str) -> str:
    return(name[:26])



def fit(name: str) -> str:
    name = fit_to_upper(name)
    name = fit_jr(name)
    if name_size(name):
        return name
    name = remove_particles(name)
    if name_size(name):
        return name
    name = remove_sufix(name)
    if name_size(name):
        return name
    name = reduce_name(name)
    if name_size(name):
        return name
    name = reduce_name2(name)
    name = reduce_size(name)

    return name

    
def reduce_name(name: str) -> str:
    names = name.split(" ")
    for i in range(1,len(names) - 1):
        if len(names[i]) > 5:
            names[i] = names[i][0]
    return(" ".join(names))

def reduce_name2(name: str) -> str:
    names = name.split(" ")
    for i in range(1,len(names) - 1):
        names[i] = names[i][0]
    return(" ".join(names))


