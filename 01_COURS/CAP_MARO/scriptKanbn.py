import json
import os

def initKanbn(projectName):
    path = os.path.abspath(".")
    folder = ".kanbn/tasks"
    os.makedirs(folder)
    #os.path.join(path, "/.kanbn")
    enteteIndex = "---\ncustomFields:\n  -\n    name: Module\n    type: string\n  -\n    name: Rang\n    type: number\nstartedColumns:\n  - 'En Cours'\ncompletedColumns:\n  - Terminé\n---\n\n# "+projectName+"\n\n## Prévu\n\n"
    with open(".kanbn/index.md", "w", encoding='utf-8') as index:
        index.write(enteteIndex)

def createTask(json_file_name):
    with open(json_file_name, encoding='utf-8') as json_input:
        data=json.load(json_input)
            
        for competence in data :
            titre=competence['Chapitre'].lower().replace(" ", "-")
            taskfile = titre+".md"
            taskpath  = ".kanbn/tasks/"+taskfile
            if taskfile not in os.listdir(".kanbn/tasks") and titre != "":                
                taskline = "- ["+titre+"]"+"(tasks/"+taskfile+")\n"
                with open(".kanbn/index.md", "a", encoding='utf-8') as index:
                    index.write(taskline)            
                with open(taskpath, "w",encoding='utf-8') as newTask:
                    taskContent = "---\ntags:\n  - '"+competence['Domaine']+"'\nRang: 0\n---\n\n# "+competence['Chapitre']+"\n\n## Sub-tasks\n"
                    newTask.write(taskContent)
                    
            with open(taskpath, "a",encoding='utf-8') as task:
                taskContent = "\n- [ ] Capacité: "+competence['Capacité']
                if competence['Connaissance'] :
                    taskContent += "\n- [ ] Connaissance: "+competence['Connaissance']
                task.write(taskContent)

def closeIndex():
    other_columns = "\n## En Préparation\n\n## En Cours\n\n## Terminé\n"
    with open(".kanbn/index.md", "a", encoding='utf-8') as index:
        index.write(other_columns)


initKanbn("CAPtest")
createTask("CAP_Maths_list.json")
closeIndex()


# with open("sequencesSciences.json","w", encoding='utf-8') as json_output:
#     json.dump(data, json_output, ensure_ascii=False)


