'''
Created on 04/11/2013

@author: Juan Ceballos
'''
from GameScriptLogger import ScriptLog
from Analyze import GroupMapper
import logging
import sys

"""
    example:
    (short) python AnalyzeGameSimulation\Flow.py E:\People\Ceballos\source\python\Test\src\GameSimulation\.sessions\session68153.scriptlog | python analyze\TimelineReducer.py
    (middle) python AnalyzeGameSimulation\Flow.py E:\People\Ceballos\source\python\Test\src\GameSimulation\.sessions\session5113717.scriptlog | python analyze\TimelineReducer.py
    (middle) python AnalyzeGameSimulation\Flow.py E:\People\Ceballos\source\python\Test\src\GameSimulation\.sessions\session5113717.scriptlog | python analyze\TimelineReducer.py
"""
def main(isDebug=False):
    if len(sys.argv)==1:
        logging.error("usage: python Flow.py <filename>")
        return -1
    
    logging.basicConfig(level=logging.ERROR)
    logging.debug("**** GAMESCRIPTLOGGER started***")
    
    logging.info("Loading filename: %s" %  sys.argv[1])
    scriptLog = ScriptLog.ScriptLog()
    scriptLog.load(sys.argv[1])
    if isDebug:
        print scriptLog
    logging.debug("--- EOF scriptLog---")
    
    # x statemanager, y state     15=numstates
    mapColor = lambda x, y: (0xFF<<(16*int(x)))+int((float(y)/15.0)*255) if (type(x)==int or x.isdigit()) and (type(y)==int or x.isdigit()) else x+"-"+y   # map statemachine and state to unique value
    print mapColor(0, 0), mapColor(0, 15), mapColor(1, 0), mapColor(1, 15), mapColor(2, 0), mapColor(2, 15),
    groupMapper = GroupMapper.GroupMapper(sys.argv[1], filterInputRecords=None, terminalState=None, isDebug=isDebug, mapColor=mapColor)
    for record in scriptLog:
        if isDebug:
            print record
        groupMapper.map(record)
    groupMapper.end()
    
    logging.debug("**** GAMESCRIPTLOGGER finished***")
    
if __name__ == "__main__":
    main(isDebug=False)
    
    