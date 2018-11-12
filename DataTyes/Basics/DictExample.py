car = {
"Model":"Nissan",
"Year":2013,
"Warranty":"3 Years",
"Model":"Nissan1",
"Year":2018,
"Warranty":"5 Years"
}

print(car["Model"],car["Year"],car["Warranty"],sep=',')


car["place"]="Newcastle"

print(car["place"])

print(car.keys(),car.values())

print(car.get("Model"))

