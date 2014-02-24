'''
Created on Dec 3, 2012

@author: dawood
'''
import time
__all__ = ['loadDemo', 'playDemo']
from IPython.lib.demo import Demo, ClearDemo

def loadDemo(path, title='', autoExec=False):
    demo = ClearDemo(path, title, auto_all=autoExec)
    return demo
    
def playDemo(demo, autoPlay=False, slidePause=10):
    if isinstance(demo, str):
        demo = loadDemo(demo, autoExec=True)
    nslides = demo.nblocks
    def unattended(prompt, nslides=nslides, slidePause=slidePause):
        for i in range(nslides):
            yield 'n'
            time.sleep(slidePause)
    
    idx = 0
    user_input = unattended if autoPlay else raw_input
    while(True):
        demo(idx)
        option = user_input('\n[n] for next. [p] for previous. [q] to quit')
        if 'n' == option:
            if demo < nslides:
                idx += 1
            else:
                break
        elif 'b' == option:
            idx = (idx -1) if idx > 0 else 0
        elif 'q' == option:
            break
    return demo
    