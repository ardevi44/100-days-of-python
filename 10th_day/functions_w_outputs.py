def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"


def format_name_2(f_name, l_name):
    if f_name == "" and l_name == "":
        return "You have tu pass both names"
    elif f_name == "" or l_name == "":
        return "You're not passing some of the values"
    else:
        return f"{f_name.title()} {l_name.title()}"


print(
    format_name_2(
        f_name=input("Please enter the first name: "),
        l_name=input("Please enter the last name: ")
    )
)
