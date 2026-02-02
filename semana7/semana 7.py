
class Libro:
    def __init__(self, titulo, autor):
        
        #Constructor:
        #Inicializa los atributos básicos del libro.
        #Se ejecuta cuando se crea un objeto Libro.
        
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def __del__(self):
        #Destructor:
        #Se ejecuta cuando el objeto Libro es eliminado de memoria.
        #Aquí solo se registra el evento (simulación).
        
        print(f"El libro '{self.titulo}' fue eliminado del sistema.")
class Usuario:
    def __init__(self, nombre):
        
        #Constructor:
        #Inicializa el nombre del usuario y su lista de libros prestados.
        
        self.nombre = nombre
        self.libros_prestados = []

    def __del__(self):
        
        #Destructor:
        #Se ejecuta cuando el objeto Usuario deja de existir.
        #Útil para registrar actividad o liberar recursos.
        
        print(f"El usuario '{self.nombre}' ha salido del sistema.")
class PrestamoService:
    def __init__(self, ruta_log="prestamos.log"):
        
        #Constructor:
        #Abre un archivo de registro para guardar las operaciones.
        #3Este recurso debe cerrarse correctamente.
        
        self.archivo_log = open(ruta_log, "a", encoding="utf-8")
        self.archivo_log.write("=== Sistema de Préstamos Iniciado ===\n")

    def prestar_libro(self, usuario, libro):
        if not libro.prestado:
            libro.prestado = True
            usuario.libros_prestados.append(libro)
            self.archivo_log.write(
                f"Libro '{libro.titulo}' prestado a {usuario.nombre}\n"
            )
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}")
        else:
            print("El libro ya está prestado.")

    def devolver_libro(self, usuario, libro):
        if libro in usuario.libros_prestados:
            libro.prestado = False
            usuario.libros_prestados.remove(libro)
            self.archivo_log.write(
                f"Libro '{libro.titulo}' devuelto por {usuario.nombre}\n"
            )
            print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}")
        else:
            print("El usuario no tiene este libro.")

    def __del__(self):
        """
        Destructor:
        Se ejecuta cuando el servicio es destruido.
        Cierra el archivo de registro para liberar el recurso.
        """
        self.archivo_log.write("=== Sistema de Préstamos Finalizado ===\n")
        self.archivo_log.close()
        print("Archivo de registro cerrado correctamente.")
#from modelos.libro import Libro
#from modelos.usuario import Usuario
#from servicios.prestamo_service import PrestamoService

def main():
    # Creación de objetos (se ejecutan los constructores __init__)
    usuario = Usuario("Carlos Pérez")
    libro1 = Libro("1984", "George Orwell")

    servicio = PrestamoService()

    # Uso del sistema
    servicio.prestar_libro(usuario, libro1)
    servicio.devolver_libro(usuario, libro1)

    # Eliminación explícita de objetos para evidenciar destructores
    del servicio
    del libro1
    del usuario

if __name__ == "__main__":
    main()
# Sistema de Préstamo de Libros – Semana 7

#Este proyecto demuestra el uso de constructores (__init__) y destructores (__del__) en Python,
#aplicando una arquitectura de Modelos y Servicios.

## Estructura
#modelos: contiene las entidades del sistema (Libro, Usuario)
#servicios: contiene la lógica del negocio (PrestamoService)
#main.py: punto de entrada del programa

## Ejecución
#bash
#python main.py
