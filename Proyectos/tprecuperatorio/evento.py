import random


class Evento:
    def __init__(self, codigo, titulo, descripcion, costo, tipo, segmento):
        self.codigo = codigo
        self.titulo = titulo
        self.descripcion = descripcion #cadena separada por espacios en blanco y terminada en un punto
        self.costo = costo
        self.tipo = tipo  #numero de 0 a 19
        self.segmento = segmento  #numero de 0 a 9

    def __str__(self):
        cad = '{:<8} | {:<30} | {:<60} | {:>10.2f} | {:^10} | {:^6} '
        return cad.format(self.codigo, self.titulo, self.descripcion, self.costo, self.tipo, self.segmento)


def encabezado():
    cad = ''
    cad += '{:<8} | {:<30} | {:<60} | {:<10} | {:<10} | {:^10}\n'
    cad += '{}'.format('-' * 150)
    return cad.format('CÓDIGO', 'TÍTULO', 'DESCRIPCIÓN DE EVENTO', 'COSTO', 'TIPO', 'SEGMENTO')


def crearTitulo():
    tipo_de_eventos = ("desastre natural", "hallazgo cientifico ", "descubrimiento social")
    return random.choice(tipo_de_eventos)


def crearDescripcion():
    sujeto = ("Un Policia", "Messi", "Massa", "Milei", "Facu Campazzo", "El capitan de los pumas", "Emilia Mernes", "Duki", "Fito Paez", "un Taxista")
    accion = ("comio una milanesa", "metio un gol", "gano el mundial", "lleno un concierto", "cumplio años", "se lesiono", "Vendio su casa")
    ubicacion = ("España", "Cordoba", "Jujuy", "Buenos aires", "Grecia", "Polonia", "Rio cuarto")
    descr = random.choice(sujeto) + " " + random.choice(accion) + " en " + random.choice(ubicacion) + "."
    return descr