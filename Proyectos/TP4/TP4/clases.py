class Ticket:
    def __init__(self, codigo, patente, vehiculo, pago, paisdecobro, distancia):
        self.codigo = codigo
        self.patente = patente
        self.vehiculo = vehiculo
        self.pago = pago
        self.paisdecobro = paisdecobro
        self.distancia = distancia

    def __str__(self):
        r = "CÓDIGO: " + str(self.codigo) + " PATENTE: " + str(self.patente) + " VEHÍCULO: " + str(self.vehiculo)
        r += " PAGO: " + str(self.pago) + " PAIS DE COBRO: " + str(self.paisdecobro) + " DISTANCIA: " + str(self.distancia)
        return r


