import json
import os
import sys

#!/usr/bin/env python3
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, "tasks.json")

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open (FILE, "w") as f:
        json.dump(tasks, f, indent=2)



def add_tasks(task):
    datos = load_tasks()
    task_id= len(datos)+1
    datos.append({
        "id": task_id,
        "description": task,
        "status": "todo",
        "createdAt": 12
        
        })
    
    save_tasks(datos)
    print (f"Tarea agregada correctamente")
    

def list_tasks():
    tasks = load_tasks()
    for task in tasks:
        status = "✔" 
        if task["status"=="done"]:
            status= "✔"
        elif task["status"=="todo"]:
            status="to-do"
        elif task["status"=="in progress"]:
            status="in progress"


        print(f'{task["id"]}. [{status}] {task["title"]}')
        

def delete_alltasks():
    datos_vacios= []
    respuesta = input("Esta seguro de que quiere borrar todos los datos de la lista?Y/N")
    if respuesta == "Y" or "y":
        save_tasks(datos_vacios)
        print("Los datos de la lista se han borrado correctamente")
    elif respuesta == "N":
        print("Los datos no se han borrado")
    
    else:
        print("Por favor, introduce una respuesta valida")



def main(): 
    if len(sys.argv) < 2:
        print("Uso:")
        print(" taskMaster add \"Tarea\"")
        print(" taskMaster list")
        print(" taskMaster delete-all")
        return
    

    command = sys.argv[1]
    if command == "add":
        if len (sys.argv) < 3:
            print("Error: Debes añadir una tarea")
            return
        task_title = sys.argv[2]
        add_tasks(task_title)
    elif command == "list":
        list_tasks()
    elif command == "delete-all":
        delete_alltasks()

if __name__ == "__main__":
    main()






