# importation des packages py2neo
from py2neo import Graph
from py2neo.data import Node, Relationship

import logging as lg
lg.basicConfig(level=lg.DEBUG)

uri= "bolt://localhost:7687"
auth= ("neo4j", "Toto")

global graph

graph = Graph(uri=uri, auth=auth)
try: 
    graph.run("MATCH (n) RETURN n LIMIT 1")
    lg.info("connection to database ok")
except :
    lg.critical("le server est-il allumé ?")

def addNewData(listOfDict):

    KeyRelation = {"Nom": "Cheval22", "Course trackes": "course22"}

    nodes, relations = formatToCreateNodesAndRelationship(listOfDict, KeyRelation)
    lg.info(nodes)

    lg.info(relations)

    # create nodes
    for add in list(nodes.values()):
        graph.run(f"""MERGE {add}""")

        

    """    # create relationship
    for relation in list(relations.values()):
        graph.run(createRelationShip(relation[0], relation[1], "aParticiperA"))"""

    return True

def formatToCreateNodesAndRelationship(listOfDict, KeyRelation):
    nodes={}
    relations={}
    key1, key2 = KeyRelation.keys()
    name1, name2 = KeyRelation.values()

    for index, oneDict in enumerate(listOfDict):
        
        nodes[oneDict[key1]] = Node(name1, name=oneDict[key1])
        nodes[oneDict[key2]] = Node(name2, name=oneDict[key2])

        relations[index] = [oneDict[key1], oneDict[key2]]
        
    return nodes, relations

def createRelationShip(name1, name2, relationType, nodeName1="Cheval22" , nodeName2="course22"):
    
    return f""" match (a:{nodeName1} {{name:"{name1}"}}) match (b:{nodeName2} {{name:"{name2}"}}) merge (a)-[:{relationType}]->(b)"""

