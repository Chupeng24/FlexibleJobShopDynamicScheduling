import json

from clItinerary import Itinerary
from clMachine import Machine
from clTask import Task


def parseNewData():
    itinerariesList = []
    savePath = input("请输入数据保存路径：")
    with open(savePath, 'r', encoding="utf8") as input_file:  # read file from path
        importedData = json.loads(input_file.read())
    imitineraryName = importedData['itineraryName']
    imtaskList = importedData['tasksList']
    insertItinerary = Itinerary()
    insertItinerary.name = imitineraryName
    for i, taskDict in enumerate(imtaskList):
        taskMachine = imtaskList[i]['taskMachine']
        insertItinerary.tasksList.append(Task(imtaskList[i]['taskName'],
                                              float(imtaskList[i]['taskDuration']),
                                              Machine(taskMachine["machineName"])))
    itinerariesList.append(insertItinerary)
    return itinerariesList