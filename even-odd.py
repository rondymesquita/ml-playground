from sklearn.naive_bayes import MultinomialNB
import pdb

classes = {
    -1: "odd",
    1: "even"
}


def _print(beverages, probalitities):
    index = 1
    for beverage, prob in zip(beverages, probalitities):
        b = classes[beverage]
        print "\nElement {} is {}".format(index, b)
        print "=== Odds"
        clazz1 = classes[model.classes_[0]]
        clazz2 = classes[model.classes_[1]]
        prob1 = prob[0]
        prob2 = prob[1]
        print "{} of chances of being {}".format(prob1, clazz1)
        print "{} of chances of being {}".format(prob2, clazz2)
        index += 1

    print("=============================================")

# value
# is odd
# is even
def get_train_data():
    odd1 = [1]
    odd2 = [3]
    odd3 = [1]
    odd4 = [3]
    odd5 = [3]
    odd6 = [1]
    odd7 = [3]

    even1 = [0]
    even2 = [0]
    even3 = [2]
    even4 = [0]
    even5 = [2]
    even6 = [0]
    even7 = [2]

    return [odd1, odd2, odd3, odd4, odd5, odd6, odd7,
            even1, even2, even3, even4, even5, even6, even7],\
        [-1, -1, -1, -1, -1, -1, -1,
          1, 1, 1, 1, 1, 1, 1]

train_data, train_target = get_train_data()
# training model
model = MultinomialNB()
model.fit(train_data, train_target)

number1 = [1]
number2 = [2]
number3 = [3]
unknown_beverages = [number1, number2, number3]

beverages = model.predict(unknown_beverages)
probalitities = model.predict_proba(unknown_beverages)
print beverages, probalitities
_print(beverages, probalitities)

# improve learning with insertion of unknown data but specifing what they are
# The probalities should be improved because the model is smarter now
# test_target = [-1, 1, -1]
# model.fit(unknown_beverages, test_target)
# beverages = model.predict(unknown_beverages)
# probalitities = model.predict_proba(unknown_beverages)
# _print(beverages, probalitities)

# errors = beverages - test_target
# number_of_hits = errors.tolist().count(0)
# percent = 100 * number_of_hits / len(test_target)
# print "Hit ratio is {}%".format(abs(percent))
