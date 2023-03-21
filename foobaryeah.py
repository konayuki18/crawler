class FooBar():
    def __init__(self, n):
            self.n = n

    def foo(self):
        for i in range(self.n):
            print("foo")
 
    def bar(self):
        for i in range(self.n):
            print("bar")

    def yeah(self):
        for i in range(self.n):
            print("yeah")

n = 1
foobaryeah = FooBar(1)
b = str(foobaryeah.foo())
c = str(foobaryeah.bar())
d = str(foobaryeah.yeah())


print(b)
