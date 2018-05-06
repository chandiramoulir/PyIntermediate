class test_class():
    number = 1
    def __init__(self):
        self.text = "Hii"

    def doThis(self):
        print(test_class.number)
        self.number = 22
        print(self.number)
        print(test_class.number)
        print(self.text)

test = test_class()
test.doThis()