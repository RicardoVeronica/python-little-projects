class Character(object):
    def __init__(self, character_class, character_name, character_sex, level,
                vigor, attunement, endurance, vitality, strength, dexterity, 
                intelligence, faith, luck):
        self.character_class = character_class
        self.character_name = character_name
        self.character_sex = character_sex
        self.level = level
        self.vigor = vigor
        self.attunement = attunement
        self.endurance = endurance
        self.vitality = vitality
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.faith = faith
        self.luck = luck


    def name_it(self):
        name = input('What is the name of your character: ')
        character_name = name

        return character_name


    def girl_boy(self):
        sex = input('What is the sex of yout character: ')
        character_sex = sex

        return character_sex
