### worm-graph

Scripts for querying connectome data for the nematode *C. elegans*, gathered from data provided by the PIT Bioinformatics group at [braingraph.org](https://braingraph.org/cms/c-elegans/).

#### Usage

Worm-graph can be used to both create graphs of neuronal connections and to receive the number of connections between any given neurons. There are two main use-cases:

**1.** Getting connection counts *from* a particular neuron.

This is the simplest way to use worm-graph.

>wormgraph.py <ROOT-NEURON\>

Each connected neuron and appropriate number of connections is printed to stdout.

**2.** Getting connection counts *from* a particular neuron and *to* any given neuron or neurons.

Similar to above, but destination neurons are passed as optional arguments with the *-t* flag.

>wormgraph.py <ROOT-NEURON\> -t <NEURON\>

Any number of destination neurons may be passed, as long as they are preceeded by a *-t* flag.

To produce a graph rather than a simple connection count, pass the *-g* flag as an argument.

### Dependencies

Worm-graph depends on:

* matplotlib
* pandas
* numpy
* networkx
* argparse
