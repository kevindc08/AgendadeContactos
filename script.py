# %% [markdown]
# # Agenda de contacto

# %% [markdown]
# ## Este programa realiza lo siguiente:
# -Almacena un contacto que devera contener nombre comleto, telefono fijo movil, correo elecrtronico y usuario de GitHub

# %%
class contacto: #deficion de la clase contacto con atributos:nombre, telefono fijo, telefono movil, correo y github
    def __init__(self,nombre, telefono_fijo, telefono_movil, correo, github):
        self.nombre = nombre
        self.telefono_fijo = telefono_fijo
        self.telefono_movil = telefono_movil
        self.correo = correo
        self.github = github

class Agendacontactos: #definicion a la clase Agendacontactos con una lista para almacenar contactos
    def __init__(self):
        self.contactos= []

    def agrega_contacto(self, contacto): #modo para agregar un contacto a la lista
        self.contactos.append(contacto)

    def mostrar_contactos(self): #metodo para mostrar la lista de contactos 
        for contacto in self.contactos:
            print(f"nombre: {contacto.nombre}")
            print(f"telefono fijo: {contacto.telefono_fijo}")
            print(f"telefono movil: {contacto.telefono_movil}")
            print(f"correo electronico: {contacto.correo}")
            print(f"usuario github: {contacto.github}")
            print("")
            
    def buscar_por_github(self, username): #metodo para buscar un contacto por el nombre 
        for contacto in self.contactos:
            if contacto.nombre == username:
                print(f"usuario encontrado:")
                print(f"nombre: {contacto.nombre}")
                print(f"telefono fijo: {contacto.telefono_fijo}")
                print(f"telefono movil: {contacto.telefono_movil}")
                print(f"correo electronico: {contacto.correo}")
                print(f"usuario github: {contacto.github}")
                return
            print("usuario no encontrado")

# %%
agenda= Agendacontactos() # creacion de una instancia a la clase Agendacontactos 
# creacion de dos instancias de la clase contacto y agregar a la agenda 
contacto1= contacto("Juan Perez", "5050395820", "5590567459", "Juan28@gmail.com", "JuanGitGUb")
contacto2= contacto("Maria Lopez", "6890659094", "5625145360", "Maria08@fmail.com", "MariaGitHub")
agenda.agrega_contacto(contacto1)
agenda.agrega_contacto(contacto2)

# %%
print("Lista de contactos:")
agenda.mostrar_contactos() #muestra la lista de contactos agendada

# %%
username_buscar="Maria Lopez" #solicitar al usuario que ingrese su nombre para buscar 
print(f"\n Buscando usuario GitHub '{username_buscar}':")
agenda.buscar_por_github(username_buscar) #buscar el usuario por el nombre en la agenda y mostrar la informacion si se encuentra 


