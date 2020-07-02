from perfTabs import *
from sortingDigraphs import NormedQuantilesRatingDigraph
#from randomPerfTabs import RandomCBPerformanceTableau
#from randomPerfTabs import Random3ObjectivesPerformanceTableau
#from randomPerfTabs import RandomPerformanceGenerator
#from randomPerfTabs import RandomPerformanceTableau
from performanceQuantiles import PerformanceQuantiles
from outrankingDigraphs import BipolarOutrankingDigraph as BipolarOD
from linearOrders import CopelandOrder, NetFlowsOrder, KohlerOrder
from sortingDigraphs import NormedQuantilesRatingDigraph
from sortingDigraphs import QuantilesSortingDigraph
from sparseOutrankingDigraphs import PreRankedOutrankingDigraph
from sortingDigraphs import QuantilesSortingDigraph

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
###Q5###
# load quantile info from file
#t = PerformanceTableau('historicalData_28')
#qs_5 = QuantilesSortingDigraph(t,limitingQuantiles=15)
#print('-'*5, 'showSorting''-'*5 )
#qs_5.showSorting()
#input("Press Enter to continue...")
#print('-'*5, 'showQuantileOrdering','-'*5)
#qs_5.showQuantileOrdering(strategy='average')
#input("Press Enter to continue...")
#bg = PreRankedOutrankingDigraph(qs_5,quantiles=15)
#print('-'*5, 'showDecomposition','-'*5)
#bg.showDecomposition()
#input("Press Enter to continue...")
#print('-'*10, 'Q5', '-'*10)
#hiD = PerformanceTableau('historicalData_28')
#rt = RandomPerformanceTableau(numberOfActions=100,numberOfCriteria=15,seed=100)
#pq = PerformanceQuantiles(rt,numberOfBins = 15,LowerClosed=True)
#nqr = NormedQuantilesRatingDigraph(hiD,tab)
#nqr.showQuantilesRating()
print('-'*10, 'Q5', '-'*10)
hiD = PerformanceTableau('historicalData_28')
pq = PerformanceQuantiles(hiD,numberOfBins=15,LowerClosed=True,Debug=False)
pq.showHTMLLimitingQuantiles(Transposed=True)
pq.updateQuantiles(tab,historySize=None)
nqr = NormedQuantilesRatingDigraph(pq,tab)
nqr.showQuantilesRating()
nqr.showHTMLRatingHeatmap()
input("Press Enter to continue...")


###Q6###
print('-'*10, 'Q6', '-'*10)
qs = QuantilesSortingDigraph(tab, limitingQuantiles=3,LowerClosed=False)
qs.showHTMLSorting()
input("Press Enter to continue...")

###Q7###
print('-'*10, 'Q7', '-'*10)
shortlist = {'set' : ['s1917', 's0032', 's1714', 's0578', 's1775', 's0624',
                      's1430', 's1878', 's1691', 's0121', 's1210', 's1950',
                      's0251', 's0928', 's1682']}
for ct in ['set']:
    print(format(ct))
    actionsSubset = shortlist[ct]
    tPart = PartialPerformanceTableau(tab,  actionsSubset)
    tBiOutR = BipolarOD(tPart)
    tBiOutR.showRubisBestChoiceRecommendation()
   
print('-'*10, 'END', '-'*10)
