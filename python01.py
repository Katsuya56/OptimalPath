# なんちゃってダイクストラ法(ほとんど自分でアルゴリズムを考えたので多分アルゴリズム違う)
startpoint = "S"
carentpoint = startpoint

def serching(serching_point, no_in=[]):
    return_formats = []
    return_format = {"path": [], "len": None}
    for i in path_lists:
        if serching_point in i:
            else_val = {i[0],i[1]}.difference(serching_point).pop()
            # 早期コンテニュー
            if len(no_in) != 0:
                if else_val in no_in:
                    continue

            return_format["path"] = []
            return_format["len"] = None
            return_val = return_format.copy()
            

            if "S" in i:
                return_format["path"] = ["S", serching_point]
                return_format["len"] = i[2]
                return return_format
            else:
                if else_val in Optimalpath.keys():
                    return_val["path"] = Optimalpath[else_val]["path"]
                    return_val["len"] = Optimalpath[else_val]["len"]
                else:
                    no_in1 = no_in.copy()
                    no_in1.append(serching_point)
                    return_val = serching({i[0],i[1]}.difference(serching_point).pop(), no_in=no_in1)
                    if return_val == None:
                        no_in.append(serching_point)
                        continue

                return_format["path"] = return_val["path"] + [serching_point]
                return_format["len"] = return_val["len"] + i[2]
                return_formats.append(return_format.copy())
    if len(return_formats) == 0:
        return None

    cnt = 0
    lens = return_formats[0]["len"]
    cnt = 0
    lens = return_formats[0]["len"]
    for i in range(1,len(return_formats)):
        if return_formats[i]["len"] < lens:
            lens = return_formats[i]["len"]
            cnt = i
    
    return return_formats[cnt]


# A~Iまでの最短経路
vals = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
Optimalpath = {}

path_lists = [
    ["S", "A", 2],
    ["S", "B", 1],
    ["S", "C", 2],
    ["A", "D", 3],
    ["B", "D", 8],
    ["B", "E", 2],
    ["C", "E", 5],
    ["C", "F", 1],
    ["D", "G", 1],
    ["D", "E", 6],
    ["E", "G", 4],
    ["E", "H", 7],
    ["E", "I", 4],
    ["E", "F", 5],
    ["F", "I", 5],
    ["G", "H", 1],
    ["H", "I", 5]
]

for serching_point in vals:
    d = serching(serching_point)
    print(serching_point,d["path"],d["len"],end="\n\n")
    Optimalpath[serching_point] = d