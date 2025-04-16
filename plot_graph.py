import matplotlib.pyplot as plt

x_lis = []
y_lis = []

def draw_line(x, y):
    plt.plot(x, y, color="green", label="Your Line")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Your Graph")
    plt.grid(True)
    plt.legend()
    plt.show()


p = input("enter points of a line point example (0,0) (1,1): ")


def get_line_pos(points):
    print()

    # get the numbers
    try:
        point1 = points.split(" ")[0]
        point2 = points.split(" ")[1]
        x1 = int(point1.split(",")[0][1:])
        y1 = int(point1.split(",")[1][:-1])
        x2 = int(point2.split(",")[0][1:])
        y2 = int(point2.split(",")[1][:-1])
    except ValueError:
        return ("\ninvalid input")

    # get the slope
    slope = (y2 - y1) / (x2 - x1)  # formula = y2 - y1 / x2 - x1

    # 12 = 6*1 + b
    # find the y-intercept aka b
    y_intercept = y1 - slope * x1

    # get the equation to plug the numbers in
    eq = f"y = {slope}x + {y_intercept}"

    # plug in the numbers
    right_side = eq.split("=")[1].strip()
    for z in range(11):
        temp = ""
        for y in right_side:
            if y == "x":
                temp += f"*{z}"
            else:
                temp += y

        x_lis.append(z)
        y_lis.append(eval(x))

get_line_pos(p)
draw_line(x_lis, y_lis)
