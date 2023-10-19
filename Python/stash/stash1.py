list_n = [11, 22, 33, 44, 55]


def func(pre, n):
    return (pre * 13337 + n) % 19260817


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.res = -1
        self.ans = -1
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

    def build_tree(self, depth):
        if depth > 0:
            for n in list_n:
                child = TreeNode(n)
                self.add_child(child)
                child.res = func(self.res, n)
                child.ans = func(child.res, 66)
                if child.ans == 7748521:
                    print(f"find it! {child.res} - {child.value} - {child.ans}")
                    # 输出路径
                    node = child
                    path = []
                    while node:
                        path.append(node.value)
                        node = node.parent
                    print(path[::-1])
                    exit(0)
                child.build_tree(depth - 1)

    def add_layer_to_leaves(self):
        if not self.children:
            for n in list_n:
                child = TreeNode(n)
                self.add_child(child)
                child.res = func(self.res, n)
                if child.res == 6475027:
                    print("find it!")
                    exit(0)
        else:
            for child in self.children:
                child.add_layer_to_leaves()

    def __str__(self, level=0):
        ret = "  " * level + repr(self.value) + "  ===  " + repr(self.res) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret


# # 创建根节点并构建树
# root = TreeNode(1337)
# root.res = 1337
# root.build_tree(11)  # 3 表示树的深度

# # 在叶子节点上添加一层新节点
# # root.add_layer_to_leaves()

# # 打印整个树
# print(root)

# result = [44, 22, 33, 55, 33, 44, 11, 11, 11, 55]
# # 验证结果
# pre = 1337
# for n in result:
#     pre = func(pre, n)
# pre = func(pre, 66)
# print(pre)

origin = ["a", "e", "i", "o", "u"]
reflect = [11, 22, 33, 44, 55]


def origin_str_to_reflect_list(origin_str):
    res = []
    for c in origin_str.lower():
        res.append(reflect[origin.index(c)])
    return res


def reflect_list_to_origin_str(reflect_list):
    res = []
    for n in reflect_list:
        res.append(origin[reflect.index(n)])
    res = "".join(res).upper()
    return res


# 验证结果
def check_res_list(res_list):
    pre = 1337
    for n in res_list:
        pre = func(pre, n)
    pre = func(pre, 66)
    return pre


# 整合两个检查结果的函数
def check_res(res):
    if isinstance(res, str):
        res_str = res
        res_list = origin_str_to_reflect_list(res_str)
        pre = check_res_list(res_list)
        print(f"res_str: {res_str}, res_list: {res_list}, pre: {pre}")
    elif isinstance(res, list):
        res_list = res
        res_str = reflect_list_to_origin_str(res_list)
        pre = check_res_list(res_list)
        print(f"res_str: {res_str}, res_list: {res_list}, pre: {pre}")
    else:
        print("wrong type")


check_res("OEIUIOAAAU")
check_res("AAUEUOUOEUE")
check_res("EUOIAOOEEAA")
check_res("AEEAOAOIAOOA")
check_res("EAAAEUIAUEEA")
check_res("EIIUEIIIEEUO")


result1 = [44, 22, 33, 55, 33, 44, 11, 11, 11, 55]
reflect_list_to_origin_str(result1)
check_res_list(result1)
