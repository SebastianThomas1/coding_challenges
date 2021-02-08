# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/536e9a7973130a06eb000e9f
#
# Pokemon Damage Calculator

EFFECTIVENESS = {
    ('electric', 'electric'): 0.5,
    ('electric', 'fire'): 1,
    ('electric', 'grass'): 1,
    ('electric', 'water'): 2,
    ('fire', 'electric'): 1,
    ('fire', 'fire'): 0.5,
    ('fire', 'grass'): 2,
    ('fire', 'water'): 0.5,
    ('grass', 'electric'): 1,
    ('grass', 'fire'): 0.5,
    ('grass', 'grass'): 0.5,
    ('grass', 'water'): 2,
    ('water', 'electric'): 0.5,
    ('water', 'fire'): 2,
    ('water', 'grass'): 0.5,
    ('water', 'water'): 0.5
}


def calculate_damage(your_type, opponent_type, attack, defense):
    return 50 * (attack / defense) * EFFECTIVENESS[(your_type,
                                                    opponent_type)]


if __name__ == '__main__':
    print(calculate_damage('fire', 'water', 100, 100))  # 25
    print(calculate_damage('grass', 'water', 100, 100))  # 100
    print(calculate_damage('electric', 'fire', 100, 100))  # 50
    print(calculate_damage('grass', 'electric', 57, 19))  # 150
    print(calculate_damage('grass', 'water', 40, 40))  # 100
    print(calculate_damage('grass', 'fire', 35, 5))  # 175
    print(calculate_damage('fire', 'electric', 10, 2))  # 250
