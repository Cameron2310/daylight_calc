import matplotlib.pyplot as plt
import find_avg as avg


# Creates graph with x-axis for seasons and y-axis for hours
def create_graph():

    SEASONS = ["Spring", "Summer", "Fall", "Winter"]
    averages = [avg.avg_spring, avg.avg_summer, avg.avg_fall, avg.avg_winter]
    POSITIONS = [0,1,2,3]

    plt.bar(POSITIONS, averages, width=0.5)
    plt.title("Average Daylight per Season")
    plt.xticks(POSITIONS, SEASONS)
    plt.xlabel("Seasons")
    plt.ylabel("Averages")


    plt.show()