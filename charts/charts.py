import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'c',]
    values = [120, 354, 80]

    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig('pie 1.png')
    plt.close()