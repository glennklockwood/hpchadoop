coord
=========

We did not go over this example in class, but it sorts through a file that has 
the general format:

1 Siloxane      3732     69.86927969     18.68401336      5.15718024
1 Siloxane      3733     39.53876162     74.60201783      5.07252075
1     SiO4      3734     19.62114272     23.08312809      5.01756597
1     SiO4      3735     30.39621836    103.97544976      5.01249768

where the columns are timestamp (integer), specie identifier (string), atom id
(integer), x position (float), x position (float), and z position (float).  The
code counts up how many types of each specie is present at each time step for
every time step to show how the concentrations of different species changes
during a simulation.

Files related to the coordination number analysis map/reduce application:

* analyzecoord.py - the original analysis code
* mapper.py - the mapper component of the analysis code
* reducer.py - the reducer component of the analysis code
* presenter.py - the post-map/reduce formatter for the analysis code
* mapreduce.py - a neatly packaged script encapsulating map/reduce/present
