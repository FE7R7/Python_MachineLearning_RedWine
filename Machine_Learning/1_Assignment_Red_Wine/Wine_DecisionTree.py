# ------------------------- Imports -------------------------- #
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


# ------------------------- MyDecisionTreeWine Class -------------------------- #


class MyDecisionTreeWine:

    # ------------------------- __init__ Constructor Function -------------------------- #

    def __init__(self):
        self.df = pd.read_csv('red_wine_quality.csv', delimiter=';')

        self.df.head()

        self.X = self.df.drop('quality', axis='columns')
        self.y = self.df.quality

        self.seedValue = 1

        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

        self.tree = DecisionTreeClassifier()

        self.y_hat = None

        self.cm = None

    # ------------------------- Seed Function -------------------------- #

    def updateSeed(self, newValue):
        self.seedValue = newValue

    # ------------------------- Train Data Function -------------------------- #

    def trainData(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=320,
                                                                                random_state=self.seedValue,
                                                                                stratify=self.y)

        self.tree = DecisionTreeClassifier()
        self.tree.fit(self.X_train, self.y_train)

    # ------------------------- Make Prediction Function -------------------------- #

    def makePrediction(self, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                       free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol):

        # Create the input data as a list of lists
        input_data = [[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide,
                       total_sulfur_dioxide, density, pH, sulphates, alcohol]]

        # Create a DataFrame with the correct column names
        df2 = pd.DataFrame(input_data, columns=[
            'fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides',
            'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol'])

        # Make the prediction using the model
        cm_result = self.tree.predict(df2)

        return cm_result[0]

    # ------------------------- Test Data Function -------------------------- #

    def testData(self):

        self.y_hat = self.tree.predict(self.X_test)

        print()
        print(self.X_test)

        print()
        print("Accuracy:", accuracy_score(self.y_test, self.y_hat))
        # print("Accuracy:", tree.score(X_test, y_test))

        # confusion matrix
        cm = confusion_matrix(self.y_test, self.y_hat)

        # ------------------------ Matrix Output Formating ----------------------- #

        # Custom print function to format the confusion matrix nicely
        formatted_rows = []  # List to store formatted rows as strings

        for row in cm:
            # Join the elements of the row into a string with specified spacing
            formatted_row = " | ".join(f"{val:2}" for val in row)  # Adjust the number (2) for width
            formatted_rows.append(formatted_row)  # Add formatted row to the list

        # Join all formatted rows with newline characters to create the final string
        return formatted_rows, accuracy_score(self.y_test, self.y_hat)

    # ------------------------- Read Categories Function -------------------------- #

    def readCategories(self):

        result = ''
        index = 0

        setOfCategories = set(self.y)

        print('\nThe Categories of Quality Score Found in the Dataset (0 < Score <= 10): ', setOfCategories)

        for catName in sorted(setOfCategories):

            if (index > 0):
                result += " |  "

            # Casting to String to be able to concatenate
            result += str(catName)

            index += 1

        return result
