#!/usr/bin/env python3
import random
import math
class Position:
    def __init__(self):
        # storing results of the initialization, empty before running the program
        self.posR = [[10.4, -3.1], [11.1, 4.0], [10.9, -4.6], [10.9, -1.9], [10.8, 2.0], [11.3, 0.7],
                     [10.2, -0.6], [10.1, 3.2], [11.1, -3.0], [10.1, -2.1], [10.6, -4.0], [10.4, 1.0],
                     [11.2, -0.4], [10.0, 0.1], [11.8, -1.1], [12.1, 2.5], [11.4, 3.1], [12.3, 3.1],
                     [10.5, -5.5], [11.9, 3.7], [11.6, -2.3], [11.7, -4.0], [12.0, 0.1], [10.7, 5.5],
                     [10.5, 4.5], [10.7, 7.1], [10.9, -7.2], [10.0, -5.9], [10.2, 6.7], [10.9, -6.1],
                     [12.4, -0.4], [12.6, -4.3], [10.9, 8.0], [11.8, 6.2], [11.4, 2.4], [11.3, 5.4],
                     [12.5, -6.0], [11.4, -7.9], [12.5, 6.4], [10.2, 8.4], [12.6, 4.5], [12.2, 5.3],
                     [12.1, -7.1], [12.8, -1.7], [10.5, -8.0], [12.0, 8.1], [13.2, -5.7], [12.9, 5.2]]
        self.posL = [[-14.6, 3.1], [-15.3, -4.0], [-15.1, 4.6], [-15.1, 1.9], [-15.0, -2.0], [-15.5, -0.7],
                     [-14.4, 0.6], [-14.3, -3.2], [-15.3, 3.0], [-14.3, 2.1], [-14.8, 4.0], [-14.6, -1.0],
                     [-15.4, 0.4], [-14.2, -0.1], [-16.0, 1.1], [-16.3, -2.5], [-15.6, -3.1], [-16.5, -3.1],
                     [-14.7, 5.5], [-16.1, -3.7], [-15.8, 2.3], [-15.9, 4.0], [-16.2, -0.1], [-14.9, -5.5],
                     [-14.7, -4.5], [-14.9, -7.1], [-15.1, 7.2], [-14.2, 5.9], [-14.4, -6.7], [-15.1, 6.1],
                     [-16.6, 0.4], [-16.8, 4.3], [-15.1, -8.0], [-16.0, -6.2], [-15.6, -2.4], [-15.5, -5.4],
                     [-16.7, 6.0], [-15.6, 7.9], [-16.7, -6.4], [-14.4, -8.4], [-16.8, -4.5], [-16.4, -5.3],
                     [-16.3, 7.1], [-17.0, 1.7], [-14.7, 8.0], [-16.2, -8.1], [-17.4, 5.7], [-17.1, -5.2]]
        self.buffer = [[0.0, -6.3], [0.5, -5.8], [-0.5, -5.8], [-0.1, -5.2], [-0.8, -5.0], [0.4, -4.1],
                       [-0.5, -3.9], [0.5, -3.4], [-0.1, -2.9], [-0.6, -2.4], [0.0, -2.1], [0.6, -1.7],
                       [0.4, -1.0], [-0.7, -1.0], [0.7, -0.2], [-0.1, -0.1], [-0.8, 0.1], [0.7, 0.5],
                       [0.0, 0.7], [-0.7, 1.1], [0.5, 1.5], [0.1, 2.1], [-0.8, 2.5], [0.6, 2.7],
                       [-0.2, 3.1], [0.8, 3.6], [-0.4, 4.1], [0.4, 4.4], [-0.4, 5.0], [0.6, 5.1],
                       [0.0, 6.0], [0.7, 6.0], [-0.6, 6.4]]

    def addOneR(self):
        new_pos = [random.randint(100, 140)/10, random.randint(-87, 87)/10]
        if all(math.sqrt((new_pos[0]-el[0])**2 + (new_pos[1]-el[1])**2) >= 0.6 for el in self.posR):
            self.posR.append(new_pos)
            print(new_pos)
            print(self.intoGeo(self.posR)[-1])
        else:
            self.addOneR()
    
    def addOneBuffer(self):
        new_pos = [random.randint(-8, 8)/10, random.randint(45, 65)/10]
        if all(math.sqrt((new_pos[0]-el[0])**2 + (new_pos[1]-el[1])**2) >= 0.7 for el in self.buffer):
            self.buffer.append(new_pos)
            print(new_pos)
            print(self.intoGeo(self.buffer)[-1])
        else:
            self.addOneBuffer()


    def intoGeo(self, lst):
        borderA = [18.06409196251192, 59.33551828048482]
        borderB = [18.064249995157855, 59.33535531252224]
        borderC = [18.063598779214896, 59.3351910473156]
        xRate = [(borderC[0] - borderB[0])/35, (borderC[1] - borderB[1])/35]
        yRate = [(borderB[0] - borderA[0])/17.4, (borderB[1] - borderA[1])/17.4]
        geoCenter = [(borderA[0] + borderC[0])/2, (borderA[1] + borderC[1])/2]
        for pos in lst:
            xGeo = pos[0] * xRate[0] + pos[1] * yRate[0]
            yGeo = pos[0] * xRate[1] + pos[1] * yRate[1]
            pos[0] = xGeo + geoCenter[0] - 0.082*(18.064249995157855-18.063598779214896)
            pos[1] = yGeo + geoCenter[1] - 0.082*(59.33535531252224-59.3351910473156)
        return lst

    def mirrorLeft(self):
        for pos in self.posR:
            self.posL.append([-4.2 - pos[0], -pos[1]])
        return self.intoGeo(self.posL)


if __name__=="__main__":
    obj = Position()
    # obj.addOneR()
    # obj.addOneBuffer()
    # print(obj.mirrorLeft())
