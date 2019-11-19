class Calculadora:
    area_cubo: float
    volume_cubo: float

    def calcular_area_cubo(self, base, altura):
        self.area_cubo = base * altura
        if self.area_cubo <= 0:
             print('valores informados de medida(s) inválido(s)!')
        return self.area_cubo

    def calcular_volume_cubo(self, base, altura, profundidade):
        self.volume_cubo = base * altura * profundidade
        if self.volume_cubo <= 0:
             print('valores informados de medida(s) inválido(s)!')
        return self.volume_cubo

