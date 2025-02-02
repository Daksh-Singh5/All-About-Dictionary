Code = {
    "india":"0091",
    "japan":"0081",
    "malasiya":"0063",
    "mexio":"0052",
    "north Korea":"0850",
    "pakistan":"0092",
    "poland":"0048",
    "qatar":"0794",
    "russia":"0007",
    "rwanda":"0250",
}

country = input("Which country code do you want: ")
country = country.lower()
print("The ",country+"'s","code is:",Code.get(country,"This is not give"))