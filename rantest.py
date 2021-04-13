import pickle, random
t = open("test.info", "wb")
t.truncate(0)
dic = {}
for x in range(0, 10):
  randomnum = random.randint(0, 100)
  print(randomnum)
  dic[randomnum] = bool(input("1/0 big "))
pickle.dump(dic, t)
t.close()
