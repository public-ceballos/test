'''
Created on 04/11/2013

@author: Juan Ceballos
'''

import Image
import numpy as np
#from numpy.random import randn
#import numpy
import re
import itertools
import logging

class TimelineAnalyzeViewer():
    _ResolutionX = 1500
    _ResolutionY = 16000
    _Intensity = 1
    _HeightBlock = 20
    
    def generate(self, fileInputName, fileName = 'untitled.png'):
        if 0:
            img = self.__readTimelineReducer(fileInputName)
        else:
            img = Image.new('RGB', (TimelineAnalyzeViewer._ResolutionX, TimelineAnalyzeViewer._ResolutionY))
            data = self.__readTimelineReducer(fileInputName)
            img.putdata(data)
        print "saving image:", fileName
        img.save(fileName)
        img.show()
        

    def __readTimelineReducer(self, fileInputName):
        greyValue = lambda x: tuple([int(x)*TimelineAnalyzeViewer._Intensity]*3)
        colorValue = lambda x: (int(x)&0xFF0000, int(x)&0x00FF00, int(x)&0x0000FF)
        
        #w,h = 1024,768
        #data = np.zeros( (w,h,3), dtype=np.uint8)
        #data = np.clip(randn(250, 250), -1, 1)      
        characters = list()
        line = ""
        data = []
        empty = (0, 0, 0)
        separatorLine = [[(255, 255, 255)]*TimelineAnalyzeViewer._ResolutionX][0]
        with open(fileInputName) as srcDataFile:
            for line in srcDataFile:
                if (line[0]=='['):
                    colorRepeat = re.findall(r'[\d]+', line.rstrip())
                    color, repeat = colorRepeat[::2], colorRepeat[1::2]
                    #data.extend([[int(k[0])]*int(k[1]) for k in zip(color, repeat)])
                    
                    # save as tuple (R, G, B) and repeat n times 
                    imgLine = []
                    for k in zip(color, repeat):
                        imgLine.extend(*[[colorValue(k[0])]*int(k[1])] )
                    
                    # fill remaining list
                    remain = TimelineAnalyzeViewer._ResolutionX - len(imgLine) if (TimelineAnalyzeViewer._ResolutionX - len(imgLine))>0 else 0
                    # [0] -> get the contain of imgLine, as we are doing the repetition of the tuple we get the second inner set
                    emptyLine = [empty]*remain
                    
                    imgLine = imgLine + emptyLine
                    imgLine = imgLine * TimelineAnalyzeViewer._HeightBlock  # size of action clip
                    data.extend(imgLine)
                else:
                    characters.append(line.rstrip())
                    data.extend(separatorLine)
        data.extend(separatorLine)
        
        print "len characters:", len(characters)
        #print data
        #data = sum(data, [])
        #data = list(t for t in itertools.chain(*data))
        print "... data flatten"
        #print data
        #return Image.fromarray(np.uint8(data))
        return data
    

logging.debug("**** TIMELINEANALYZERVIEWER started***")
timelineAnalyzeViewer = TimelineAnalyzeViewer()
#timelineAnalyzeViewer.generate('.\src\Analyze\output1.data')
timelineAnalyzeViewer.generate('.\src\Analyze\output3.data')
logging.debug("**** TIMELINEANALYZERVIEWER finished***")
print "Done."







