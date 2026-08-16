#  Graph of Failures
## 2026-08-16

things happen for a reason. i want to build a graphical network of historic failure events, where each failure event points to another failure event, where the connection is a weighted blame. 

for example, if the entire network of events is that john fell off his bike 80% because he was not paying attention to the terrain and 20% because his bike tires were too bald, there would be a node for "john fell off bike", a node for "john did not pay attention to the terrain" and a node for "john's bike tires were bald". each node has a measure of catastrophe (call it MoC index for now), where a higher number may indicate high fatality, environmental destruction, or other means of harm. "john fell off his bike" may have a MoC of 0.5 (because he broke a spine and was paralyzed for 6 years, and this also wrecked a bike that embodied X kg CO2). There would be an edge with weight 0.8 from the "john fell off his bike" to "john did not pay attention to the terrain". similarly, there would be an edge with weight 0.2 from “john fell off his bike” to “john’s tires were bald”. in this network of only 3 events, this concludes the entire graph.

the direction of this edge if the direction of blame. note that this is not the opposite as the direction of causation, because i'm only looking at the cause of failure, not the cause of everything.

it would be interesting to build this on different network of events. this could evolve not only into cool graphical figures, but also failure analysis tools. yeah, i’m basically creating a fishbone diagram but in the form of a graph structure that allows for graph analysis.
