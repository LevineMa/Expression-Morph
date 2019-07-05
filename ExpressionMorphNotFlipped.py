import os
import ExpressionFunctionsNotFlipped as ef

ef.PATH = input("Would you like to use the default path /Users/LevineMa/Desktop/LAB/Results Expression Morph/? y/n")        #Checks if user wants to use default path /Users/LevineMa/Desktop/LAB/Results Expression Morph/
if ef.PATH == "y":      #Uses default path if user wants to use default path
    ef.PATH = "/Users/LevineMa/Desktop/LAB/Results Expression Morph/"
elif ef.PATH == "n":    #If user doesn't want to use default path allows them to input their own path
    ef.PATH = input("What is the path to your files? i.e: /Users/LevineMa/Desktop/LAB/Results Expression Morph/")   #Takes user input for the path to the files that need to be analyzed

ef.SAVE = input("Would you like the files to be saved to the default folder /Users/LevineMa/Desktop/LAB/Graphs Expression Morph/? y/n")         #Checks if user wants to save the graphs to the default folder
if ef.SAVE == "y":      #Uses default path if user wants to save to the default folder
    ef.SAVE = "/Users/LevineMa/Desktop/LAB/Graphs Expression Morph/"
elif ef.SAVE == "n":        #If user doesn't want to save to the default folder allows them to input thei own path to a folder to save in
    ef.SAVE = input("What is the path to the folder you would like to save your graphs? i.e: /Users/LevineMa/Desktop/LAB/Graphs Expression Morph/")     #Takes user input for a path to the folder they want the graphs to be saved to



for file in os.listdir(ef.PATH):    #Loops through files in the path inputted by the user
    if file[0] != "." and file != "Tests":      #Makes sure it only takes the files it is supposed to. (I had a tests folder and a file that was .something and didn't want those taken)
        ef.resultsList.append(file)     #Adds all the file names to a list
        ef.parser(file)                 #Runs the parser function on the files

ef.analysis(ef.analyses_happy_surpr, ef.zero_happy_surpr, ef.two_happy_surpr, ef.three_happy_surpr, ef.four_happy_surpr, ef.five_happy_surpr, ef.six_happy_surpr, ef.seven_happy_surpr, ef.eight_happy_surpr, ef.ten_happy_surpr)       #Runs the analysis function on the happy surprised files

ef.analysis(ef.analyses_anger_sad, ef.zero_anger_sad, ef.two_anger_sad, ef.three_anger_sad, ef.four_anger_sad, ef.five_anger_sad, ef.six_anger_sad, ef.seven_anger_sad, ef.eight_anger_sad, ef.ten_anger_sad)       #Runs the analysis function on the anger sad files

ef.analysis(ef.analyses_anger_fear, ef.zero_anger_fear, ef.two_anger_fear, ef.three_anger_fear, ef.four_anger_fear, ef.five_anger_fear, ef.six_anger_fear, ef.seven_anger_fear, ef.eight_anger_fear, ef.ten_anger_fear)         #Runs the analysis function on the anger fear files

ef.analysis(ef.analyses_disgust_surprise, ef.zero_disgust_surprise, ef.two_disgust_surprise, ef.three_disgust_surprise, ef.four_disgust_surprise, ef.five_disgust_surprise, ef.six_disgust_surprise, ef.seven_disgust_surprise, ef.eight_disgust_surprise, ef.ten_disgust_surprise)         #Runs the analysis function on the disgust surprised files

ef.getPercentage(ef.analyses_happy_surpr)       #Runs the function to get percentages of "e" vs "i" and makes graphs with that data
ef.makeGraph("Group Analysis Happy Surprised")
ef.getPercentage(ef.analyses_anger_sad)
ef.makeGraph("Group Analysis Anger Sad")
ef.getPercentage(ef.analyses_disgust_surprise)
ef.makeGraph("Group Analysis Disgust Surprise")
ef.getPercentage(ef.analyses_anger_fear)
ef.makeGraph("Group Analysis Anger Fear")
ef.reset()      #Resets everything for single analysis

ef.itemAnalysisMapMaker(ef.resultsList[0])      #Runs the map maker function to initialize map
for file in ef.resultsList:           #Loops through all files
    if file != ef.resultsList[0]:     #Skips the map populator function for the first file because map maker populates the map with the first file already
        ef.itemAnalysisMapPopulator(file)   #Populates map with all files after the first



ef.groupItemAnalysisGraph()     #Makes group item analysis graph

for file in ef.resultsList:
    ef.itemAnalysisMapMaker(file)       #Makes map for individual file for individual analysis
    ef.individualItemAnalysisGraph(file)#Make individual analysis graph

for file in ef.resultsList:
    read = open(ef.PATH + file, 'r')
    # Gets the subject's ID to name the graph
    for line in read:
        splitLine = line.split(",")
        try:
            if splitLine[0] == "Chrome":
                subject = splitLine[10]
        except IndexError:
            subject = subject
    ef.singleAnalysis(file, subject + " Analysis")   #Code that is running for the single analysis