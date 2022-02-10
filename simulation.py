from graphics import *
import random as rng
import math

win = GraphWin("Simulation - Universe", 800, 800, False)
winSize = [-400, -400, 400, 400]
win.setCoords(winSize[0], winSize[1], winSize[2], winSize[3])
win.setBackground("#050506")


def clear(window):
    for item in window.items[:]:
        item.undraw()
    window.update()


# Star
def createStar(xCoord, yCoord, starSize):
    c = Circle(Point(xCoord, yCoord), starSize)
    c.draw(win)
    c.setFill("#0481ff")
    c.setOutline("#0481ff")


# Star Cluster
def createStarCluster(xCoord, yCoord, radius, numberOfStars):
    for _ in range(numberOfStars):
        r = radius * math.sqrt(rng.random())
        theta = rng.random() * 2 * math.pi

        x = xCoord + r * math.cos(theta)
        y = yCoord + r * math.sin(theta)

        createStar(x, y, rng.uniform(0.75, 1))


def setStarClusterCenter(numberOfStarClusters, minRadius, maxRadius, minNumberOfStars, maxNumberOfStars):
    for _ in range(numberOfStarClusters):
        createStarCluster(
            rng.randint(winSize[0], winSize[2]),
            rng.randint(winSize[1], winSize[3]),
            rng.randint(minRadius, maxRadius),
            rng.randint(minNumberOfStars, maxNumberOfStars)
        )


# Universe
def createUniverse(numberOfStars):
    for _ in range(numberOfStars):
        createStar(
            rng.randint(winSize[0], winSize[2]),
            rng.randint(winSize[1], winSize[3]),
            rng.uniform(0.5, 1.75)
        )


def load():
    setStarClusterCenter(32, 25, 75, 50, 75)
    createUniverse(1500)


def reload():
    clear(win)
    load()


load()

while True:
    if win.checkKey() == "r":
        reload()

win.mainloop()
