#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Octubre 2023
#==============================

#==== Clsase ClienteBancario ====
class ClienteBancario:
	__nombres:str = None
	__apellidos:str = None
	__edad:int = 0
	__balanceDeCuenta:float = 0.0

	def __init__(self, nombres:str, apellidos:str, edad:int=0, balanceDeCuenta:float=0.0):
		self.__validarEdad(edad)
		self.__validarCantidad(balanceDeCuenta)
		self.nombres = nombres
		self.apellidos = apellidos
		self.__edad = edad
		self.balanceDeCuenta = balanceDeCuenta
	def getNombreCompleto(self) -> str:
		return self.nombres + " " + self.apellidos
	def __mandarEmail(self, titulo:str, texto:str) -> None:
		print("mandar email: " + titulo + "con texto: " + texto)
	def __enviarBalanceAlBanco(self, cantidad:float) -> None:
		print("Enviando cantidad: " + str(cantidad) + "al banco...")


