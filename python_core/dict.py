
thisdict = {
    "band": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)
print(len(thisdict))
print(thisdict['model'])
print(thisdict.get('model'))
l1=list(thisdict.keys())
print(l1)

l2=list(thisdict.values())
print(l2)

l3=list(thisdict.items())
print(l3)

print("model" in thisdict)

thisdict.update({"year":2026})
print(thisdict)

thisdict.pop("band")
print(thisdict)

car={
    "brand":"Ford","model": "Mustang","year":2024
}
print(car)
print(car.get("model"))
car["color"]="red"
car.pop("brand")
print(car)