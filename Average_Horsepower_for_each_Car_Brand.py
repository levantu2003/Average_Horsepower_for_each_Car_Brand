import csv

with open("cars.csv","r") as f:
    csv_reader = csv.DictReader(f)
    cars = list(csv_reader)

car_brands = {}
for car in cars:
    car_brands[car['Make']] = car_brands.get(car['Make'], []) + [car['Horsepower']]
car_brand_hp = {}

for car_brand, hp_list in car_brands.items():
    hp_sum = 0
    for hp in hp_list:
        hp_sum = hp_sum + int(hp)
    car_brand_hp[car_brand] = hp_sum/len(hp_list)

print(car_brand_hp)
