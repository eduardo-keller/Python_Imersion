# persons = {
#     "jean": "valjean",
#     "grace": "hopper",
#     "xavier": "niel",
#     "fifi": "brindacier"
#     }


def format_names(dct: dict[str, str]) -> list[str]:
    '''receives a dict and returns a list of key/values capitalized'''
    name_list = []

    for key, value in dct.items():
        name = f"{key.capitalize()} {value.capitalize()}"
        name_list.append(name)
    return name_list


# if __name__== "__main__":
#     s = format_names(persons)
#     print(s)
