from random import choice
from typing import Optional, List


def cast_random_spell(additional_spells: Optional[List] = None) -> str:
    spells = [
        'Expelliarmus',
        'Avada Kedavra',
        'Expecto Patronum',
        'Protego Maxima',
        'Lumos Maxima',
        'Wingardium Leviosa'
    ]
    if additional_spells:
        spells += additional_spells

    return f'{choice(spells)}!'
