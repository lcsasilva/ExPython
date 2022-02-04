import math

ang = float(input('Digite o ângulo: '))

print('Seno: {:.2f}, Cosseno: {:.2f},Tangente: {:.2f}'.format(math.sin(math.radians(ang)),
                                math.cos(math.radians(ang)),
                                math.tan(math.radians(ang))))
