from copy import deepcopy

class poly:
    coeffs: [float]

    def __init__(self, coeffs):
        self.coeffs = coeffs

    def eval(self, x) -> float:
        return sum(map(lambda c: c[1] * pow(x, c[0]), enumerate(self.coeffs)))

    def derivative(self):
        re = deepcopy(self)
        re.coeffs = list(map(lambda c: c[0] * c[1], enumerate(self.coeffs)))[1:]
        return re
        
    def __mul__(self, r: 'poly') -> 'poly':
        if type(r) == float:
            return poly(list(map(lambda x: x * r, self.coeffs)))
        re = [0 for _ in range(len(r.coeffs) + len(self.coeffs) - 1)]
        for i, c0 in enumerate(r.coeffs):
            for j, c1 in enumerate(self.coeffs):
                re[i+j] += c0*c1
        return poly(re)

    def apply_newtons(self, x=-1, precision=4) -> float:
        derivative = self.derivative()
        cutoff = pow(10,-precision)
        y = cutoff + 1
        iterations=0
        while abs(y) > cutoff and iterations < 40:
            y = self.eval(x)
            x -= y / derivative.eval(x)
            iterations+=1
        return x

    def __add__(self, r: 'poly') -> 'poly':
        def add(long, short) -> [float]:
            for i, c in enumerate(short):
                long[i]+=c
            return long

        return poly(add(self.coeffs, r.coeffs) if len(self.coeffs) > len(r.coeffs) else add(r.coeffs, self.coeffs))

    def __repr__(self):
        return str(self)

    def __str__(self):
        supers="¹²³⁴⁵⁶⁷⁸⁹"
        sign=["+ ","- ",]
        return str(self.coeffs[0]) + " " + " ".join(map(lambda c: sign[c[1]<0] +str(abs(c[1]))+"x"+supers[c[0]], enumerate((self.coeffs[1:]))))

class node:
    lo:float
    hi:float
    y:float

    def __init__(self, lo: (float, float), hi: (float,float)):
        self.hi = hi[0]
        self.lo = lo[0]
        self.y = (hi[1] - lo[1]) / (hi[0] - lo[0])

    def next(lo, hi) -> 'node':
        return node((lo.lo, lo.y), (hi.hi, hi.y))

    def __repr__(self):
        return "(" + str(self.lo ) + ".." +str(self.hi) + ") => " + str(self.y)


def build_poly(init: [(float,float)]) -> poly:

    polys = list(map(lambda x: poly([-x[0],1]), init[:-1]))

    for i in range(len(polys) - 1):
        polys[i+1] = polys[i] * polys[i+1]


    polys.insert(0, poly([1]))

    points = list(map(node, init[:-1], init[1:]))
    coeffs = [init[0][1]]

    while len(points) > 0:
        coeffs.append(points[0].y)
        points = list(map(node.next, points[:-1], points[1:]))


    final_form = poly([])
    [final_form:=final_form + p* c for c,p in zip(coeffs, polys)]

    return final_form



# points=[(0.1, 1.2), (0.5, 2.7), (0.7, 3.8), (1.2, 4.7), (1.5, 6.0)]
points=[(-2.,8.), (0.,4.), (1.,2.), (3.,-2.)]

p = build_poly(points)

print("Polynomial that passes through the points ", points)
print("\t=> ", p)

for x, y in points:
    print(p.eval(x), y)


poly=poly([-5,-1,1,3])

print("Zero of polynomial", poly,"\n\t=>", poly.apply_newtons())


