#Nathan Greene 2021
from random import randint


def rollstats():
    stats = []
    for i in range(6):
        currentRoll = []
        for x in range(4):
            currentRoll.append(randint(1,6))
        currentRoll.remove(min(currentRoll))
        stats.append(sum(currentRoll))
    stats.append(15)
    stats.sort()
    return stats

def determineMod(score):
    mod = -3
    if score > 4:
        mod = -2
    if score > 6:
        mod = -1
    if score > 8:
        mod = 0
    if score > 12:
        mod = 1
    if score > 14:
        mod = 2
    if score > 16:
        mod = 3
    return mod

class hireling:

    def addWeapon(self, name, dist, dice, mod, extra=""):
        if mod == "Str":
            bonus = str(self.Str)
            if self.Str >= 0:
                bonus = "+" + bonus
        if mod == "Dex":
            bonus = str(self.Dex)
            if self.Dex >= 0:
                bonus = "+" + bonus
        weapon = name +" ("+dist+", "+bonus+" to-hit," +str(dice)+bonus+" damage"+")" 
        if extra != "":
            stars = ""
            for i in range(len(self.extraInfo)+1):
                stars = stars + "*"
            weapon = weapon + stars
            self.extraInfo.append(stars + extra)
        self.gear.append(weapon)

    def addGear(self, item):
        self.gear.append(item)

    def __init__(self, background):
        self.background = background
        self.dice = rollstats()
        self.AC = 10
        self.hitpoints = 4
        self.Strength = 0
        self.Str = -3
        self.Dexterity = 0
        self.Dex = -3
        self.Constitution = 0
        self.Con = -3
        self.Perception = 0
        self.Perc = -3
        self.Willpower = 0
        self.Will = -3
        self.Intelligence = 0
        self.Int = -3
        self.Charisma = 0
        self.Cha = -3

        self.gear = []
        self.extraInfo = []

    def setStr(self):
        self.Strength = self.dice.pop()
        self.Str = determineMod(self.Strength)
    def setDex(self):
        self.Dexterity = self.dice.pop()
        self.Dex = determineMod(self.Dexterity)
        self.AC += self.Dex
    def setCon(self):
        self.Constitution = self.dice.pop()
        self.Con = determineMod(self.Constitution)
        self.hitpoints += self.Con
    def setPerc(self):
        self.Perception = self.dice.pop()
        self.Perc = determineMod(self.Perception)
    def setWill(self):
        self.Willpower = self.dice.pop()
        self.Will = determineMod(self.Willpower)
    def setInt(self):
        self.Intelligence = self.dice.pop()
        self.Int = determineMod(self.Intelligence)
    def setCha(self):
        self.Charisma = self.dice.pop()
        self.Cha = determineMod(self.Charisma)

    def addArmor(self, armor):
        self.AC += armor

    def printChar(self, location):
        location.write("Name: \n")
        location.write("Background: "+self.background+"\n")
        location.write("\n")
        location.write("Str "+str(self.Strength)+" Dex "+str(self.Dexterity)+" Con "+str(self.Constitution)+" Int "+str(self.Intelligence)+"\n")
        location.write("Perc "+str(self.Perception)+" Will "+str(self.Willpower)+" Cha "+str(self.Charisma)+" Luck: 4"+"\n")
        location.write("\n")
        location.write("Armour Class: "+str(self.AC)+"    Hit Points:" +str(self.hitpoints)+"\n")
        location.write("\n")
        location.write("GEAR/NOTES\n")
        location.write("----------\n")
        for item in self.gear:
            location.write(item+"\n")
        location.write("\n")
        for item in self.extraInfo:
            location.write(item+"\n")
        location.write("\n\n\n\n")

def randomLightArmor():
    armors = ["Heavy Robes", "Hide", "Leather", "Studded Leather"]
    return armors[randint(0,3)]+" (+1 AC)"

def randomMediumArmor():
    armors = ["Chain Shirt", "Scale Shirt", "Breastplate", "Bone Armor", "Reinforced Hide", "Monster Chitin Armor"]
    return armors[randint(0,5)]+" (+3 AC)"

def randomHeavyArmor():
    armors = ["Plate Mail", "Splint Armor", "Chain Mail", "Ring Mail"]
    return armors[randint(0,3)]+" (+5 AC)"

def lbmh(character):
    random = randint(0,3)
    if random == 0:
        character.addWeapon("Longsword", "Melee", "1d8", "Str", "+1 damage if two-handed, disarm foe on nat. 19")
    if random == 1:
        character.addWeapon("Battle Axe", "Melee", "1d8", "Str", "+1 damage if two-handed, on nat. 19 foe is injured.")
    if random == 2:
        character.addWeapon("Mace", "Melee", "1d6", "Str", "May be thrown 25 ft, on nat. 19 knock target prone or 10ft back.")
    if random == 3:
        character.addWeapon("Hammer", "Melee", "1d8", "Str", "+1 damage if two-handed, on nat. 19 knock target prone or 10ft back.")

def makeHireling(combatant, location) :
    if combatant:
        backgrounds = ["City Watch", "Militia", "Bodyguard", "Pit Fighter", "Soldier", "Thug", "Pirate", "Green Recruit"]
        character = hireling(backgrounds[randint(0,7)])
        gear = randint(1,12)
        if gear == 1:
            character.setStr()
            character.setCon()
            character.setDex()
            character.setPerc()
            character.setCha()
            character.setWill()
            character.setInt()
            character.addArmor(1)
            character.addGear(randomLightArmor())
            character.addWeapon("Shortsword", "Melee", "1d6", "Str", "Disarm on nat 19. +2 on Init. Checks")
        if gear == 2:
            character.setCon()
            character.setStr()
            character.setWill()
            character.setCha()
            character.setPerc()
            character.setDex()
            character.setInt()
            character.addArmor(1)
            character.addGear(randomLightArmor())
            character.addWeapon("Flail", "Melee", "1d6+1", "Str", "Trip or Disarm on Nat 19.")
        if gear == 3:
            character.setStr()
            character.setDex()
            character.setCon()
            character.setCha()
            character.setWill()
            character.setInt()
            character.setPerc()
            character.addArmor(2)
            character.addGear("Shield (+1 AC)")
            character.addGear(randomLightArmor())
            character.addWeapon("Spear", "10ft", "1d6+1", "Str", "+1 damage if used two handed, may be thrown 50ft.")
        if gear == 4:
            character.setStr()
            character.setCon()
            character.setDex()
            character.setWill()
            character.setPerc()
            character.setCha()
            character.setInt()
            character.addArmor(3)
            character.addGear(randomMediumArmor())
            character.addWeapon("Heavy Mace", "Melee", "1d8", "Str", "+1 if used two handed, on nat. 19 knock target prone or backwards 10ft.")
        if gear == 5: 
            character.setCon()
            character.setDex()
            character.setStr()
            character.setCha()
            character.setWill()
            character.setInt()
            character.setPerc()
            character.addArmor(4)
            character.addGear(randomMediumArmor())
            character.addGear("Shield (+1 AC)")
            character.addWeapon("Shortsword", "Melee", "1d6", "Str", "Disarm on nat 19. +2 to Init. Checks")
            character.addWeapon("3 Light Axes", "25ft", "1d6", "Dex", "Thrown. On nat. 19, target gains an injury")
        if gear == 6:
            character.setDex()
            character.setCon()
            character.setWill()
            character.setStr()
            character.setPerc()
            character.setInt()
            character.setCha()
            character.addArmor(3)
            character.addGear(randomMediumArmor())
            character.addWeapon("Spear", "10ft", "1d6+1", "Str", "+1 damage if used two-handed. May be thrown 50ft.")
            character.addWeapon("3 Javelins", "70ft", "1d6", "Dex", "May be used in melee without disadvantage.")
        if gear == 7:
            character.setStr()
            character.setDex()
            character.setCon()
            character.setPerc()
            character.setInt()
            character.setCha()
            character.setWill()
            character.addArmor(4)
            character.addGear(randomMediumArmor())
            character.addGear("Shield (+1 AC)")
            lbmh(character)
        if gear == 8:
            character.setCon()
            character.setStr()
            character.setDex()
            character.setWill()
            character.setCha()
            character.setPerc()
            character.setInt()
            character.addArmor(3)
            character.addGear(randomMediumArmor())
            polearms = ["Glaive", "Halberd", "Falchion", "Guisame", "Naginata"]
            polearm = polearms[randint(0,4)]
            character.addWeapon(polearm, "10ft", "1d10", "Str", "Two-handed. Suffers disadvantage in cramped quarters.")
        if gear == 9:
            character.setStr()
            character.setCon()
            character.setDex()
            character.setCha()
            character.setInt()
            character.setPerc()
            character.setWill()
            character.addArmor(3)
            character.addGear(randomMediumArmor())
            weaponNames = ["Greatsword", "Greataxe", "Great-Hammer"]
            weapon = weaponNames[randint(0,2)]
            character.addWeapon(weapon, "Melee", "1d12", "Str", "Two-handed. Disadvantage in cramped quarters. On nat. 19 daze foe.")
        if gear == 10:
            character.setDex()
            character.setCon()
            character.setPerc()
            character.setInt()
            character.setCha()
            character.setWill()
            character.setStr()
            character.addArmor(1)
            character.addGear(randomLightArmor())
            character.addWeapon("Shortsword", "Melee", "1d6", "Str", "Disarm on nat. 19. +2 to init")
            bow = randint(0,1)
            if bow == 1:
                character.addWeapon("Short Bow", "100ft", "1d6", "Dex", "Two-handed. May be used while mounted.")
            else:
                character.addWeapon("Long Bow", "250ft", "1d8", "Dex", "Two-handed.")
            character.addGear("20 Arrows")
        if gear == 11:
            character.setDex()
            character.setCon()
            character.setCha()
            character.setInt()
            character.setPerc()
            character.setWill()
            character.setStr()
            character.addArmor(3)
            character.addGear(randomMediumArmor())
            character.addWeapon("Heavy Crossbow", "200ft", "2d8", "Dex", "Two-handed. Target prone on nat. 19. Costs an action to reload.")
            character.addGear("20 Crossbow Bolts")
        if gear == 12:
            character.setStr()
            character.setCon()
            character.setDex()
            character.setCha()
            character.setPerc()
            character.setWill()
            character.setInt()
            character.addArmor(6)
            character.addGear(randomHeavyArmor())
            character.addGear("Shield (+1 AC)")
            lbmh(character)
    else:
        backgrounds = {
                "Pickpocket" : "Lockpick",
                "Rat Catcher" : "Rat Poison",
                "Grave Digger" : "Shovel",
                "Beggar" : "Mangy Dog (Stats as Wolf)",
                "Busker" : "Lute",
                "Fishmonger" : "1 Week of Rations (Misc. Fish)",
                "Skinner" : "3 Sheets of Leather",
                "Alley Thug" : "Bandit Mask",
                "Lay Preacher" : "Holy Water",
                "Woodsplitter" : "Flannel Shirt",
                "Ditch Digger" : "Shovel",
                "Street Sweeper" : "Broom",
                "Bar Wench" : "2 Liter Ale Barrel",
                "Yellow Lotus Addict" : "5 Yellow Lotus Pellets",
                "Chimney Sweep" : "Grappling Hook",
                "Mutineer" : "Sextant",
                "Beekeeper" : "Jar full of bees",
                "Leech Collector" : "3 'Medicinal' Leeches",
                "Stable Hand" : "4 Sugar Cubes",
                "Bone Grubber" : "2 Old Outfits",
                "Deserter" : "Insignia of Rank",
                "Thatcher" : "Bucket of Pitch",
                "Cobbler" : "Tinker's Tools",
                "Wagoneer" : "Wagon & Mule",
                "Limeburner" : "Raw Limestone",
                "Organlegger" : "Healer's Kit",
                "Ploughman" : "Draft Horse",
                "Scullion" : "Cook's Tools",
                "Mudlark" : "10 ft Pole",
                "Swineherd" : "Sturdy Riding Pig",
                "Fur Trapper" : "2 Bear Traps",
                "Fuller" : "Fuller's Earth",
                "Gong Farmer" : "Smelly Bucket",
                "Hangman" : "Ominous Hood"
        }
        backGroundNames = list(backgrounds.keys())
        background = backGroundNames[randint(0,len(backGroundNames)-1)]
        character = hireling(background)
        array = randint(1,7)
        if array == 1:
            character.setStr()
            character.setCon()
            character.setCha()
            character.setWill()
            character.setPerc()
            character.setInt()
            character.setDex()
        if array == 2:
            character.setCon()
            character.setWill()
            character.setPerc()
            character.setCha()
            character.setStr()
            character.setDex()
            character.setInt()
        if array == 3:
            character.setCha()
            character.setDex()
            character.setPerc()
            character.setCon()
            character.setInt()
            character.setWill()
            character.setStr()
        if array == 4:
            character.setWill()
            character.setCon()
            character.setCha()
            character.setStr()
            character.setPerc()
            character.setInt()
            character.setDex()
        if array == 5:
            character.setPerc()
            character.setDex()
            character.setCon()
            character.setInt()
            character.setWill()
            character.setCha()
            character.setStr()
        if array == 6:
            character.setInt()
            character.setDex()
            character.setCon()
            character.setPerc()
            character.setCha()
            character.setWill()
            character.setStr()
        if array == 7:
            character.setDex()
            character.setPerc()
            character.setCha()
            character.setCon()
            character.setInt()
            character.setWill()
            character.setStr()
        gear = randint(1,4)
        if gear == 1:
            character.addWeapon("Knife", "40ft", "1d4", "Dex", "Easily concealed. +2 on init checks")
        if gear == 2:
            character.addWeapon("Club", "Melee", "1d6", "Str")
        if gear == 3:
            character.addWeapon("Flail", "Melee", "1d6+1", "Str", "On a natural 19, trip or disarm foe.")
        if gear == 4:
            character.addWeapon("Staff", "10ft", "1d6", "Str", "+1 if used two-handed.")
        character.addGear(backgrounds[background])

    KnickKnacks = ["Bell", "Block & Tackle", "10 Candles", "Chalk (10 Sticks)", "Grappling Hook", "Lamp", "Lantern (Bullseye)", "Lantern (Hooded)", "Mirror (Small steel)", "Oil (2 Pints)", "Parchment (5 sheets)", "Pickaxe", "10 Ft Pole", "Pot (Cast Iron)", "Sack (Large)", "Rations (1 week)", "Rope (60 ft)", "Sealing Wax", "Signal Whistle", "Iron Spike (5)", "Tent (2 person)", "Torch (5)"]
    character.addGear(KnickKnacks[randint(0,len(KnickKnacks)-1)])
    character.addGear(KnickKnacks[randint(0,len(KnickKnacks)-1)])

    character.printChar(location)

def generateBatch(charType, numChars, location):
    for i in range(numChars):
        if charType == "m" :
            if randint(0,1) == 1:
                makeHireling(True, location)
            else:
                makeHireling(False, location)
        if charType == "c" :
            makeHireling(True, location)
        if charType == "n" :
            makeHireling(False, location)

