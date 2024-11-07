class Father():
    def gardening(self):
        print("I love Gardening")
    def skill(self):
        print("Programming")

class Mother():
    def cooking(self):
        print("i love cooking")
    def skill(self):
        print("Cooking")

class child(Father,Mother):
    def sports(self):
        print("I enjoy sports")
    def skill(self):
        Father.skill(self)
        Mother.skill(self)
        print("Sports")

c=child()

c.skill()