# fonte das distâncias
# https://www.distanciaentreascidades.com.br/
# acesso em 07/10/2022
# Exitem estados que não possuem ligação por estrada diretamente. 
 
import matplotlib.pyplot as plt
import networkx as nx
from networkx import Graph

def plotagem(G,colors):
    img = plt.imread(r"mapa.png")
    fixed_positions={
        "AP":(461,168),
        "AC":(156,350),
        "AM":(300,226),
        "RR":(285,115),
        "RO":(226,327),
        "PA":(508,190),
        "MT":(370,454),
        "MS":(397,540),
        "PR":(495,632),
        "SC":(509,669),
        "RS":(460,715),
        "SP":(543,597),
        "MG":(590,529),
        "ES":(658,536),
        "BA":(689,404),
        "SE":(717,368),
        "AL":(741,343),
        "PB":(755,300),
        "PE":(755,317),
        "RN":(748,274),
        "CE":(690,237),
        "PI":(613,259),
        "MA":(584,214),
        "TO":(509,352),
        "GO":(494,473),
        "DF":(519,445),
        "RJ":(603,584)
    }
    fixed_nodes = fixed_positions.keys()
    pos = nx.spring_layout(G, pos = fixed_positions, fixed = fixed_nodes)  # Seed for reproducible layout
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels = labels,verticalalignment= 'baseline', alpha = 0.4)
    nx.draw(G, pos, node_size = 20, with_labels = False, edge_color = colors)  
    plt.imshow(img)
    plt.show()

def montar_grafo(arestas):
    G.add_weighted_edges_from(arestas)
    nx.set_edge_attributes(G,color,'color')
    for edge in G.edges:
        G.edges[edge]['color'] = 'black'    
    

def cores(G,edges):
    colors = [G[u][v]['color'] for u,v in edges]
    return colors

def cores_dijkstra(G,resultado_dijkstra):
    for i in range(len(resultado_dijkstra)-1):
        G.edges[resultado_dijkstra[i],resultado_dijkstra[i+1]]['color'] = 'red'
    return G



class PrintGraph(Graph):
    """
    Example subclass of the Graph class.

    Prints activity log to file or standard output.
    """
estado_inicial = "RS"
estado_final = "CE"
dijkstra = False
  
arestas=[   ('DF','GO',209),
            ('RR','AM',748),
            ('AM','AC',1399),
            ('AM','PA',3051),
            ('AM','RO',891),
            ('PA','AP',1905),
            ('PA','MA',801),
            ('PA','TO',1195),
            ('PA','MT',2374),
            ('RO','MT',1448),
            ('TO','MA',1247),
            ('TO','BA',1450),
            ('TO','GO',862),
            ('MT','GO',935),
            ('MT','MS',709),
            ('MS','GO',843),
            ('MS','PR',996),
            ('MS','SP',1018),
            ('SC','RS',456),
            ('SC','PR',303),
            ('PR','SP',405),
            ('SP','RJ',431),
            ('SP','MG',585),
            ('RJ','ES',517),
            ('ES','BA',1158),
            ('RJ','MG',436),
            ('GO','MG',889),
            ('MG','BA',1408),
            ('MG','ES',518),
            ('BA','SE',324),
            ('MA','PI',439),
            ('PI','CE',592),
            ('PI','PE',1131),
            ('CE','RN',515),
            ('PE','PB',118),
            ('PB','RN',181),
            ('PE','AL',258),
            ('AL','SE',269)
        ]
G = PrintGraph()
color=[]
montar_grafo(arestas)
DFS_list = nx.dfs_edges(G, source = estado_inicial )

print("DFS:")
for edge in DFS_list:
    print(edge)
if dijkstra:
    resultado_dijkstra = nx.dijkstra_path(G,estado_inicial,estado_final)
    print("DIJKSTRA:")
    print(resultado_dijkstra)
    G=cores_dijkstra(G,resultado_dijkstra)


edges=G.edges()
colors = cores(G,edges)
plotagem(G,colors)