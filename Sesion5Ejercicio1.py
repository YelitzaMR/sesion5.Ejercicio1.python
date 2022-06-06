def triangulo (h,b):
    area=h*b/2
    print('El areá es:', area)

def circulo (r):
    import numpy
    area=numpy.pi*r**2
    print('El área es:', round (area,2))

triangulo(6,6)
circulo(8)