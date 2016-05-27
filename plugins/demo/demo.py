'''
Created on Dec 3, 2012

@author: dawood
'''
import time
__all__ = ['loadDemo', 'playDemo']
from IPython.lib.demo import Demo, ClearDemo, ClearMixin

def mp_pre_cmd(self):
    from IPython.utils.terminal import _term_clear as term_clear
    term_clear()

ClearMixin.pre_cmd = mp_pre_cmd

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
    while(True):
        demo(idx)
        option = None
        if autoPlay :
            option = unattended('\n[n] for next. [p] for previous. [q] to quit')
        else :
            option = input('\n[n] for next. [p] for previous. [q] to quit')
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
    