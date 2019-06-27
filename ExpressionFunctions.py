import matplotlib.pyplot as plt
import numpy as np
import os


#PATH = "/Users/LevineMa/Desktop/LAB/Results Expression Morph/"
PATH = ""           #Variable for the path to the files
SAVE = ""           #Variable for the path to save the graphs
resultsList = []    #List to store the names of the files that need to be analyzed

x = []      #Stores the values for the x axis of the graph (Intervals)
yE = []     #Stores the values for the y axis of the graph for the percentage of times the person or people pressed "E"
yI = []

zero_anger_fear = []
two_anger_fear = []
three_anger_fear = []
four_anger_fear = []
five_anger_fear = []
six_anger_fear = []
seven_anger_fear = []
eight_anger_fear = []
ten_anger_fear = []

zero_disgust_surprise = []
two_disgust_surprise = []
three_disgust_surprise = []
four_disgust_surprise = []
five_disgust_surprise = []
six_disgust_surprise = []
seven_disgust_surprise = []
eight_disgust_surprise = []
ten_disgust_surprise = []

zero_anger_sad = []
two_anger_sad = []
three_anger_sad = []
four_anger_sad = []
five_anger_sad = []
six_anger_sad = []
seven_anger_sad = []
eight_anger_sad = []
ten_anger_sad = []

zero_happy_surpr = []
two_happy_surpr = []
three_happy_surpr = []
four_happy_surpr = []
five_happy_surpr = []
six_happy_surpr = []
seven_happy_surpr = []
eight_happy_surpr = []
ten_happy_surpr = []    #Lists for all the different continuua to store data for the analysis

itemAnalysis = {

}   #Dictonary to be used for item analysis

analyses_happy_surpr = {
        0:{
            "e": 0,
            "i": 0
        },
        2:{
            "e": 0,
            "i": 0
        },
        3:{
            "e": 0,
            "i": 0
        },
        4:{
            "e": 0,
            "i": 0
        },
        5:{
            "e": 0,
            "i": 0
        },
        6:{
            "e": 0,
            "i": 0
        },
        7:{
            "e": 0,
            "i": 0
        },
        8:{
            "e": 0,
            "i": 0
        },
       10:{
           "e": 0,
           "i": 0
       }
}   #Stores how often e and i were chosen for the different continuua at different percentages of each part of the continuua

analyses_anger_sad = {
        0:{
            "e": 0,
            "i": 0
        },
        2:{
            "e": 0,
            "i": 0
        },
        3:{
            "e": 0,
            "i": 0
        },
        4:{
            "e": 0,
            "i": 0
        },
        5:{
            "e": 0,
            "i": 0
        },
        6:{
            "e": 0,
            "i": 0
        },
        7:{
            "e": 0,
            "i": 0
        },
        8:{
            "e": 0,
            "i": 0
        },
       10:{
           "e": 0,
           "i": 0
       }
}

analyses_disgust_surprise = {
        0:{
            "e": 0,
            "i": 0
        },
        2:{
            "e": 0,
            "i": 0
        },
        3:{
            "e": 0,
            "i": 0
        },
        4:{
            "e": 0,
            "i": 0
        },
        5:{
            "e": 0,
            "i": 0
        },
        6:{
            "e": 0,
            "i": 0
        },
        7:{
            "e": 0,
            "i": 0
        },
        8:{
            "e": 0,
            "i": 0
        },
       10:{
           "e": 0,
           "i": 0
       }
}

analyses_anger_fear = {
        0:{
            "e": 0,
            "i": 0
        },
        2:{
            "e": 0,
            "i": 0
        },
        3:{
            "e": 0,
            "i": 0
        },
        4:{
            "e": 0,
            "i": 0
        },
        5:{
            "e": 0,
            "i": 0
        },
        6:{
            "e": 0,
            "i": 0
        },
        7:{
            "e": 0,
            "i": 0
        },
        8:{
            "e": 0,
            "i": 0
        },
       10:{
           "e": 0,
           "i": 0
       }
}

def reset():
    #Resets all global variables. Used to switch from the group analysis to individual analyses
    global analyses_disgust_surprise
    global analyses_anger_sad
    global analyses_anger_fear
    global analyses_happy_surpr

    zero_disgust_surprise.clear()
    two_disgust_surprise.clear()
    three_disgust_surprise.clear()
    four_disgust_surprise.clear()
    five_disgust_surprise.clear()
    six_disgust_surprise.clear()
    seven_disgust_surprise.clear()
    eight_disgust_surprise.clear()
    ten_disgust_surprise.clear()

    zero_anger_sad.clear()
    two_anger_sad.clear()
    three_anger_sad.clear()
    four_anger_sad.clear()
    five_anger_sad.clear()
    six_anger_sad.clear()
    seven_anger_sad.clear()
    eight_anger_sad.clear()
    ten_anger_sad.clear()

    zero_anger_fear.clear()
    two_anger_fear.clear()
    three_anger_fear.clear()
    four_anger_fear.clear()
    five_anger_fear.clear()
    six_anger_fear.clear()
    seven_anger_fear.clear()
    eight_anger_fear.clear()
    ten_anger_fear.clear()

    zero_happy_surpr.clear()
    two_happy_surpr.clear()
    three_happy_surpr.clear()
    four_happy_surpr.clear()
    five_happy_surpr.clear()
    six_happy_surpr.clear()
    seven_happy_surpr.clear()
    eight_happy_surpr.clear()
    ten_happy_surpr.clear()


    analyses_disgust_surprise = {
        0: {
            "e": 0,
            "i": 0
        },
        2: {
            "e": 0,
            "i": 0
        },
        3: {
            "e": 0,
            "i": 0
        },
        4: {
            "e": 0,
            "i": 0
        },
        5: {
            "e": 0,
            "i": 0
        },
        6: {
            "e": 0,
            "i": 0
        },
        7: {
            "e": 0,
            "i": 0
        },
        8: {
            "e": 0,
            "i": 0
        },
        10: {
            "e": 0,
            "i": 0
        }
    }
    analyses_anger_sad = {
        0: {
            "e": 0,
            "i": 0
        },
        2: {
            "e": 0,
            "i": 0
        },
        3: {
            "e": 0,
            "i": 0
        },
        4: {
            "e": 0,
            "i": 0
        },
        5: {
            "e": 0,
            "i": 0
        },
        6: {
            "e": 0,
            "i": 0
        },
        7: {
            "e": 0,
            "i": 0
        },
        8: {
            "e": 0,
            "i": 0
        },
        10: {
            "e": 0,
            "i": 0
        }
    }
    analyses_anger_fear = {
        0: {
            "e": 0,
            "i": 0
        },
        2: {
            "e": 0,
            "i": 0
        },
        3: {
            "e": 0,
            "i": 0
        },
        4: {
            "e": 0,
            "i": 0
        },
        5: {
            "e": 0,
            "i": 0
        },
        6: {
            "e": 0,
            "i": 0
        },
        7: {
            "e": 0,
            "i": 0
        },
        8: {
            "e": 0,
            "i": 0
        },
        10: {
            "e": 0,
            "i": 0
        }
    }
    analyses_happy_surpr = {
        0: {
            "e": 0,
            "i": 0
        },
        2: {
            "e": 0,
            "i": 0
        },
        3: {
            "e": 0,
            "i": 0
        },
        4: {
            "e": 0,
            "i": 0
        },
        5: {
            "e": 0,
            "i": 0
        },
        6: {
            "e": 0,
            "i": 0
        },
        7: {
            "e": 0,
            "i": 0
        },
        8: {
            "e": 0,
            "i": 0
        },
        10: {
            "e": 0,
            "i": 0
        }
    }

    x.clear()
    yE.clear()

def parser(filename):
    file = open(os.fspath(PATH + filename), 'r')
    for line in file:
        splitLine = line.split(",")     #Split all the lines in the csv file at commas
        for line in splitLine:          #Loop through all the lines
            lineSplit = line.split("_")
            for word in lineSplit:   #Loop through all the words in the lineSplit
                try:
                    if word[0] == "(":      #If the first letter is a "(" use the try except to see if the next value is an integer
                        try:
                            tenTest = int(word[1])
                            value = int(word[2])    #Check if number is an integer


                            if lineSplit[0] == "anger" and lineSplit[1] == "fear":  #For all times the anger fear continuua is seen, populates the anger_fear lists with how many times e and i were chosen
                                if tenTest == 0 and value == 0:     #Checks if percentage for the continuua is 0% (00)
                                    zero_anger_fear.append(splitLine[12])   #e and i were the value at splitLine[12] in this situation
                                if value == 2:
                                    two_anger_fear.append(splitLine[12])
                                if value == 3:
                                    three_anger_fear.append(splitLine[12])
                                if value == 4:
                                    four_anger_fear.append(splitLine[12])
                                if value == 5:
                                    five_anger_fear.append(splitLine[12])
                                if value == 6:
                                    six_anger_fear.append(splitLine[12])
                                if value == 7:
                                    seven_anger_fear.append(splitLine[12])
                                if value == 8:
                                    eight_anger_fear.append(splitLine[12])
                                if tenTest == 1 and value == 0:     #Checks if percentage for the continuua is 100% (10)
                                    ten_anger_fear.append(splitLine[12])
                            if lineSplit[0] == "disgust" and lineSplit[1] == "surprise" and lineSplit[2] == "male":     #Same as anger fear but does separately for male and female stimuli because the female e and i are backward (i is first stimulus e is second)
                                if tenTest == 0 and value == 0:
                                    zero_disgust_surprise.append(splitLine[12])
                                if value == 2:
                                    two_disgust_surprise.append(splitLine[12])
                                if value == 3:
                                    three_disgust_surprise.append(splitLine[12])
                                if value == 4:
                                    four_disgust_surprise.append(splitLine[12])
                                if value == 5:
                                    five_disgust_surprise.append(splitLine[12])
                                if value == 6:
                                    six_disgust_surprise.append(splitLine[12])
                                if value == 7:
                                    seven_disgust_surprise.append(splitLine[12])
                                if value == 8:
                                    eight_disgust_surprise.append(splitLine[12])
                                if tenTest == 1 and value == 0:
                                    ten_disgust_surprise.append(splitLine[12])
                            elif lineSplit[0] == "disgust" and lineSplit[1] == "surprise" and lineSplit[2] == "female":
                                if tenTest == 0 and value == 0:
                                    if splitLine[12] == "i":
                                        zero_disgust_surprise.append("e")
                                    elif splitLine[12] == "e":
                                        zero_disgust_surprise.append("i")
                                if value == 2:
                                    if splitLine[12] == "i":
                                        two_disgust_surprise.append("e")
                                    elif splitLine[12] == "e":
                                        two_disgust_surprise.append("i")
                                if value == 3:
                                    if splitLine[12] == "i":
                                        three_disgust_surprise.append("e")
                                    elif splitLine[12] == "e":
                                        three_disgust_surprise.append("i")
                                if value == 4:
                                    if splitLine[12] == "i":
                                        four_disgust_surprise.append("e")
                                    elif splitLine[12] == "e":
                                        four_disgust_surprise.append("i")
                                if value == 5:
                                    if splitLine[12] == "i":
                                        five_disgust_surprise.append("e")
                                    elif splitLine[12] == "e":
                                        five_disgust_surprise.append("i")
                                if value == 6:
                                    if splitLine[12] == "i":
                                        six_disgust_surprise.append("e")
                                    elif splitLine[12] == "e":
                                        six_disgust_surprise.append("i")
                                if value == 7:
                                    if splitLine[12] == "i":
                                        seven_disgust_surprise.append("e")
                                    elif splitLine[12] == "e":
                                        seven_disgust_surprise.append("i")
                                if value == 8:
                                    if splitLine[12] == "i":
                                        eight_disgust_surprise.append("e")
                                    elif splitLine[12] == "e":
                                        eight_disgust_surprise.append("i")
                                if tenTest == 1 and value == 0:
                                    if splitLine[12] == "i":
                                        ten_disgust_surprise.append("e")
                                    elif splitLine[12] == "e":
                                        ten_disgust_surprise.append("i")
                            if lineSplit[0] == "anger" and lineSplit[1] == "sad":   #Same as anger fear
                                if tenTest == 0 and value == 0:
                                    zero_anger_sad.append(splitLine[12])
                                if value == 2:
                                    two_anger_sad.append(splitLine[12])
                                if value == 3:
                                    three_anger_sad.append(splitLine[12])
                                if value == 4:
                                    four_anger_sad.append(splitLine[12])
                                if value == 5:
                                    five_anger_sad.append(splitLine[12])
                                if value == 6:
                                    six_anger_sad.append(splitLine[12])
                                if value == 7:
                                    seven_anger_sad.append(splitLine[12])
                                if value == 8:
                                    eight_anger_sad.append(splitLine[12])
                                if tenTest == 1 and value == 0:
                                    ten_anger_sad.append(splitLine[12])
                            if lineSplit[0] == "happy" and lineSplit[1] == "surpr":     #Same as anger fear
                                if tenTest == 0 and value == 0:
                                    zero_happy_surpr.append(splitLine[12])
                                if value == 2:
                                    two_happy_surpr.append(splitLine[12])
                                if value == 3:
                                    three_happy_surpr.append(splitLine[12])
                                if value == 4:
                                    four_happy_surpr.append(splitLine[12])
                                if value == 5:
                                    five_happy_surpr.append(splitLine[12])
                                if value == 6:
                                    six_happy_surpr.append(splitLine[12])
                                if value == 7:
                                    seven_happy_surpr.append(splitLine[12])
                                if value == 8:
                                    eight_happy_surpr.append(splitLine[12])
                                if tenTest == 1 and value == 0:
                                    ten_happy_surpr.append(splitLine[12])

                        except ValueError or IndexError:          #If the second letter in the word isn't an integer an error will be thrown and if that error is thrown do nothing
                            value = 0
                except IndexError:
                    value = 0

def analysis(continua, list0, list2, list3, list4, list5, list6, list7, list8, list10):

    for value in list0:     #Converts all the times e and i occur at each percentage value to a number by incrementing an e or i value in a dictionary. Same thing for other lists
        if value == "e":    #For each e or i in the 0% list it increments the appropriate value in the dictionary by 1. Same for other lists
            continua.get(0)["e"] += 1
        if value == "i":
            continua.get(0)["i"] += 1
    for value in list2:
        if value == "e":
            continua.get(2)["e"] += 1
        if value == "i":
            continua.get(2)["i"] += 1
    for value in list3:
        if value == "e":
            continua.get(3)["e"] += 1
        if value == "i":
            continua.get(3)["i"] += 1
    for value in list4:
        if value == "e":
            continua.get(4)["e"] += 1
        if value == "i":
            continua.get(4)["i"] += 1
    for value in list5:
        if value == "e":
            continua.get(5)["e"] += 1
        if value == "i":
            continua.get(5)["i"] += 1
    for value in list6:
        if value == "e":
            continua.get(6)["e"] += 1
        if value == "i":
            continua.get(6)["i"] += 1
    for value in list7:
        if value == "e":
            continua.get(7)["e"] += 1
        if value == "i":
            continua.get(7)["i"] += 1
    for value in list8:
        if value == "e":
            continua.get(8)["e"] += 1
        if value == "i":
            continua.get(8)["i"] += 1
    for value in list10:
        if value == "e":
            continua.get(10)["e"] += 1
        if value == "i":
            continua.get(10)["i"] += 1

def getPercentage(list):
    #Gets the percent of times e and i are chosen and updates the analyses dictionary with that data for the group analysis

    for value in list:
        forPercE = list.get(value)["e"]     #Keeps track of how many times e and i occur in order to divide later on to get a percentage
        forPercI = list.get(value)["i"]
        list.get(value)["e"]= 100 * list.get(value)["e"] / (forPercE + forPercI)
        list.get(value)["i"]= 100 * list.get(value)["i"] / (forPercE + forPercI)
    for value in list:
        x.append(value)
        yE.append(list.get(value)["e"])

def makeGraph(title):
    #Makes a graph with the title passed into the program and the data stored in x, yE, and yI
    plt.plot(x, yE, color="blue")
    plt.title(title)
    plt.xlabel("Interval")
    plt.ylabel("Percent Chose Continuua 1")
    plt.savefig(SAVE + title)
    plt.show()
    x.clear()
    yE.clear()

def itemAnalysisMapMaker(filename):                     #Initializes and then populates the item analysis dictionary
    file = open(os.fspath(PATH + filename), 'r')
    for line in file:                                   #Loops through all the lines in the file and splits them at every comma
        splitCsv = line.split(",")
        try:
            splitLine = splitCsv[2].split("_")             #Tries to split the already split lines at every "_"
            if splitLine[0] == "anger" or splitLine[0] == "disgust" or splitLine[0] == "happy":
                try:        #Puts values in the item analysis map and maps them to an empty map to populate later on
                    splitLine[5].__str__()
                    itemAnalysis[splitLine[0].__str__() + "_" + splitLine[1].__str__() + "_" + splitLine[2] + "_" + splitLine[3] + "_" + splitLine[4]]={}
                except IndexError:
                    itemAnalysis[splitLine[0].__str__() + "_" + splitLine[1].__str__() + "_" + splitLine[2] + "_" + splitLine[3]]={}
        except IndexError:
            splitLine = splitLine
        for value in itemAnalysis:                          #Finiashes initializing the item analysis dictionary which is a map from the stimuli name to a map of each percentage in the continuua to another map of e and i to how many times they occur
            itemAnalysis.get(value)["(00)"] = {"e":0, "i":0}
            itemAnalysis.get(value)["(02)"] = {"e":0, "i":0}
            itemAnalysis.get(value)["(03)"] = {"e":0, "i":0}
            itemAnalysis.get(value)["(04)"] = {"e":0, "i":0}
            itemAnalysis.get(value)["(05)"] = {"e":0, "i":0}
            itemAnalysis.get(value)["(06)"] = {"e":0, "i":0}
            itemAnalysis.get(value)["(07)"] = {"e":0, "i":0}
            itemAnalysis.get(value)["(08)"] = {"e":0, "i":0}
            itemAnalysis.get(value)["(10)"] = {"e":0, "i":0}
    itemAnalysisMapPopulator(filename)

def itemAnalysisMapPopulator(filename):
    file = open(os.fspath(PATH + filename), 'r')
    for line in file:
        importantInformation = []           #Stores all the information that is important for the dictionary
        splitCsv = line.split(",")          #Splits the csv so you can access the different columns
        try:
            try:
                splitCsv[2].split("_")[5].__str__()     #Makes sure the line you are accessing is for a continuua
                importantInformation.append(splitCsv[2].split("_")[0].__str__() + "_" + splitCsv[2].split("_")[1].__str__() + "_" + splitCsv[2].split("_")[2] + "_" + splitCsv[2].split("_")[3] + "_" + splitCsv[2].split("_")[4])      #Appends the name of the file to the important information list for later
            except IndexError:          #Runs if it is not a line with a continuua
                importantInformation.append(splitCsv[2].split("_")[0].__str__() + "_" + splitCsv[2].split("_")[1].__str__() + "_" + splitCsv[2].split("_")[2] + "_" + splitCsv[2].split("_")[3])
            importantInformation.append(splitCsv[2].split("_")[splitCsv[2].split("_").__len__() - 1])
            importantInformation.append(splitCsv[12])       #Does nothing
            try:
                if(importantInformation[0].split("_")[0] == "disgust" and importantInformation[0].split("_")[1] == "surprise" and importantInformation[0].split("_")[2] == "female"):   #Fixes the female disgust surprise issue of flipped continuua (if elif statement below flips the e's and i's to fix it
                    if(importantInformation[2] == "i"):
                        itemAnalysis.get(importantInformation[0]).get(importantInformation[1])["e"] += 1
                    elif (importantInformation[2] == "e"):
                            itemAnalysis.get(importantInformation[0]).get(importantInformation[1])["i"] += 1
                else:
                    itemAnalysis.get(importantInformation[0]).get(importantInformation[1])[importantInformation[2]] += 1        #Uses the information in the important information list to populate the item analysis dictionary
            except AttributeError:
                importantInformation = importantInformation     #Does nothing
        except IndexError:
            importantInformation = importantInformation     #Does nothing

def groupItemAnalysisGraph():
    n_groups = 9                #How many values will be on the x axis
    continuua1 = []                   #Empty list to store how many times continuua 1 is chosen
    continuua2 = []                 #Empty list to store how many times continuua 2 is chosen
    for value in itemAnalysis:
        for number in itemAnalysis.get(value):
            continuua1.append(itemAnalysis.get(value).get(number).get('e'))       #Puts how many times 'e' was chosen into the continuua1 list by using the item analysis dictionary
            continuua2.append(itemAnalysis.get(value).get(number).get('i'))     #Puts how many times 'i' was chosen into the continuua2 list by using the item analysis dictionary

        fig, ax = plt.subplots()                        #https://pythonspot.com/matplotlib-bar-chart/
        index = np.arange(n_groups)                     #Makes a list of how many things on the x axis we will use (0-8)
        bar_width = 0.35

        rects1 = plt.bar(index, continuua1, bar_width, color='b', label='Continuua 1')                   #Initializes bar graph for continuua1 values
        rects2 = plt.bar(index + bar_width, continuua2, bar_width, color='r', label='Continuua 2')   #Initializes bar graph for continuua2 values

        plt.xlabel('Continuum')
        plt.ylabel('Number Out Of 95')
        plt.title(value + " Group Analysis")
        plt.xticks(index + (bar_width/2), ('0%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '100%'))      #Says what x values we will have and how far apart they should be
        plt.legend()

        plt.tight_layout()      #Makes plot fit in the graph space
        plt.savefig(SAVE + value + " Group Analysis")
        plt.show()
        continuua1.clear()
        continuua2.clear()
    reset()

def individualItemAnalysisGraph(filename):
    subject = ""        #Empty string for subject name
    n_groups = 9        #How many values will be on x axis
    continuua1 = []     #Empty list to store how many times continuua 1 was chosen
    continuua2 = []     #Empty list to store how many times continuua 2 was chosen
    file = open(os.fspath(PATH + filename), 'r')        #Opens file to analyze
    for line in file:                                   #Loops through all the lines in the file
        splitLine = line.split(",")                     #Splits the csv file
        try:
            if splitLine[5] == "en-US":                 #Tests that the line that is being looked at has the name of the subject
                subject = splitLine[10]                 #Fills the empty string with the subjects name to name graph
        except IndexError:                              #Does nothing if there is nothing in the 5th spot of the line after being split by commas
            subject = subject       #Does nothing
    for value in itemAnalysis:                          #Loops through item analysis values
        for number in itemAnalysis.get(value):          #Loops through what the values are mapped to in the item analysis
            continuua1.append(itemAnalysis.get(value).get(number).get('e'))     #Gets how many times e occurred by looking at the item analysis dictionary
            continuua2.append(itemAnalysis.get(value).get(number).get('i'))     #Gets how many times e occurred by looking at the item analysis dictionary

        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35

        #Makes the graph using the matplot lib
        rects1 = plt.bar(index, continuua1, bar_width, color='b', label='Continuua 1')
        rects2 = plt.bar(index + bar_width, continuua2, bar_width, color='r', label='Continuua 2')

        plt.xlabel('Continuum')
        plt.ylabel('Number Out Of Five')
        plt.title(value + " Analysis Subject " + subject)
        plt.xticks(index + (bar_width/2), ('0%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '100%'))
        plt.legend()

        plt.tight_layout()
        plt.savefig(SAVE + value + " Analysis Subject " + subject)
        plt.show()
        continuua1.clear()
        continuua2.clear()
    reset()

def singleAnalysis(resultsNumber, graphName):
    #Runs all the code needed for the single analysis

    parser(resultsNumber)       #Runs the parser code above in order to be able to do the analysis code
    analysis(analyses_happy_surpr, zero_happy_surpr, two_happy_surpr, three_happy_surpr, four_happy_surpr, five_happy_surpr, six_happy_surpr, seven_happy_surpr, eight_happy_surpr, ten_happy_surpr)        #Runs the analysis code above for happy surprise
    getPercentageIndividual(analyses_happy_surpr)
    makeGraph(graphName + " Happy Surprise")        #Makes happy surprise graph
    reset()

    parser(resultsNumber)       #Runs the parser code above in order to be able to do the analysis code. Need to run every time because of reset
    analysis(analyses_anger_sad, zero_anger_sad, two_anger_sad, three_anger_sad, four_anger_sad, five_anger_sad, six_anger_sad, seven_anger_sad, eight_anger_sad, ten_anger_sad)        #Runs the analysis code above for anger sad
    getPercentageIndividual(analyses_anger_sad)
    makeGraph(graphName + " Anger Sad")         #Makes anger sad graph
    reset()

    parser(resultsNumber)       #Runs the parser code above in order to be able to do the analysis code. Need to run every time because of reset
    analysis(analyses_anger_fear, zero_anger_fear, two_anger_fear, three_anger_fear, four_anger_fear, five_anger_fear, six_anger_fear, seven_anger_fear, eight_anger_fear, ten_anger_fear)          #Runs the analysis code above for anger fear
    getPercentageIndividual(analyses_anger_fear)
    makeGraph(graphName + " Anger Fear")            #Makes anger fear graph
    reset()

    parser(resultsNumber)       #Runs the parser code above in order to be able to do the analysis code. Need to run every time because of reset
    analysis(analyses_disgust_surprise, zero_disgust_surprise, two_disgust_surprise, three_disgust_surprise, four_disgust_surprise, five_disgust_surprise, six_disgust_surprise, seven_disgust_surprise, eight_disgust_surprise, ten_disgust_surprise)      #Runs the analysis code above for disgust surprise
    getPercentageIndividual(analyses_disgust_surprise)
    makeGraph(graphName + " Disgust Surprise")          #Makes disgust surprise graph
    reset()

def getPercentageIndividual(list):
    # Gets the percent of times e and i are chosen and updates the analyses dictionary with that data for the individual analysis
    for value in list:
        for value in list:
            forPercE = list.get(value)[
                "e"]  # Keeps track of how many times e and i occur in order to divide later on to get a percentage
            forPercI = list.get(value)["i"]
            list.get(value)["e"] = 100 * list.get(value)["e"] / (forPercE + forPercI)
            list.get(value)["i"] = 100 * list.get(value)["i"] / (forPercE + forPercI)
    for value in list:
        x.append(value)
        yE.append(list.get(value)["e"])
