def introduction(name):
    def x():
        return "My name is " + name + "."
    return x

intro = introduction("Jaquino")
print(intro()) 