import json

from clItinerary import Itinerary
from clMachine import Machine
from clTask import Task


def parseData():
    """Tries to import JSON JobShop PRO file to program"""
    machinesList = []
    itinerariesList = []
    savePath = input("请输入数据保存路径：")

    with open(savePath, 'r', encoding="utf8") as inputfile:  # read file from path
        importedData = json.loads(inputfile.read())

    if list(importedData.keys()) == ["itineraries", "machines"]:
        imMachines = importedData['machines']  # is first level structure is correct, then split
        imItineraries = importedData['itineraries']

        if len(list(imMachines)) > 0 and len(list(imItineraries)) > 0:
            for index, dictMachine in enumerate(imMachines):
                machinesList.append(Machine(imMachines[index]['machineName']))

            for _, dictItinerary in enumerate(imItineraries):  # for each itinerary check structure
                tmpItinerary = Itinerary()
                tmpItinerary.name = dictItinerary['itineraryName']
                tmpItineraryTasks = dictItinerary['tasksList']
                for i, taskDict in enumerate(tmpItineraryTasks):  # check structure of each task in itinerary
                    if list(tmpItineraryTasks[i].keys()) == ['taskName', 'taskMachine', 'taskDuration']:
                        taskMachine = tmpItineraryTasks[i]['taskMachine']

                        if list(taskMachine.keys()) == ["machineName"]:  # check corectness of elements
                            tmpItinerary.tasksList.append(Task(tmpItineraryTasks[i]['taskName'],
                                                                           float(tmpItineraryTasks[i]['taskDuration']),
                                                                           # parse values to taskList
                                                                           Machine(taskMachine["machineName"])))
                        # add itinerary to global list, beacuse parsing finished
                itinerariesList.append(tmpItinerary)

    return machinesList, itinerariesList