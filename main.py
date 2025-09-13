import random

def street_food_combo():
    # Lists of food and drinks
    mains = ["Sev Usal", "Vada Pav", "Dabeli", "Locho", "Kachori", "Pav Bhaji"]
    sides = ["Masala Fries", "Fafda", "Chilli Garlic Noodles", "Onion Bhajiya", "Cheese Puff"]
    drinks = ["Sugarcane Juice", "Chaas", "Cold Coco", "Buttermilk", "Falooda"]
    spice_levels = ["Low", "Medium", "Tears of Joy"]

    # choices
    main = random.choice(mains)
    side = random.choice(sides)
    drink = random.choice(drinks)
    spice = random.choice(spice_levels)

    # formatting
    combo = f"""
     Vadodara Street Food Combo of the Evening 
    ------------------------------------------------
    Main Dish : {main}
     Side      : {side}
     Drink     : {drink}
     Spicy Lv : {spice}
    ------------------------------------------------
    Enjoy your meal!
    """
    return combo


print(street_food_combo())
