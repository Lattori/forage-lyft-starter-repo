import car

tire_wear_array = [0, 0.2, 0.6, 0.9]


def check_if_tire_serviced(tire_wear, brand):
    if brand is "Carrigan tires" and tire_wear >= 0.9:
        print("Does not need to be serviced")

    elif brand is "Octoprime tires" and sum(tire_wear_array) > 3:
        print("does not need to be serviced")
    else:
        print("needs to be serviced")
