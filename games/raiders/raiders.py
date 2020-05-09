
def raiders_config_menu(addons):
    # Set default values
    golds = 18
    meads = 0
    jarls = 0


    if 'hall_of_heroes' in addons:
        golds = golds + 5
        meads = 40

    if 'field_of_fame' in addons:
        jarls = 12

    pool = {1: ("Valk", 18), 
            2: ("Gold", golds),
            3: ("Iron", 18),
            4: ("Cows", 26), 
            5: ("Mead", meads),
            6: ("Jarl", jarls) }

    # Generate a pool of locations with their item slots
    location_pool = {1: ("Fortress", 2),
                     2: ("Fortress", 3),
                     3: ("Fortress", 2),
                     4: ("Fortress", 2),
                     5: ("Fortress", 2),
                     6: ("Fortress", 3),
                     7: ("Monastery", 3),
                     8: ("Monastery", 2),
                     9: ("Outpost", 3),
                     10: ("Outpost", 3), 
                     11: ("Monastery", 2), 
                     12: ("Monastery", 3), 
                     13: ("Harbour", 4),
                     14: ("Harbour", 3),
                     15: ("Harbour", 4),
                     16: ("Outpost", 4),
                     17: ("Outpost", 3),
                     18: ("Harbour", 3),
                     19: ("Harbour", 4),
                     20: ("Harbour", 4),
                     21: ("Harbour", 4),
                     22: ("Harbour", 3),
                     23: ("Harbour", 4) }

    if 'fieldOfFame' in addons:
        location_pool[24] = ("Township", 4)
        location_pool[25] = ("Township", 3)
        location_pool[26] = ("Township", 4)

    return pool, location_pool

