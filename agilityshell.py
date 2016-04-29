'''
Created on Oct 26, 2012

@author: dawood
'''

from agilityinit import *

from core.smfy import embed_short
from optparse import OptionParser

ipshell = embed_short.ipshell
from core.universal import agility, a

def main():
    # parse commandline options
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="Execute file")
    parser.add_option("-c", "--command", dest="command", help="Execute command")
    parser.add_option("-p", "--config", dest="config", help="Use configuration file specified by path")
    parser.add_option("-a", "--fargs", dest="fileargs",
                      help="Command line arguments for --file arguments if applicable")
    options, args = parser.parse_args()
    if options.config:
        configuration = getConfiguration(options.config)
        init(configuration, conn=None)
    else:
        init()
    agility = a = universal.agility
    agility._initPlugins()
    #execute python file or first argu

    if options.filename or (len(args) > 0 and args[0].endswith('.py')):
        if options.filename:
            filename = options.filename
        else:
            filename = args[0]
            args = args[1:]
        sys.argv = sys.argv[0:1] + args
        pythonpath.addPath(os.path.dirname(filename))
        exec_ns = {
            '__name__': '__main__',
            'a': a,
            'agility': agility,
            'argv': options.fileargs.split() if options.fileargs else []
        }
        exec(compile(open(filename).read(), filename, 'exec'), exec_ns)
        sys.exit(0)
    #start logserver
    elif options.command:
        exec(options.command)
        sys.exit(0)

    ipshell()


if __name__ == '__main__':
    main()
    