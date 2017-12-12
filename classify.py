from sklearn.naive_bayes import MultinomialNB
import pdb

classes = {
    1: "juice",
    -1: "coffee"
}

# is sweet?
# is cold?
# is organic?

juice1 = [1, 1, 1]
juice2 = [1, 1, 1]
juice3 = [1, 0, 1]
juice4 = [1, 1, 0]

coffee1 = [0, 0, 1]
coffee2 = [0, 0, 1]
coffee3 = [0, 1, 1]
coffee4 = [0, 0, 0]

train_data = [juice1, juice2, juice3, juice4, coffee1, coffee2, coffee3, coffee4]
train_target = [1, 1, 1, 1, -1, -1, -1, -1]

model = MultinomialNB()
model.fit(train_data, train_target)

beverage1 = [1, 1, 0]  # maybe juice
beverage2 = [0, 0, 1]  # maybe coffee
beverage3 = [0, 1, 0]  # I can't tell...
unknown_beverages = [beverage1, beverage2, beverage3]
beverages = model.predict(unknown_beverages)
probalitities = model.predict_proba(unknown_beverages)

index = 1
for beverage, prob in zip(beverages, probalitities):
    b = classes[beverage]
    print "\nBeverage {} is {}".format(index, b)
    print "=== Odds"
    clazz1 = classes[model.classes_[0]]
    clazz2 = classes[model.classes_[1]]
    prob1 = prob[0]
    prob2 = prob[1]
    print "{} of chances of being {}".format(prob1, clazz1)
    print "{} of chances of being {}".format(prob2, clazz2)
    index+=1

print ""
print probalitities
print model.classes_