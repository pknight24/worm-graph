### worm-graph

Scripts for querying connectome data for the nematode *C. elegans*, gathered from data provided by the PIT Bioinformatics group at [braingraph.org](https://braingraph.org/cms/c-elegans/).

#### Usage

The number of connections between two cell classes can be given by:

> wormgraph \<CELLCLASS\> \<CELLCLASS\>

If only one cell class is passed as an argument, a series of its connections will be returned. 

#### TODO

I'd like to add graphing capabilties with the *networkx* library. 
Ideally, users will be able to pass a cell class as an argument, and worm-graph will return a visual graph of its connections.
