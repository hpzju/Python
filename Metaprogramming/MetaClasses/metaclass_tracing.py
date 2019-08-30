class TracingMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print("TracingMeta.__prepare__(name, bases, **kwargs)")
        print("  mcs =", mcs)
        print("  name =", name)
        print("  bases =", bases)
        print("  kwargs =", kwargs)
        namespace = super().__prepare__(name, bases)
        print("<-- namespace =", namespace)
        print()
        return namespace

    def __new__(mcs, name, bases, namespace, **kwargs):
        print("TracingMeta.__new__(mcs, name, bases, namespace, **kwargs)")
        print("  mcs =", mcs)
        print("  name =", name)
        print("  bases =", bases)
        print("  namespace =", namespace)
        print("  kwargs =", kwargs)
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)
        print("<-- cls =", cls)
        print()
        return cls

    def __init__(cls, name, bases, namespace, **kwargs):
        print("TracingMeta.__init__(cls, name, bases, namespace, **kwargs)")
        print("  cls =", cls)
        print("  name =", name)
        print("  bases =", bases)
        print("  namespace =", namespace)
        print("  kwargs =", kwargs)
        super().__init__(name, bases, namespace)
        print()

    def metamethod(cls):
        print("TracingMeta.metamethod(cls)")
        print("  cls = ", cls)
        print()

    def __call__(cls, *args, **kwargs):
        print("TracingMeta.__call__(cls, *args, **kwargs)")
        print("  cls =", cls)
        print("  args =", args)
        print("  kwargs =", kwargs)
        print("  About to call type.__call__()")
        obj = super().__call__(*args, **kwargs)
        print("  Returned from type.__call__()")
        print("<-- obj =", obj)
        print()
        return obj


class TracingClass(metaclass=TracingMeta):

    def __new__(cls, *args, **kwargs):
        print("  TracingClass.__new__(cls, args, kwargs")
        print("    cls =", cls)
        print("    args =", args)
        print("    kwargs =", kwargs)
        obj = super().__new__(cls)
        print("  <-- obj =", obj)
        print()
        return obj

    def __init__(self, *args, **kwargs):
        print("  TracingClass.__init__(self, *args, **kwargs")
        print("    self =", self)
        print("    args =", args)
        print("    kwargs =", kwargs)
        print()

    def instmethod(self):
        print("TracingClass.instmethod(inst)")
        print("  inst = ", self)
        print()

    @classmethod
    def __call__(cls, *args, **kwargs):
        print("TracingClass.__call__(cls, *args, **kwargs)")
        print("  cls =", cls)
        print("  args =", args)
        print("  kwargs =", kwargs)
        # print("  About to call super().__call__()")
        # obj = super().__call__(*args, **kwargs)
        # print("  Returned from super().__call__()")
        # print("<-- obj =", obj)
        print()
        # return obj


class TC2(TracingClass):

    def __init__(self, *args, **kwargs):
        print("  TC2.__init__(self, *args, **kwargs")
        print("    self =", self)
        print("    args =", args)
        print("    kwargs =", kwargs)
        print()
        self.a = args[0]

    def __call__(self, *args, **kwargs):
        print("TC2.__call__(self, *args, **kwargs)")
        print("  self =", self)
        print("  args =", args)
        print("  kwargs =", kwargs)
        print("  About to call super().__call__()")
        obj = super().__call__(*args, **kwargs)
        print("  Returned from super().__call__()")
        print("<-- obj =", obj)
        print()
        return obj


if __name__ == '__main__':
    print('-----'*20)

    a = TracingClass(1, '1', msg="TracingClass")
    print('======' * 20)
    b = TC2(2, '2', msg='tc2')
    b(3, msg='TC2 instance called')
    print(b.a)
    print('$$$$$' * 20)
    b.instmethod()
    print(dir(b))
    print(dir(b.__class__))
    print(b.__class__.__mro__)
    print('#####' * 20)
    TC2.metamethod()
    print(dir(TC2))
    print(dir(TC2.__class__))
    print(TC2.__mro__)
    print('*****'*20)