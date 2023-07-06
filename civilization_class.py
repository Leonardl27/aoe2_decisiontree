# Civilization Class format

# Create Civ class
class Civilization:
    def __init__(self, name, archer_civ_plus=False, knight_civ=False, infantry_civ=False, camel_civ=False, archer_civ_minus=False,
hussar=False, halb=False, elite_skirm=False):
        self.name = name
        self.archer_civ_plus = archer_civ_plus
        self.knight_civ = knight_civ
        self.infantry_civ = infantry_civ
        self.camel_civ = camel_civ
        self.archer_civ_minus = archer_civ_minus
        self.hussar = hussar
        self.halb = halb
        self.elite_skirm = elite_skirm

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