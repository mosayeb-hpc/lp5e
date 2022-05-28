class DFLR:
    def dflr(self, klass):
        here = [klass]
        for sup in klass.__bases__:
            here += self.dflr(sup)
        return here


class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

