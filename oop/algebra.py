import math


class Complex:
    def __init__(self, fst: float, snd: float):
        self.__coords = (float(fst), float(snd))

    @property
    def re(self) -> float:
        return self.__coords[0]

    @property
    def im(self) -> float: 
        return self.__coords[1]

    @property
    def modulus(self) -> float: 
        return self.__coords[0]

    @property
    def phase(self) -> float: 
        return self.__coords[1]

    def to_polar(self) -> "Complex": 
        return self
    
    def to_cartesian(self) -> "Complex": 
        return self
    
    def conjugate(self) -> "Complex": 
        return self.cartesian(self.re, -self.im)

    def __add__(self, other: "Complex") -> "Complex": 
        return self.cartesian(self.re + other.re, self.im + other.im)
    
    def __neg__(self) -> "Complex": 
        return self.cartesian(-self.re, -self.im)
    
    def __sub__(self, other: "Complex") -> "Complex": 
        return self + (-other)

    def __mul__(self, other: "Complex") -> "Complex": 
        return self.polar(self.modulus * other.modulus, self.phase + other.phase)
    
    def __truediv__(self, other: "Complex") -> "Complex": 
        return self.polar(self.modulus / other.modulus, self.phase - other.phase)
    
    def __abs__(self) -> float: 
        return self.modulus
    
    @classmethod
    def polar(cls, modulus: float, phase: float) -> "Complex":
        return PolarComplex(modulus, phase)

    @classmethod
    def cartesian(cls, modulus: float, phase: float) -> "Complex": 
        return CartesianComplex(modulus, phase)
    
    def __eq__(self, other):
        return isinstance(other, Complex) and \
            ((self.re == other.re and self.im == other.im) or \
            (self.modulus == other.modulus and self.phase == other.phase))

    def __hash__(self):
        return hash(self.__coords)
    
    def __repr__(self):
        return f"{type(self).__name__}({', '.join(str(c) for c in self.__coords)})"


class CartesianComplex(Complex):
    def __init__(self, re: float, im: float):
        super().__init__(re, im)

    @property
    def modulus(self) -> float:
        return math.hypot(self.re, self.im)

    @property
    def phase(self) -> float:
        return math.atan2(self.im, self.re)
    
    def to_polar(self) -> "PolarComplex":
        self.polar(self.modulus, self.phase)

    def __str__(self):
        sign = '+' if self.im >= 0.0 else '-'
        im = abs(self.im)
        im = str(im) if im != 1.0 else ""
        return f"{self.re} {sign} i{im}" if self.im != 0.0 else str(self.re)


class PolarComplex(Complex):
    @staticmethod
    def __normalize_angle(angle: float) -> float:
        return (angle + math.pi) % (2 * math.pi) - math.pi

    def __init__(self, modulus: float, phase: float):
        super().__init__(modulus, PolarComplex.__normalize_angle(phase))

    @property
    def re(self) -> float:
        return self.modulus * math.cos(self.phase)

    @property
    def im(self) -> float:
        return self.modulus * math.cos(self.phase)
    
    def to_cartesian(self):
        return self.cartesian(self.re, self.im)
    
    def __str__(self):
        sign = '' if self.phase >= 0.0 else '-'
        return f"{self.modulus} * e^{sign}i{abs(self.phase)}" if self.phase != 0.0 else str(self.modulus)


if __name__ == "__main__":
    z = Complex.polar(2, math.pi / 4)
    print(z) # 2.0 * e^i0.7853981633974483
    print(z.modulus) # 2.0
    print(z.phase) # 0.7853981633974483
    print(z.to_cartesian()) # 1.4142135623730951 + i1.4142135623730951
    print(z.re) # 1.4142135623730951
    print(z.im) # 1.4142135623730951
    print(z is z.to_polar()) # True
    print(z.conjugate()) # 1.4142135623730951 - i1.4142135623730951
    print(z + z) # 2.8284271247461903 + i2.8284271247461903
    print(z - z) # 0.0
    print(z * z) # 4.0 * e^i1.5707963267948966
    print(z / z) # 1.0
    print(abs(z)) # 2.0
    print(z + z == z * Complex.cartesian(2, 0)) # True