import json
import logging as lg
lg.basicConfig(level=lg.DEBUG)


def startCleanning(filepath, dicToRenameKeys):
    datastore = openJson(filepath)

    lenData= len(datastore)
    lg.info(f"data len : {lenData}")

    listAllkeys = AllKeys(datastore)
    lg.info(f"all keys {listAllkeys}")

    for oldKey, newKey in dicToRenameKeys.items():
        datastore = renamekey(datastore, oldKey, newKey)

    listAllkeys = AllKeys(datastore)
    lg.info(f"all keys Clean {listAllkeys}")

    lg.info(numberOfUniqueValues(datastore, listAllkeys))


    return datastore


def openJson(filepath):

    with open(filepath, 'r') as data:
        datastore = json.load(data)

    return datastore

def AllKeys(listOfDict):
    """
    return all keys from the listOfDict
    """
    
    res = []
    for oneDict in listOfDict:
        res.extend(oneDict.keys())
        
    return list(set(res))

def renamekey(listOfDict, oldKey, newKey):
    """Change keys for all document
        
        take : list of dict, oldKey, newKey
        return : list of dict
    """
    for dic in listOfDict:
        if oldKey in dic.keys():
            dic[newKey] = dic.pop(oldKey)
            
    return listOfDict

def uniqueValues(listOfDict, keyName):
    """
    return a list of unique values
    """
    # que faire si keyName n'est pas dans tous les dict
    
    return list(set([oneDict[keyName] for oneDict in listOfDict if type(oneDict[keyName]) in [int, str]]))


def numberOfUniqueValues(listOfDict, listeKey=None):
    """
    return : un résumé des données
    """
    if listeKey:
        listeKey = AllKeys(listOfDict)
    listre = []
    for key in listeKey:
        listre.append(f"Nbre d'élément pour : {key}, {str(len(uniqueValues(listOfDict, key)))}")
    return listre