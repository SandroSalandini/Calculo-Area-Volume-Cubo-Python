#programa feito para calcular área e volume de um cubo
from Calculadora import Calculadora
from Cubo import Cubo

calc = Calculadora()

base: float = float(input('Qual o valor da base?'))
profundidade: float = float(input('Qual o valor do profundidade?'))
altura: float = float(input('Qual o valor da altura?'))

cubo = Cubo(base, altura, profundidade)

print('A área do cubo é de (cm²):', calc.calcular_area_cubo (cubo.base, cubo.altura)
    )

print('O volume do cubo é de (cm³):', calc.calcular_volume_cubo (cubo.base, cubo.altura, cubo.profundidade)

)