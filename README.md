# Tarea Semana 7: Implementación de Constructores y Destructores en Python

## Descripción general

Este proyecto es un ejemplo sencillo que demuestra el uso de **constructores (`__init__`)** y **destructores (`__del__`)** en Python, aplicando una arquitectura separada en **modelos** y **servicios**, tal como se trabaja en Programación Orientada a Objetos.

El caso planteado simula un **sistema básico de gestión de archivos**, donde:

* Un modelo representa un archivo abierto.
* Un servicio se encarga de crear y cerrar archivos.
* El programa principal muestra claramente cuándo se ejecutan el constructor y el destructor.

---

## Estructura del proyecto

```
proyecto_constructores/
│
├── modelos/
│   └── archivo.py
│
├── servicios/
│   └── archivo_service.py
│
├── main.py
└── README.md
```

---

## modelos/archivo.py

```python
class Archivo:
    def __init__(self, nombre, modo):
        """
        Constructor de la clase Archivo.
        Se ejecuta automáticamente cuando se crea un objeto Archivo.

        Inicializa:
        - nombre del archivo
        - modo de apertura
        - abre el archivo y guarda la referencia
        """
        self.nombre = nombre
        self.modo = modo
        self.archivo = open(nombre, modo)
        print(f"[INIT] Archivo '{self.nombre}' abierto en modo '{self.modo}'.")

    def escribir(self, texto):
        self.archivo.write(texto)

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Se ejecuta cuando el objeto es destruido o deja de existir.

        Intenta realizar la limpieza de recursos:
        - cerrar el archivo si aún está abierto

        Este método puede ejecutarse cuando:
        - el programa finaliza
        - el objeto es eliminado con del
        - el recolector de basura lo detecta sin referencias
        """
        try:
            if not self.archivo.closed:
                self.archivo.close()
                print(f"[DEL] Archivo '{self.nombre}' cerrado correctamente.")
        except AttributeError:
            print("[DEL] El archivo ya había sido cerrado.")

```markdown
# Tarea Semana 7 – Constructores y Destructores en Python

## Descripción
Este proyecto demuestra el uso de los métodos especiales __init__ y __del__ en Python, aplicando una arquitectura separada en modelos y servicios.

## Ejecución
1. Clonar el repositorio
2. Ejecutar:
   python main.py

## Uso de __init__
El constructor se ejecuta al crear un objeto Archivo, inicializando los atributos y abriendo el archivo.

## Uso de __del__
El destructor se ejecuta cuando el objeto es eliminado, cerrando el archivo y liberando recursos.



