
from perfTabs import *
import IPython
from IPython.display import Image

###Q1###
print('-'*10, 'Q1', '-'*10)
# load the tableau
tab = PerformanceTableau('perfTab_28')
print(tab)
tab.showHTMLPerformanceHeatmap(Correlations = True, ndigits = 0, colorLevels = 9)

input("Press Enter to continue...")

###Q2###
print('-'*10, 'Q2', '-'*10)
from outrankingDigraphs import BipolarOutrankingDigraph as BipolarOD
# bipolar outranking digraph
bipolar = BipolarOD(tab)
# compute chordless circuits
bipolar.computeChordlessCircuits()
# show computed chordless circuits
bipolar.showChordlessCircuits()

input("Press Enter to continue...")
