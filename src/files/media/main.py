from Generators import MauchlyGenerator, FibonacciGenerator, linear_congruential_method, InvCongruentialGenerator, BaysDurhamGenerator
from Generators import Super_Generator


def mauchly_test():
    generator = MauchlyGenerator('1234012340123', 5)
    s = set()
    curr = 0
    while curr not in s:
        s.add(curr)
        curr = generator.next()

    print len(s)


def potential(b, m):
    p = 1
    while b ** p % m != 0:
        p += 1
    print "P : " + str(p)


def linear_test1():
    num = 7
    m = 12
    a = 25
    c = 7

    for i in range(50):
        num = linear_congruential_method(m, a, c, num)
        print num

    b = a - 1
    potential(b, m)


def linear_test2():
    num = 7
    m = 12
    a = 8
    c = 6

    for i in range(20):
        num = linear_congruential_method(12, 8, 6, num)
        print num

    b = a - 1
    potential(b, m)


def fibonacci_test():
    #f = FibonacciGenerator(6, 10, 7) # bad test
    f = FibonacciGenerator(16, 10, 7) # good test
    num = f.next()
    cnt = 0
    while cnt != 50:
        cnt += 1
        next_num = f.next()
        print next_num, cnt


def inv_cong_test():
    g = InvCongruentialGenerator(5, 2, 3, 1)
    for i in range(50):
        print g.next()


def bays_durkham_test():
    g = BaysDurhamGenerator()
    for i in range(50):
        print g.next()


def own_method_test():
    gen = Super_Generator(12, 8, 6, 7)
    for i in range(100):
        print gen.next()

linear_test2()