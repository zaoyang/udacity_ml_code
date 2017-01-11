# ------------------------------------------------------------------

#
#   Bayes Optimal Classifier
#
#   In this quiz we will compute the optimal label for a second missing word in a row
#   based on the possible words that could be in the first blank
#
#   Finish the procedurce, LaterWords(), below
#
#   You may want to import your code from the previous programming exercise!
#

from __future__ import division

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be ---
'''

data_list = sample_memo.strip().split()

words_to_guess = ["ahead", "could"]

def countWordPlusDistance(sample, word, distance):
    afterWordDict = {}
    afterWordProb = {}
    sumAll = 0
    for idx, sampleWord in enumerate(sample):
        if word == sampleWord:
            wordAfter = sample[idx + distance]

            sumAll += 1
            if distance == 1:
                if afterWordDict.get(wordAfter) == None:
                    afterWordDict[wordAfter] = 1
                else:
                    afterWordDict[wordAfter] = afterWordDict.get(wordAfter) + 1
            elif distance == 2:
                wordBeforeAfter = sample[idx + distance-1]

                if afterWordDict.get(wordBeforeAfter + " " + wordAfter) == None:
                    afterWordDict[wordBeforeAfter + " " + wordAfter] = 1
                else:
                    afterWordDict[wordBeforeAfter + " " + wordAfter] = afterWordDict.get(wordBeforeAfter + " " + wordAfter) + 1

    for word in afterWordDict.keys():
        afterWordProb[word] = afterWordDict.get(word) / sumAll

    afterWordDict = sorted(afterWordDict.items(), key=lambda x: x[1], reverse=True)
    afterWordProb = sorted(afterWordProb.items(), key=lambda x: x[1], reverse=True)

    return (afterWordDict, afterWordProb)



def LaterWords(sample, word, distance):
    '''@param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''

    sampleText = sample.strip().split()

    # TODO: Given a word, collect the relative probabilities of possible following words
    # from @sample. You may want to import your code from the maximum likelihood exercise.
    tuple = countWordPlusDistance(sampleText, word, 1)
    afterWordDict = tuple[0]
    afterWordProb = tuple[1]


    # print afterWordDict
    # print afterWordProb
    # print
    #

    # # TODO: Repeat the above process--for each distance beyond 1, evaluate the words that
    # # might come after each word, and combine them weighting by relative probability
    # # into an estimate of what might appear next.

    # add all the probablities for a given
    tuple = countWordPlusDistance(sampleText, word, distance)
    splitWordDict = tuple[0]
    splitWordProb = tuple[1]

    print splitWordDict
    print splitWordProb
    print

    splitList = []
    for word in splitWordDict:
        splitWord = word[0].split()
        splitList.append(splitWord[1])

    finalProbDict ={}
    for word in splitList:

        for splitProb in splitWordProb:
            if(splitProb[0].split()[1] == word):
                if finalProbDict.get(word) == None:
                    finalProbDict[word] = splitProb[1]
                else:
                    finalProbDict[word] += splitProb[1]


    finalProbDictSorted = sorted(finalProbDict.items(), key=lambda x: x[1], reverse=True)

    return max(finalProbDictSorted, key= lambda x: x[1])[0]


if __name__ == '__main__':

    print LaterWords(sample_memo,"ahead",2)
    print LaterWords(sample_memo,"could",2)
    print LaterWords(sample_memo, "and", 2)

    print LaterWords(sample_memo, "stuff", 2)
    print LaterWords(sample_memo, "gonna", 2)
    print LaterWords(sample_memo, "be", 2)
    print LaterWords(sample_memo, "forgot", 2)
