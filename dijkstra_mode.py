from snake import *

class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = -1
        self.value = -1
        self.visted = 0
        self.id = 0

    def updateValue(self):
        pass


class Pathplanner(object):
    def __init__(self, startCoord, goalCoord, obstacleArray):
        self.root = Tk()
        self.cv = Canvas(self.root, bg='white', height=500, width=600)

        self.start_x = startCoord[0]
        self.start_y = startCoord[1]
        start = self.cv.create_rectangle(self.start_x, self.start_y, self.start_x + 20, self.start_y + 20, fill='green')

        self.goal_x = goalCoord[0]
        self.goal_y = goalCoord[1]
        goal = self.cv.create_rectangle(self.goal_x, self.goal_y, self.goal_x + 20, self.goal_y + 20, fill='yellow')

        self.obstacle_array = obstacleArray
        for i in range(len(obstacleArray)):
            self.cv.create_rectangle(obstacleArray[i][0], obstacleArray[i][1], obstacleArray[i][0] + 20,
                                     obstacleArray[i][1] + 20, fill='black')

        self.nodeList = []
        self.coords = []
        self.cv.pack()

        self.optimalPath = []
        self.optimalPath.append([self.goal_x, self.goal_y])

    def update(self, startCoord, goalCoord, obstacleArray):
        self.start_x = startCoord[0]
        self.start_y = startCoord[1]
        self.goal_x = goalCoord[0]
        self.goal_y = goalCoord[1]
        self.obstacle_array = obstacleArray
        self.nodeList = []
        self.coords = []
        self.optimalPath = []
        self.optimalPath.append([self.goal_x, self.goal_y])

    def findPath(self):
        node = Node(self.start_x, self.start_y)
        temp = [self.start_x, self.start_y]
        j = 0
        node.visted = 1
        node.value = 0
        node.id = len(self.nodeList)
        self.nodeList.append(node)
        self.coords.append(temp)

        currentID = node.id

        findGoal = 0

        flag = 0
        while findGoal == 0:
            temp_x = self.nodeList[j].x
            temp_y = self.nodeList[j].y
            temp = [temp_x, temp_y]
            currentID = j

            flag = 0
            node = Node(temp_x + 20, temp_y)
            temp = [node.x, node.y]
            node.parent = currentID
            node.id = currentID + 1
            if node.x == self.goal_x and node.y == self.goal_y:
                findGoal = 1
                node.value = self.nodeList[node.parent].value + 1
                self.coords.append(temp)
                self.nodeList.append(node)
                break
            elif node.x > 0 and node.y > 0:
                if temp not in self.coords:
                    for i in range(len(self.obstacle_array)):
                        if node.x == self.obstacle_array[i][0] and node.y == self.obstacle_array[i][1]:
                            flag = 1
                    # if the node is not an obstacle, then calculate value
                    if flag == 0:
                        node.value = self.nodeList[node.parent].value + 1
                        self.coords.append(temp)
                        self.nodeList.append(node)
                else:
                    if node.value > self.nodeList[node.parent].value + 1:
                        node.value = self.nodeList[node.parent].value + 1
            node.visited = 1

            # (temp_x-20, temp_y)
            node = Node(temp_x - 20, temp_y)
            temp = [node.x, node.y]
            node.parent = currentID
            node.id = currentID + 2
            flag = 0
            if node.x == self.goal_x and node.y == self.goal_y:
                findGoal = 1
                node.value = self.nodeList[node.parent].value + 1
                self.coords.append(temp)
                self.nodeList.append(node)
                break
            elif node.x > 0 and node.y > 0:
                if temp not in self.coords:
                    for i in range(len(self.obstacle_array)):
                        if node.x == self.obstacle_array[i][0] and node.y == self.obstacle_array[i][1]:
                            flag = 1
                    # if the node is not an obstacle, then calculate value
                    if flag == 0:
                        node.value = self.nodeList[node.parent].value + 1
                        self.nodeList.append(node)
                        self.coords.append(temp)
                else:
                    if node.value > self.nodeList[node.parent].value + 1:
                        node.value = self.nodeList[node.parent].value + 1
            node.visited = 1

            # (temp_x, temp_y + 20)
            node = Node(temp_x, temp_y + 20)
            temp = [node.x, node.y]
            node.parent = currentID
            node.id = currentID + 3
            flag = 0
            if node.x == self.goal_x and node.y == self.goal_y:
                findGoal = 1
                node.value = self.nodeList[node.parent].value + 1
                self.coords.append(temp)
                self.nodeList.append(node)
                break
            elif node.x > 0 and node.y > 0:
                if temp not in self.coords:
                    for i in range(len(self.obstacle_array)):
                        if node.x == self.obstacle_array[i][0] and node.y == self.obstacle_array[i][1]:
                            flag = 1
                    # if the node is not an obstacle, then calculate value
                    if flag == 0:
                        node.value = self.nodeList[node.parent].value + 1
                        self.nodeList.append(node)
                        self.coords.append(temp)
                else:
                    if node.value > self.nodeList[node.parent].value + 1:
                        node.value = self.nodeList[node.parent].value + 1
            node.visited = 1

            # (temp_x, temp_y - 20)
            node = Node(temp_x, temp_y - 20)
            temp = [node.x, node.y]
            node.parent = currentID
            node.id = currentID + 4
            flag = 0
            if node.x == self.goal_x and node.y == self.goal_y:
                findGoal = 1
                node.value = self.nodeList[node.parent].value + 1
                self.coords.append(temp)
                self.nodeList.append(node)
                break
            elif node.x > 0 and node.y > 0:
                if temp not in self.coords:
                    for i in range(len(self.obstacle_array)):
                        if node.x == self.obstacle_array[i][0] and node.y == self.obstacle_array[i][1]:
                            flag = 1
                    # if the node is not an obstacle, then calculate value
                    if flag == 0:
                        node.value = self.nodeList[node.parent].value + 1
                        self.nodeList.append(node)
                        self.coords.append(temp)
                else:
                    if node.value > self.nodeList[node.parent].value + 1:
                        node.value = self.nodeList[node.parent].value + 1
            node.visited = 1

            j = j + 1
        # self.cv.pack()


        length = len(self.nodeList)
        index = length - 1
        while not self.nodeList[index].parent == 0:
            index = self.nodeList[index].parent
            self.optimalPath.append([self.nodeList[index].x, self.nodeList[index].y])
            self.cv.create_rectangle(self.nodeList[index].x, self.nodeList[index].y, self.nodeList[index].x + 20,
                                     self.nodeList[index].y + 20, fill='red')

        self.cv.pack()
        return self.optimalPath

    def drawPath(self):
        for k in range(len(self.optimalPath)):
            print "path ", k, "  :",self.optimalPath[k]
            time.sleep(0.2)
            self.cv.create_rectangle(self.optimalPath[k][0], self.optimalPath[k][1], self.optimalPath[k][0] + 20, self.optimalPath[k][1] + 20, fill = 'green')

class AutoSnakeGame(SnakeGame):
    def __init__(self, background, game_height=15, game_width=15, period=0.3):
        super(AutoSnakeGame, self).__init__(background, game_height, game_width, period)

    def init_game(self):
        self.signal = threading.Event()

        t1 = threading.Thread(target=self.move)
        t1.start()

        t2 = threading.Thread(target=self.goToFood)
        t2.start()

    def move(self):
        while True:
            #print self.signal.isSet()
            self.snake.move()
            if self.snake.snake_coord[0] == self.food.coord:
                self.snake.eat()
                self.food.generate(self.snake.snake_coord)
            self.signal.set()
            time.sleep(0.5)

    def goToFood(self):
        while True:
            time.sleep(0.05)
            if self.signal.isSet():
                time1 = time.time()
                # get status after the snake has moved
                food_coord, snake_coord, snake_direction = self.getCurrentStatus()
                startCoord = snake_coord[0]
                #print startCoord
                obstacleArray = []
                for i in range(1, len(snake_coord)):
                    obstacleArray.append(snake_coord[i])
                pathplanner = Pathplanner(startCoord, food_coord, obstacleArray)
                optimalPath = pathplanner.findPath()
                print time.time() - time1
                #print optimalPath
                i = len(optimalPath) - 1
                # self.background.cv.create_rectangle(optimalPath[i][0],
                #                                     optimalPath[i][1],
                #                                     optimalPath[i][0]+20, 
                #                                     optimalPath[i][1]+20, 
                #                                     fill = 'red')
                class FakeEvent(object):
                    char = ''
                if optimalPath[i][0] > snake_coord[0][0]:
                    # need to change to 0
                    FakeEvent.char = 'd'
                elif optimalPath[i][0] < snake_coord[0][0]:
                    FakeEvent.char = 'a'
                elif optimalPath[i][1] > snake_coord[0][1]:
                    FakeEvent.char = 's'
                elif optimalPath[i][1] < snake_coord[0][1]:
                    FakeEvent.char = 'w'
                #print FakeEvent.char
                self.changedirection(FakeEvent)
                self.signal.clear()


if __name__ == '__main__':
    print "Start Game"
    background = Background()
    background.draw()

    # find path and control snake
    game = AutoSnakeGame(background)
    game.init_game()
    game.background.root.mainloop()
