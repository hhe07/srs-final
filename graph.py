import matplotlib.pyplot as plt
import numpy as np
sys = ["Markov-Extra", "Markov", "Direct Translation","IBM", "Reference Maximum"]
scores = [0.06392372682986576,0.07396317874139555,0.13791491044355006,0.3700964690779332,1.0]
fig, ax = plt.subplots()
ax.set_ylabel("BLEU Score")
ax.set_xlabel("Method")
ax.set_title("BLEU Score vs. Method")

x = np.arange(len(sys))
plots = ax.bar(x,scores,0.5,label = "System")

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height.round(5)),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(plots)
plt.bar(sys, scores)
plt.show()

