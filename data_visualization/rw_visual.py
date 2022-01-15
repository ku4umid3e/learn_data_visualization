import matplotlib.pyplot as plt

from random_wolk import RandomWalk

while True:
    # Plotting random points and plotting them on a diagram.
    rm = RandomWalk()
    rm.fill_walk()
    
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rm.num_points))
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
   # plt.plot(rm.x_values, rm.y_values, linewidth=1)
    plt.scatter(rm.x_values, rm.y_values, c=point_numbers, cmap=plt.cm.Blues,
            edgecolor='none', s=3)
    plt.scatter(0, 0, c='green', edgecolors='none', s=15)
    plt.scatter(rm.x_values[-1], rm.y_values[-1], c='red', 
            edgecolors='none', s=15)


    plt.show()


    keep_running = input("Make another walk? (y/n)")
    if keep_running == 'n':
        break

