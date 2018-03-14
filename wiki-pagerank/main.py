import json
import logging
import snap
import operator
import time

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

PATH_JSON = "result.json"

def read_file(filePath):
    logging.info("read file json")
    with open(filePath, "r") as file:
        rs = file.read()
    list_data = json.loads(rs)
    logging.info("so luong phan tu : {}".format(len(list_data)))
    return list_data


def map_id(list_data):
    """
        map cac url voi 1 id
    """
    list_node = []
    for i in list_data:
        list_node.append(i["src"])
        list_node.extend(i["dst"])
    set_node = set(list_node)
    dict_map_id = {}
    dict_map_id_inverse = {}
    id = 0
    for node in set_node:
        dict_map_id[id] = node
        dict_map_id_inverse[node] = id
        id +=1
    logging.info("so node la : {}".format(len(set_node)))
    return set_node,dict_map_id,dict_map_id_inverse


def transform_data(set_node,list_data,map_id,map_id_inverse):
    """
        chuyen url -> id
    """
    list_data_transform = []
    for data in list_data:
        node = {}
        node["src"] = map_id_inverse[data["src"]]
        list_dst = []
        for url in data["dst"]:
            list_dst.append(map_id_inverse[url])
        node["dst"] = list_dst
        list_data_transform.append(node)
    set_node_transform = []
    for node in set_node:
        set_node_transform.append(map_id_inverse[node])

    return set_node_transform,list_data_transform


def create_graph(list_node,list_data):
    logging.info("create graph")
    G1 = snap.TNGraph.New()
    for node in list_node:
        G1.AddNode(node)
    for data in list_data:
        node_src = data["src"]
        for node_dst in data["dst"]:
            G1.AddEdge(node_src,node_dst)
    return G1


def compute_page_rank(graph):
    logging.info("compute pagerank")
    PRankH = snap.TIntFltH()
    snap.GetPageRank(graph, PRankH)
    for item in PRankH:
        print item, PRankH[item]
    return PRankH


def get_max_rank(rank):
    max = 0
    for item in rank:
        if rank[item] > max:
            max = rank[item]
            best = item
        print item, rank[item]
    return best


def get_top(rank,top=100):
    logging.info("top {} :".format(top))
    top = 0 - top
    sorted_rank = sorted(rank.items(), key=operator.itemgetter(1))
    tuple_top_rank = sorted_rank[top:]
    top_rank = { x:y for x,y in tuple_top_rank}
    return top_rank


def parse_rank(rank):
    logging.info("parse rank")
    new_rank = {}
    for item in rank:
        new_rank[item] = rank[item]
    return new_rank


if __name__ == "__main__":
    time_start = time.time()
    list_data = read_file(PATH_JSON)
    set_node,map_id,map_id_inverse = map_id(list_data)
    set_node_transform,list_data_transform = transform_data(set_node,list_data,map_id,map_id_inverse)
    graph = create_graph(set_node_transform,list_data_transform)
    rank = compute_page_rank(graph)
    new_rank = parse_rank(rank)
    best = get_max_rank(new_rank)
    top_rank = get_top(new_rank,top=100)

    for id,value in top_rank.items():
        print("{} : {} ".format(map_id[id],value))

    logging.info("thoi gian chay : {}s".format(time.time() - time_start))





