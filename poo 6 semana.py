# Proyecto de Ejemplo – Programación Orientada a Objetos en Python

Este proyecto cumple con los requisitos solicitados: herencia, encapsulación, polimorfismo, buena organización y comentarios explicativos.

---

##  Estructura del Proyecto

```
proyecto_poo/
│
├── modelos/
│   ├── persona.py
│   └── estudiante.py
│── servicios/
│   └── gestor_personas.py
│
└── main.py
```

---

## 📄 modelos/persona.py


# Clase base que representa una Persona
class Persona:
    def __init__(self, nombre, edad):
        # Atributos encapsulados (privados)
        self.__nombre = nombre
        self.__edad = edad

    # Métodos getter (encapsulación)
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Método que será sobrescrito (polimorfismo)
    def presentarse(self):
        return f"Hola, soy {self.__nombre} y tengo {self.__edad} años."
```

---

##  modelos/estudiante.py


# Clase derivada que hereda de Persona
from modelos.persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # Llamada al constructor de la clase base
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Método sobrescrito (polimorfismo)
    def presentarse(self):
        return f"Soy {self.get_nombre()}, estudio {self.carrera} y tengo {self.get_edad()} años."
```

---

##  servicios/gestor_personas.py


# Clase de servicio que maneja la lógica del sistema
class GestorPersonas:
    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def mostrar_presentaciones(self):
        # Polimorfismo: se llama al mismo método en diferentes objetos
        for persona in self.personas:
            print(persona.presentarse())
```

---

## ▶️ main.py


from modelos.persona import Persona
from modelos.estudiante import Estudiante
from servicios.gestor_personas import GestorPersonas

# Crear instancias de las clases
persona1 = Persona("Carlos", 40)
estudiante1 = Estudiante("Ana", 21, "Ingeniería")

# Crear gestor de personas
gestor = GestorPersonas()
gestor.agregar_persona(persona1)
gestor.agregar_persona(estudiante1)

# Ejecutar la aplicación
gestor.mostrar_presentaciones()
```

---

