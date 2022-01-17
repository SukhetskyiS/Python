def email_parse(email):
    my_dict = {}
    import re
    pattern = r"^[a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
    RE_EMAIL = re.compile(pattern)
    try:
        if RE_EMAIL.match(email) is not None:
            my_dict.setdefault('username', re.compile(r"^[a-zA-Z0-9\._]+").findall(email)[0])
            my_dict.setdefault('domain', re.compile(r"[a-zA-Z0-9]+\.[a-zA-Z]+$").findall(email)[0])
            return my_dict
        else:
            raise ValueError
    except ValueError:
        return f'ValueError: wrong email: {email}'


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
