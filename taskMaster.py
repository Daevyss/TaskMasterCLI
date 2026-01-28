import json
import os
import sys
from datetime import datetime


#!/usr/bin/env python3
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  #Me aseguro que busque el archivo json en el directorio en el que esta el .py
FILE = os.path.join(BASE_DIR, "tasks.json")


#Método para leer el json
def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

#Método para escribir en el json una vez hecho los cambios
def save_tasks(tasks):
    with open (FILE, "w") as f:
        json.dump(tasks, f, indent=2)


#Método para la funcionalidad de añadir tareas
def add_tasks(task):
    datos = load_tasks()
    task_id= len(datos)+1        #El ID es más bien el orden de las tareas mas que un identificador único
    datos.append({
        "id": task_id,
        "description": task,
        "status": "toDo",
        "createdAt": datetime.now().isoformat(),  #la función isoformat formatea el datetime para que pueda ser escrito en un json, ya que datetime es de tipo class datetime
        "updatedAt": datetime.now().isoformat(),
        })
    
    save_tasks(datos)
    print (f"Tarea agregada correctamente")
    
#Método para listar todas las tareas
def list_tasks():
    tasks = load_tasks()
    for task in tasks:
        status = "✔" 
        if task["status"] =="done":
            status= "✔"
        elif task["status"] =="toDo":
            status="to-Do"
        elif task["status"]=="in progress":
            status="in progress"
        else: 
            status = "?"


        print(f'{task["id"]}. [{status}] {task["description"]}')

#Método para listar las tareas dependiendo de su estado
def list_filter_tasks(status_requested):
    tasks = load_tasks()
    if status_requested.lower() == "done":
        for task in tasks:
            status = "✔" 
            if task["status"] =="done":
                status= "✔"
                print(f'{task["id"]}. [{status}] {task["description"]}')
            else: 
                continue

    elif status_requested.lower() == "todo":
        for task in tasks:
            status = "✔" 
            if task["status"] =="toDo":
                status= "to-Do"
                print(f'{task["id"]}. [{status}] {task["description"]}')
            else: 
                continue
    
    elif status_requested.lower() == "in-progress":
        for task in tasks:
            status = "✔" 
            if task["status"] =="in progress":
                status= "in progress"
                print(f'{task["id"]}. [{status}] {task["description"]}')
            else: 
                continue
    else:
        print(f"El estado {status_requested} no se reconoce, los estados posibles son: toDo, done y in-progress")

#Método para borrar una tarea por su ID
def delete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task_id == task["id"]:
            del tasks[task_id-1]
            print("Tarea borrada correctamente")
            for i,task in enumerate(tasks):
                task["id"] = i+1
            save_tasks(tasks)
            return

    print("No se ha encontrado ninguna tarea con ese ID")


#Método para borrar todas las tareas
def delete_alltasks():
    datos_vacios= []
    respuesta = input("Esta seguro de que quiere borrar todos los datos de la lista?Y/N")
    if respuesta == "Y" or "y":
        save_tasks(datos_vacios)
        print("Los datos de la lista se han borrado correctamente")
    elif respuesta == "N" or "n":
        print("Los datos no se han borrado")
    
    else:
        print("Por favor, introduce una respuesta valida")

#Método para actualizar una tarea mediante su ID
def update_task(task_id, update):
    tasks = load_tasks()
    for task in tasks:
        if task_id == task["id"]:
            task["description"]= update
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("La tarea se ha actualizado correctamente")
            return
    print("No se ha encontrado ninguna tarea con ese ID")


#Metodo para cambiar el estado a done de una tarea mediante su ID
def mark_task_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task_id == task["id"]:
            task["status"]= "done"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("La tarea se ha actualizado correctamente")
            return
    print("No se ha encontrado ninguna tarea con ese ID")

#Metodo para cambiar el estado a in-progress de una tarea mediante su ID
def mark_task_ip(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task_id == task["id"]:
            task["status"]= "in progress"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("La tarea se ha actualizado correctamente")
            return
    print("No se ha encontrado ninguna tarea con ese ID")

#Aquí manejo todo el funcionamiento de la app, sys.argv recoge los comandos
def main(): 
    #tutorial si solo escribe el comando del programa "taskmaster"
    if len(sys.argv) < 2:
        print("Uso:")
        print(" taskMaster add \"Tarea\"")
        print(" taskMaster list")
        print(" taskMaster list \"Status\"")
        print(" taskMaster delete \"Id-Tarea\"")
        print(" taskMaster delete-all")
        print(" taskMaster update \"Id-Tarea\" \"Tarea-actualizada\"")
        print(" taskMaster mark-done \"Id-Tarea\"")
        print(" taskMaster mark-in-progress \"Id-Tarea\"")
        return
    
    #manejo de funcionalidades dependiendo del segundo comando
    command = sys.argv[1]
    if command == "add":
        if len (sys.argv) < 3:
            print("Error: Debes añadir una tarea")
            return
        task_title = sys.argv[2]
        add_tasks(task_title)
    elif command == "list":
        if len (sys.argv) < 3:
            list_tasks()
        else:
            list_filter_tasks(sys.argv[2])
    elif command == "delete":
        delete_task(int(sys.argv[2]))
    elif command == "delete-all":
        delete_alltasks()
    elif command == "update":
        update_task(int(sys.argv[2]), sys.argv[3])
    elif command == "mark-done":
        mark_task_done(int(sys.argv[2]))
    elif command == "mark-in-progress":
        mark_task_ip(int(sys.argv[2]))

if __name__ == "__main__":
    main()






