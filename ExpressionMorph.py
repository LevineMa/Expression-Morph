import os
import ExpressionFunctions as ef

ef.PATH = input("What is the path to your files? i.e: /Users/LevineMa/Desktop/LAB/Results Expression Morph/")


for file in os.listdir(ef.PATH):
    if file[0] != "." and file != "Tests":
        ef.resultsList.append(file)
        ef.parser(file)

ef.analysis(ef.analyses_happy_surpr, ef.zero_happy_surpr, ef.two_happy_surpr, ef.three_happy_surpr, ef.four_happy_surpr, ef.five_happy_surpr, ef.six_happy_surpr, ef.seven_happy_surpr, ef.eight_happy_surpr, ef.ten_happy_surpr)

ef.analysis(ef.analyses_anger_sad, ef.zero_anger_sad, ef.two_anger_sad, ef.three_anger_sad, ef.four_anger_sad, ef.five_anger_sad, ef.six_anger_sad, ef.seven_anger_sad, ef.eight_anger_sad, ef.ten_anger_sad)

ef.analysis(ef.analyses_anger_fear, ef.zero_anger_fear, ef.two_anger_fear, ef.three_anger_fear, ef.four_anger_fear, ef.five_anger_fear, ef.six_anger_fear, ef.seven_anger_fear, ef.eight_anger_fear, ef.ten_anger_fear)

ef.analysis(ef.analyses_disgust_surprise, ef.zero_disgust_surprise, ef.two_disgust_surprise, ef.three_disgust_surprise, ef.four_disgust_surprise, ef.five_disgust_surprise, ef.six_disgust_surprise, ef.seven_disgust_surprise, ef.eight_disgust_surprise, ef.ten_disgust_surprise)

ef.getPercentage(ef.analyses_happy_surpr)
ef.makeGraph("Group Analysis Happy Surprised")
ef.getPercentage(ef.analyses_anger_sad)
ef.makeGraph("Group Analysis Anger Sad")
ef.getPercentage(ef.analyses_disgust_surprise)
ef.makeGraph("Group Analysis Disgust Surprise")
ef.getPercentage(ef.analyses_anger_fear)
ef.makeGraph("Group Analysis Anger Fear")
ef.reset()

ef.itemAnalysisMapMaker(ef.resultsList[0])
for file in ef.resultsList:
    if file != ef.resultsList[0]:
        ef.itemAnalysisMapPopulator(file)



ef.groupItemAnalysisGraph()

for file in ef.resultsList:
    ef.itemAnalysisMapMaker(file)
    ef.individualItemAnalysisGraph(file)

for file in ef.resultsList:
    read = open(ef.PATH + file, 'r')
    # Gets the subject's ID number to name the graph
    for line in read:
        splitLine = line.split(",")
        try:
            if splitLine[0] == "Chrome":
                subject = splitLine[10]
        except IndexError:
            subject = subject
    ef.singleAnalysis(file, subject + " Analysis")   #Code that is running for the single analysis