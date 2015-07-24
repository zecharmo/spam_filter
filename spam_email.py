
# Spam Filtering with Naive Bayes 

# Bayes Theorem: P(Y|X) = (P(x|Y)*P(Y))/P(X)


# access the data
enron = 'http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron1.tar.gz'

# the data contains 1,500 spam messages and 3,672 ham messages

# compute the probability that an e-mail is or is not spam
p_spam = 1500/(1500+3672)
p_ham = 1 - p_spam

# get counts containing the word 'meeting' in spam and ham e-mail sets
meeting_spam = grep -il meeting enron/spam/*.txt | wc -l
meeting_ham = grep -il meeting enron/ham/*.txt | wc -l

# compute the probability that an e-mail contains the word 'meeting' given it is or isn't spam
p_word_g_spam = meeting_spam/1500
p_word_g_ham = meeting_ham/3672

# compute the probability an e-mail is spam given it contains the word 'meeting'
p_spam_g_word = (p_word_g_spam * p_spam) / ((p_word_g_spam * p_spam) + (p_word_g_ham * p_ham))


# now lets compute a probability that combines words
# we expand our definition of Bayes Rule to Naive Bayes, which predicts a class value given a set of set of attributes

# Naive Bayes: P(C|A1, A2,...An) = (SUM(P(A's|C))*P(C))/SUM(P(A's))

# when we’re dealing with a product of probabilities, it is standard to take the log of both sides to get a summation instead

# summation of the probabilities of all of the words
# to get p_word1 and p_word2 (etc), you would get a count of how often that word appears in a spam e-mail
word_sum = (log((p_word1) / (1-p(word1))))+ (log((p_word2) / (1-p(word2))))
not_word_sum = (1-p(word1)) + (1-p(word2))

p_spam_g_allwords = ((word_sum + not_word_sum) * p_spam) / word_sum