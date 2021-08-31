import json

def ajoutChapitre(json_file_name):
    data={}
    with open(json_file_name, encoding='utf-8') as json_input:
        data=json.load(json_input)            
        for competence in data :
            competence['Chapitre'] = ""

    with open(json_file_name,"w", encoding='utf-8') as json_output:
        json.dump(data, json_output, ensure_ascii=False, indent=4)

ajoutChapitre("BACPRO_Sciences_2nde.json")
