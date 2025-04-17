'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
State Ferry fare based on age and whether the person has a vehicle. Assume the following rates:
* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
* Children (0-18): Free.
'''

def ferry_fare(age, vehicle):
    adult_fare = 10
    senior_fare = 5
    vehicle_fare = 10
    cost = 0
    if (age > 18 and age < 65):
        cost += adult_fare
    elif(age >= 65):
        cost += senior_fare
    if (vehicle):
        cost += vehicle_fare
    return cost
