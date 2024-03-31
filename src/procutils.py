from functools import cache


ref = {
    'or': "ANY",
    'and': "ALL"
}

@cache
def buildTree(data, course: str):
    temp = []
    children = data[2]
    # print(children)
    if len(children) > 0:

        if (children[0] in ['and', 'or']):
            temp.append({
                ref[children[0]]: children[1:]
            })
            

        else:
            for child in children:
                print(child)

    # print(temp)


def getDependentTrees(data, course):
    # expect data to be request["courses"]
    q = []
    ps = data[course][2]

    for c in ps:
        if not (c in ["or", "and"]):
            if type(c) == list:
                # list of more stuff
                ps.extend(c)
            elif type(c) == dict:
                # actual course
                q.append(c)

    return q

