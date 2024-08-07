person  = { "Name" : "Nitin",
          "age": 100,
          "country": "USA"
}

person["country"] = "INDIA"
print(person.get("country"))

for i in person.items:
    print(i)

