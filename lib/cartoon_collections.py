def roll_call_dwarves(dwarves):
   for index, dwarf in enumerate(dwarves, start=1):
        print(f"{index}. {dwarf}")


def summon_captain_planet(captain_calls):
    return [call.capitalize() + '!' for call in captain_calls]


def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]
    for snack in snacks:
        if snack in cheeses:
            return snack
    return None
