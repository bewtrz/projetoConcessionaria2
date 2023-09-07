from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Veiculo(db.Model):
    __tablename__ = 'veiculos'
    Id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100))
    cor = db.Column(db.String(50))
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    ano_fabricacao = db.Column(db.String(50))
    estado = db.Column(db.String(50))
    quilometragem = db.Column(db.String(10))
    passagem = db.Column(db.String(50))
    pagamento = db.Column(db.String(100))
    
    def __init__(self, tipo:int, cor:str, marca:str, modelo:str, anoFabricacao:str, novo:bool, kmRodados:int, leilao:bool,parcela:bool ):
        self.tipo = tipo
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = anoFabricacao
        self.estado = novo
        self.quilometragem = kmRodados
        self.passagem = leilao
        self.pagamento = parcela

    @property
    def serialize(self):
        return {
            'Id': self.Id,
            'Tipo': self.tipo,
            'Cor': self.cor,
            'Marca': self.marca,
            'Modelo': self.modelo,
            'AnoFabricacao': self.ano_fabricacao,
            'Novo': self.estado,
            'KmRodados': self.quilometragem,
            'Leilao': self.passagem,
            'Parcela': self.pagamento
        }