var natural = require('natural');
var classifier = new natural.BayesClassifier();

function getTrainData(){
    return [
        {
            'features': ['sweet', 'cold', 'organic'],
            'class': 'juice'
        },
        {
            'features': ['sweet', 'cold', 'organic'],
            'class': 'juice'
        },
        {
            'features': ['sweet', 'hot', 'organic'],
            'class': 'juice'
        },
        {
            'features': ['sweet', 'cold', 'artificial'],
            'class': 'juice'
        },
        {
            'features': ['bitter', 'hot', 'organic'],
            'class': 'coffee'
        },
        {
            'features': ['bitter', 'hot', 'organic'],
            'class': 'coffee'
        },
        {
            'features': ['bitter', 'cold', 'organic'],
            'class': 'coffee'
        },
        {
            'features': ['bitter', 'hot', 'artificial'],
            'class': 'coffee'
        }
    ]
}

function getUnknownData(){
    return [
        {
            'features': ['sweet', 'cold', 'artificial']
        },
        {
            'features': ['bitter', 'hot', 'organic']
        },
        {
            'features': ['bitter', 'cold', 'artificial']
        }
    ]
}

var list = getTrainData();
list.forEach(function(value, index){
    classifier.addDocument(value.features, value.class);
});
web.train();

var list2 = getUnknownData();

list2.forEach(function(value, index){
    classification = classifier.getClassifications(value.features);
    console.log(classifier.classify(value.features));
    console.log(classification);
    classification.forEach(function(value, index){
        // console.log(value.value * 100)
    });
    console.log();
});

// classifier.addDocument('i am long qqqq', 'buy');
// classifier.addDocument('buy the q\'s', 'buy');
// classifier.addDocument('short gold', 'sell');
// classifier.addDocument('sell gold', 'sell');

// classifier.train();

// console.log(classifier.classify('i am short silver'));
