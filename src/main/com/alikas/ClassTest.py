
print("starting script...")

class AbsClass:

    def __init__(self):
        print("created abs class")

    def __fun(self):
        print("not from outside call")


class MyFirstClass:
    pass

    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)

    @staticmethod
    def fun1():
        print("fun1")

    def fun(self):
        print("fun with self")


if __name__ == "__main__":
    print("from main")
    mfc = MyFirstClass(3)
    print(mfc)
    mfc.fun()
    MyFirstClass.fun1()

    abs = AbsClass()
    print(dir(abs))
    abs._AbsClass__fun()