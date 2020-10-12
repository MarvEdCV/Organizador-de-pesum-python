class Curso:
    def __init__(self, cod, nom,preq,opc,semstr,cred,est):
        self.codigo = cod
        self.nombre = nom
        self.pre_requisitos= preq
        self.opcionalidad=opc
        self.semestre=semstr
        self.creditos=cred
        self.estado=est
