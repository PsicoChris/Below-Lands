class Character():

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe (self):
        print(self.name + "is here!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk (self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
        print("[" + self.name + " says]: " + "Are you leaving now?")
        resp=input("Yes/No")
        if resp == "Yes" or resp == "yes":
            print("[" + self.name + " says]: " + "Then go, and do not bother the land of below" )
        elif resp == "No" or resp == "no":
            print("[" + self.name + " says]: " + "Then you'll suffer... " )
            print("Zombies raise and take their swords out*")
        else:
            print("...")

class Enemy(Character):
    def __init__ (self, char_name, char_description):
            super().__init__(char_name, char_description)
            self.weakness = None
    
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness
 
    def get_weakness(self):
        return self._weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You anhilate " + self.name + " with the " + combat_item )
            return True
        else:
            print(self.name + " destroys you, a simple weapon is nothing against a legion of zombies*")
            return False

class Neutral(Character):
    def __init__ (self, char_name, char_description):
            super().__init__(char_name, char_description)
            self.weakness = None