import argparse
import logging as lg

from src.json import *
from src.neoj4 import *

# nom des keys a renomer : oldKey : NewKey
dicToRenameKeys = {
    "Course trackÃ©es": "Course trackes",
    "Type de dÃ©part": "Type de depart"
}
lg.basicConfig(level=lg.DEBUG)
# default="courses.json",
def parse_arguments (): 
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--pathFile",  help="""Path to json file""") 
    parser.add_argument("-n", "--nodes", default=["Cheval", "course"], help= """Names of differents Nodes""")
    parser.add_argument("-v", "--verbose", action='store_true', help="""Make the application talk       !""")
    return parser.parse_args()


def main(dicToRenameKeys):
    args = parse_arguments()
    
    if args.verbose: 
        lg.basicConfig(level=lg.DEBUG)
        print("toiot")
        lg.debug("Debbug")
        lg.info("info")
        lg.critical("coucou")

    try: 
        pathFile = args.pathFile
        if pathFile == None : 
            raise Warning("You must indicate a pathFile !")

        # Nettoyage des données 
        datastore = startCleanning(pathFile, dicToRenameKeys)

        # Ajoute des données à Neo4j
        addNewData(datastore)

    except FileNotFoundError as e :
        lg.critical(f"Ow :( The file was not found. Here is the original message of the exception : {e}")

    finally:
        lg.info("############## Analysis is over #############")


if __name__ == "__main__" : 
    main(dicToRenameKeys)