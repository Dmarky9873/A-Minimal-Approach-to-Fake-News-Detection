from pycallgraph2 import PyCallGraph
from pycallgraph2 import Config
from pycallgraph2 import GlobbingFilter
from pycallgraph2.output import GraphvizOutput

from GENERATE_DATABASE import main


config = Config()
config.trace_filter = GlobbingFilter(exclude=[
    'pycallgraph.*',
])

graphviz = GraphvizOutput(output_file='call-graph.png')

with PyCallGraph(output=graphviz, config=config):
    main()
