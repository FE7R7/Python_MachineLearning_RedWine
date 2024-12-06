# ------------------------- Importing -------------------------- #

from tkinter import *

from Wine_DecisionTree import MyDecisionTreeWine

# ------------------------- Window Settings -------------------------- #


window = Tk()
window.geometry("435x607")
window.title("Welcome To Wine Predictor App")
window.configure(bg='beige')

# -------------- Creating an Instance of MyDecisionTreeWine Class -------------- #


decisionTree = MyDecisionTreeWine()


# ------------- trainData(), testData(), makeNewPrediction() Functions ------------ #

def trainData():
    newSeedValue = int(seedsVar.get())

    decisionTree.updateSeed(newSeedValue)
    decisionTree.trainData()


def testData():
    text.delete("1.0", "end")  # Clear the Text Area

    text.insert(END, ' ' + decisionTree.readCategories())

    text.insert(END, '\n----------------------------')

    result, accuracy = decisionTree.testData()

    text.insert(END, '\n' + str(result[0]))
    text.insert(END, '\n' + str(result[1]))
    text.insert(END, '\n' + str(result[2]))

    print()
    text.insert(END, '\n\nAccuracy ' + str(int(accuracy * 100)) + '%')


def makeNewPrediction():
    fixed_acidity = float(entry41.get())
    volatile_acidity = float(entry42.get())
    citric_acid = float(entry43.get())
    residual_sugar = float(entry44.get())
    chlorides = float(entry45.get())
    free_sulfur_dioxide = float(entry46.get())
    total_sulfur_dioxide = float(entry47.get())
    density = float(entry48.get())
    pH = float(entry49.get())
    sulphates = float(entry50.get())
    alcohol = float(entry51.get())

    prediction_Res = decisionTree.makePrediction(fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                                                 chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH,
                                                 sulphates, alcohol)

    print(fixed_acidity, "|", volatile_acidity, citric_acid, "|", residual_sugar, "|",
          chlorides, "|", free_sulfur_dioxide, "|", total_sulfur_dioxide, "|", density, "|", pH, "|", sulphates, "|",
          alcohol, ' => Score => ', prediction_Res)

    prediction = prediction_Res

    entry52.delete(0, END)
    entry52.insert(END, prediction)


# ------------------------- TKinter UI Settings -------------------------- #

# ------------- Frame ------------- #

frame = Frame(window, width=450, height=450)
frame.place(x=10, y=100)

label0 = Label(window, text=" Wine Quality Predictor", fg="blue", bg="white", font=("arial", 16, "bold"))
label0.place(x=125, y=17)  # place on screen

# ------------- Seed ------------- #

label01 = Label(window, text="First Enter Seed Value:", fg="green", bg="white", font=("arial", 12, "bold"))
label01.place(x=19, y=70)

label1 = Label(frame, text="      Enter Seed Value     ", fg="blue", width=15, font=("arial", 10, "bold"))
label1.grid(row=0, column=0, sticky=W + E)

list1 = ['1', '2', '3', '4', '41']
seedsVar = StringVar()
combo1 = OptionMenu(frame, seedsVar, *list1)

seedsVar.set("1")
combo1.grid(row=0, column=1, sticky=W + E)

# ------------- Train Data ------------- #

button1 = Button(frame, text="     Train Data    ", fg="black", font=("arial", 10, "bold"), command=trainData)
button1.grid(row=1, column=0, sticky=W + E)

# ------------- Test Data ------------- #

button2 = Button(frame, text="     Test Data      ", fg="black", font=("arial", 10, "bold"), command=testData)
button2.grid(row=1, column=1, sticky=W + E)

# ------------- Output ------------- #

label3 = Label(frame, text="Output", fg="blue", width=15, font=("arial", 10, "bold"))
label3.grid(row=2, column=0)

text = Text(frame, height=6, width=7)
text.grid(row=2, column=1, ipadx=100)

label02 = Label(frame, text="      ", fg="green", font=("arial", 16, "bold"))
label02.grid(row=3, column=0, columnspan=2, sticky=W + E)

# ------------- Test New Data ------------- #

label03 = Label(frame, text="Now Test for New Data:", fg="green", bg="white", font=("arial", 12, "bold"))
label03.grid(row=4, column=0, columnspan=2, sticky=W + E)
label03.place(x=8, y=130)  # place on screen

# ------------- New Data Provided By User for Each Wine Feature ------------- #

# 1 - fixed_acidity Feature
label41 = Label(frame, text="Fixed Acidity (e.g. = 7.4) ", fg="blue", width=25, font=("arial", 10, "bold"))
label41.grid(row=5, column=0, sticky=W + E)

entry41 = Entry(frame)
entry41.insert(END, '')
entry41.grid(row=5, column=1, sticky=W + E)

# 2 - volatile_acidity Feature
label42 = Label(frame, text="Volatile Acidity (e.g. = 0.7)", fg="blue", width=25, font=("arial", 10, "bold"))
label42.grid(row=6, column=0, sticky=W + E)

entry42 = Entry(frame)
entry42.insert(END, '')
entry42.grid(row=6, column=1, sticky=W + E)

# 3 - citric_acid Feature
label43 = Label(frame, text="Citric Acid (e.g. = 0.04)", fg="blue", width=25, font=("arial", 10, "bold"))
label43.grid(row=7, column=0, sticky=W + E)

entry43 = Entry(frame)
entry43.insert(END, '')
entry43.grid(row=7, column=1, sticky=W + E)

# 4 - residual_sugar Feature
label44 = Label(frame, text="Residual Sugar (e.g. = 4.7)", fg="blue", width=25, font=("arial", 10, "bold"))
label44.grid(row=8, column=0, sticky=W + E)

entry44 = Entry(frame)
entry44.insert(END, '')
entry44.grid(row=8, column=1, sticky=W + E)

# 5 - chlorides Feature
label45 = Label(frame, text="Chlorides (e.g. = 0.074)", fg="blue", width=25, font=("arial", 10, "bold"))
label45.grid(row=9, column=0, sticky=W + E)

entry45 = Entry(frame)
entry45.insert(END, '')
entry45.grid(row=9, column=1, sticky=W + E)

# 6 - free_sulfur_dioxide Feature
label46 = Label(frame, text="Free Sulfur Dioxide (e.g. = 12)", fg="blue", width=25, font=("arial", 10, "bold"))
label46.grid(row=10, column=0, sticky=W + E)

entry46 = Entry(frame)
entry46.insert(END, '')
entry46.grid(row=10, column=1, sticky=W + E)

# 7 - total_sulfur_dioxide Feature
label47 = Label(frame, text="Total Sulfur Dioxide (e.g. = 70)", fg="blue", width=25, font=("arial", 10, "bold"))
label47.grid(row=11, column=0, sticky=W + E)

entry47 = Entry(frame)
entry47.insert(END, '')
entry47.grid(row=11, column=1, sticky=W + E)

# 8 - density Feature
label48 = Label(frame, text="Density (e.g. = 0.9978)", fg="blue", width=25, font=("arial", 10, "bold"))
label48.grid(row=12, column=0, sticky=W + E)

entry48 = Entry(frame)
entry48.insert(END, '')
entry48.grid(row=12, column=1, sticky=W + E)

# 9 - pH Feature
label49 = Label(frame, text="pH (e.g. = 3.16)", fg="blue", width=25, font=("arial", 10, "bold"))
label49.grid(row=13, column=0, sticky=W + E)

entry49 = Entry(frame)
entry49.insert(END, '')
entry49.grid(row=13, column=1, sticky=W + E)

# 10 - sulphates Feature
label50 = Label(frame, text="Sulphates (e.g. = 0.47)", fg="blue", width=25, font=("arial", 10, "bold"))
label50.grid(row=14, column=0, sticky=W + E)

entry50 = Entry(frame)
entry50.insert(END, '')
entry50.grid(row=14, column=1, sticky=W + E)

# 11 - alcohol Feature
label51 = Label(frame, text="Alcohol (e.g. = 9.4)", fg="blue", width=25, font=("arial", 10, "bold"))
label51.grid(row=15, column=0, sticky=W + E)

entry51 = Entry(frame)
entry51.insert(END, '')
entry51.grid(row=15, column=1, sticky=W + E)

# ------------- Make New Prediction ------------- #

button3 = Button(frame, text="Make Prediction", fg="black", font=("arial", 10, "bold"), command=makeNewPrediction)
button3.grid(row=16, column=0, sticky=W + E)

entry52 = Entry(frame)
entry52.insert(END, '')
entry52.grid(row=16, column=1, sticky=W + E)

mainloop()
