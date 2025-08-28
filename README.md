# Tukey-HSD-no-replicates
Perform Tukey's range test / multiple comparisons with only Mean, SD and Replicate number (number of observations). No need for replicate values. ANOVA not included
I AM NOT A STATISTICIAN AND CARE LITTLE FOR STATISTICS. USE AT OWN RISK. 
It looks like it works fine. The statsmodels.stats.libqsturng.psturng library gives only very few decimal datapoints for p-values, if your data is reasonably strong you may need a different tool to convert from q-values.

You will need to format your data as such (example data adapted from https://www.biostathandbook.com/onewayanova.html):
name	mean	SD	N
Tillamook	0.0802	0.011349361	10
Newport	0.0748	0.008041921	8
Petersburg	0.103442857	0.015007032	7
Magadan	0.0780125	0.012108617	8
Tvarminne	0.0957	0.0118323	6


Copy into clipboard and run code
