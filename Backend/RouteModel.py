# -*- coding: utf-8 -*-
import model

class RouteSafer:
    def __init__(self, roadClass, district, loccord, accLoc, injury, intDir, vehType):
        self.roadClass = roadClass
        self.district  = district
        self.loccord   = loccord
        self.accLoc    = accLoc
        self.injury    = injury
        self.intDir    = intDir
        self.vehType   = vehType

        md = model.Model()
        md.startModel()
        d = [self.roadClass, self.district, self.loccord,
             self.accLoc,   self.injury,    self.intDir, self.vehType]
        print(md.Predict([d]))

if __name__ == '__main__':
    rs = RouteSafer(1, 1, 1, 2, 1, 2, 1)
