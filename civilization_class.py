# Civilization Class format

# Create Civ class

class Civilization:
    def __init__(self, name, archer_civ_plus=False, knight_civ=False, infantry_civ=False, camel_civ=False, 
                 archer_civ_minus=False, hussar=False, halb=False, elite_skirm=False, attack1=False, 
                 attack2=False, attack3=False, fletching=False, bodkin=False, bracer=False, 
                 arch_armour1=False, arch_armour2=False, arch_armour3=False, knight=False, cavalier=False, 
                 paladin=False, archer=False, crossbowman=False, arbalest=False, thumb_ring=False, 
                 ballistics=False, chemistry=False, bloodlines=False, husbandry=False, spearman=False, 
                 pikeman=False, halberdier=False, skirmisher=False, elite_skirmisher=False, scout=False, 
                 light_cavalry=False, hussar=False, magonel=False, onager=False, siege_onager=False, 
                 bombard_canon=False, trebuchet=False, siege_engineers=False):
        
        self.name = name
        self.archer_civ_plus = archer_civ_plus
        self.knight_civ = knight_civ
        self.infantry_civ = infantry_civ
        self.camel_civ = camel_civ
        self.archer_civ_minus = archer_civ_minus
        self.hussar = hussar
        self.halb = halb
        self.elite_skirm = elite_skirm
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack3 = attack3
        self.fletching = fletching
        self.bodkin = bodkin
        self.bracer = bracer
        self.arch_armour1 = arch_armour1
        self.arch_armour2 = arch_armour2
        self.arch_armour3 = arch_armour3
        self.knight = knight
        self.cavalier = cavalier
        self.paladin = paladin
        self.archer = archer
        self.crossbowman = crossbowman
        self.arbalest = arbalest
        self.thumb_ring = thumb_ring
        self.ballistics = ballistics
        self.chemistry = chemistry
        self.bloodlines = bloodlines
        self.husbandry = husbandry
        self.spearman = spearman
        self.pikeman = pikeman
        self.halberdier = halberdier
        self.skirmisher = skirmisher
        self.elite_skirmisher = elite_skirmisher
        self.scout = scout
        self.light_cavalry = light_cavalry
        self.hussar = hussar
        self.magonel = magonel
        self.onager = onager
        self.siege_onager = siege_onager
        self.bombard_canon = bombard_canon
        self.trebuchet = trebuchet
        self.siege_engineers = siege_engineers
'''
# Future edit to make the civilization class not so cumbersum
class Civilization:
    def __init__(self, name, unit_upgrades={}, tech_upgrades={}):
        self.name = name
        self.unit_upgrades = unit_upgrades
        self.tech_upgrades = tech_upgrades
'''

# Function to change a list to lower case 
def to_lowercase(input_list):
    return [item.lower() for item in input_list]

# Civ List
civilization_list = ["Aztecs", 
    "Berbers", 
    "Bengalis",
    "Britons", 
    "Bulgarians", 
    "Burmese", 
    "Byzantines", 
    "Celts", 
    "Chinese", 
    "Cumans",
    "Dravidians", 
    "Ethiopians", 
    "Franks", 
    "Goths", 
    "Huns",
    "Hindustanis",
    "Incas", 
    "Italians", 
    "Japanese", 
    "Khmer", 
    "Koreans", 
    "Lithuanians", 
    "Magyars", 
    "Malay", 
    "Malians", 
    "Mayans", 
    "Mongols", 
    "Persians", 
    "Portuguese", 
    "Romans",
    "Saracens", 
    "Slavs", 
    "Spanish", 
    "Teutons", 
    "Turks", 
    "Vietnamese", 
    "Vikings", 
    "Tatars", 
    "Sicilians", 
    "Burgundians"]

print(civilization_list)

archer_civs =[]
