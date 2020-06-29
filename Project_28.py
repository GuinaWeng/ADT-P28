
from perfTabs import *
import IPython
from IPython.display import Image
from outrankingDigraphs import BipolarOutrankingDigraph as BipolarOD
###Q1###
print('-'*10, 'Question1', '-'*10)
# load the tableau
tab = PerformanceTableau('perfTab_28')
print(tab)
tab.showHTMLPerformanceHeatmap(Correlations = True, ndigits = 0, colorLevels = 9)

input("Press Enter to continue...")

###Q2###
print('-'*10, 'Question2', '-'*10)
from outrankingDigraphs import BipolarOutrankingDigraph as BipolarOD
# bipolar outranking digraph
bipolar = BipolarOD(tab)
# compute chordless circuits
bipolar.computeChordlessCircuits()
# show computed chordless circuits
bipolar.showChordlessCircuits()

input("Press Enter to continue...")

###Q3###
print('-'*10, 'Question3', '-'*10)
#Copeland Ranking
cop = CopelandOrder(bipolar)
cop_corr = bipolar.computeOrdinalCorrelation(cop).get('correlation')
print(f'Correlation of Copeland order {cop_corr}')
#Kohler Ranking
koh = KohlerOrder(bipolar)
koh_corr = bipolar.computeOrdinalCorrelation(koh).get('correlation')
print(f'Correlation of Kohler order {koh_corr}')
#Netflows Ranking
netflow = NetFlowsOrder(bipolar)
netflow_corr = bipolar.computeOrdinalCorrelation(netflow).get('correlation')
print(f'Correlation of NetFlows order {netflow_corr}')

if cop_corr >= netflow_corr and cop_corr >= koh_corr:
    print('According to the Copeland order,the ranking is:')
    cop.showRanking()
elif netflow_corr >= cop_corr and netflow_corr >= koh_corr:
    print('According to the NetFlows order,the ranking is:')
    netflow.showRanking()
elif koh_corr >= netflow_corr and koh_corr >= cop_corr:
    print('According to the Kohler order,the ranking is:')
    koh.showRanking()
input("Press Enter to continue...")

###Q4###
print('-'*10, 'Q4', '-'*10)
qs = QuantilesSortingDigraph(tab, limitingQuantiles=15,LowerClosed=False)
qs.showHTMLSorting()
input("Press Enter to continue...")

###Q6###
print('-'*10, 'Q6', '-'*10)
qs = QuantilesSortingDigraph(tab, limitingQuantiles=3,LowerClosed=False)
qs.showHTMLSorting()
input("Press Enter to continue...")
