import re
from nltk import pos_tag

def count_words(text):
  counts = dict()
  lowered = text.lower()

  replaced = lowered.replace(',','').replace('.','')
  words = lowered.split(' ')
  for w in words:
    if w in counts:
      counts[w] += 1
    else:
      counts[w] = 1
  return counts


my_text = "As I was waiting, a man came out of a side room, and at a glance I was sure he must be Long John. His left leg was cut off close by the hip, and under the left shoulder he carried a crutch, which he managed with wonderful dexterity, hopping about upon it like a bird. He was very tall and strong, with a face as big as a ham—plain and pale, but intelligent and smiling. Indeed, he seemed in the most cheerful spirits, whistling as he moved about among the tables, with a merry word or a slap on the shoulder for the more favoured of his guests"
n_words = count_words(my_text)
print(n_words)


def sent_tokenize(text):
  splt = re.split("\.", text)
  striped = []
  for s in splt:
    if s != '':
      striped.append(s.strip().replace(',',''))
  
  return striped

sentences = sent_tokenize(my_text)

#print(sentences)

def word_tokenize(sentence):
  splt = re.split('\ +',sentence)
  striped=[]
  for w in splt:
    if w != '':
      striped.append(w.strip().replace(",","").replace(".",""))
  return striped

words = word_tokenize("As I was waiting  a man came out of a side room  and at a glance I was sure he must be Long John")


result = pos_tag(words)
print(result)