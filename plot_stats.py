import matplotlib.pyplot as plt

with open("stats.txt", "r") as f:
    lines = f.readlines()

xs = []
letters = []
sentences = []
for line in lines:
    if "Author " in line:
        xs.append(int(line.split("Author ")[1]))
        continue
    if "Number of letter per word " in line:
        letters.append(float(line.split("Number of letter per word ")[1]))
        continue
    if "Number of sentences " in line:
        sentences.append(float(line.split("Number of sentences ")[1]))
        continue

# plt.scatter(xs, letters)
# plt.ylabel("Average number of letter per word")
plt.scatter(xs, sentences)
plt.ylabel("Average number of sentences")
plt.grid()
plt.xlabel("Author number")
plt.show()