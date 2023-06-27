from matplotlib import pyplot as plt
plt.plot([1,3,5,7],[10,20,30,40])
plt.savefig("./pyplotimg/plot1.jpg")
plt.cla()

n = range(1,30)
plt.plot(n, n, marker='o', linestyle='--', color='y')
plt.savefig("./pyplotimg/plot2.jpg")