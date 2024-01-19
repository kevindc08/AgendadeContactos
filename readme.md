# Agenda de Contactos
Este programa nos podría gestionar información de contactos, como nombres, teléfono celular, teléfono fijo, correos electrónicos y usuario de github. Podría permitir la adición, modificación y eliminación de contactos, además de buscar y mostrar la lista de contactos.

Primero debes crear una instancia de la clase. Aquí hay un ejemplo simple de cómo podrías hacerlo:

```class AgendaContactos:
    def _init_(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono, correo):
        self.contactos[nombre] = {'telefono': telefono, 'correo': correo}

    def mostrar_contactos(self):
        for nombre, info in self.contactos.items():
            print(f'{nombre}: Teléfono - {info["telefono"]}, Correo - {info["correo"]}')
 Crear una instancia de la clase AgendaContactos
mi_agenda = AgendaContactos()

 Agregar contactos
mi_agenda.agregar_contacto('Juan', '123-456-7890', 'juan@email.com')
mi_agenda.agregar_contacto('Maria', '987-654-3210', 'maria@email.com')

 Mostrar la lista de contactos
mi_agenda.mostrar_contactos()
```
Para ejecutar un programa en Visual Studio Code con Python, necesitarás tener instalado lo siguiente:

Python: Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde el sitio oficial de Python
Visual Studio Code: Descarga e instala Visual Studio Code desde su sitio oficial
Extensiones de Python en VSCode: Instala la extensión de Python para Visual Studio Code. Puedes hacer esto desde la pestaña de extensiones en VSCode.

_kevinDC_

