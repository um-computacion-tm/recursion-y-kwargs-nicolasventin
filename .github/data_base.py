
database = {
            "1":{
                "nombre1":"Pablo",
                "nombre2":"Diego",
                "apellido1":"Ruiz",
                "apellido2":"Picasso"
            },
            "2":{
                "nombre1":"Elio",
                "apellido1":"Anci"
            },
            "3":{
                "nombre1":"Elias",
                "nombre2":"Marcos",
                "nombre3":"Luciano",
                "apellido1":"Marcelo",
                "apellido2":"Gonzalez"
            },
            "4":{
                "nombre1":"Nicolas",
                "nombre2":"Guillermo",
                "apellido1":"Ventin",
                "apellido2":"Elaskar"
            }
}

def buscar_datos(*words, **kwords):
    for num, dic in kwords.items():
        if all(word in dic.values() for word in words) and len(dic.values()) == len(words):
            return num
    return None