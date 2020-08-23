# given an input string, output its arithmetic operation results. Note: 
# Only support positive integer, if at any point you get 
# an negative number or non-integer, return false
# "(3 + (3 * 5)) / 2"  -> return 9
# "((3 - 5) + 12) / 2" -> return false because 3 - 5 = -2, which is a negative number
# "8 / 12" -> return false because it is a non-integer

# You are also given a split function that takes in a string, 
# and output a tuple (left_operand, operator, right_operand)
# split("3 / 5") => output ("3", "/", "5")
# split("5") => output("5")
# split("(10 / 2) / 5") => output("(10 / 2)", "/", "5")

def calculate(st):
    def evaluate(s):
        if len(split(s)) < 3:
            return int(s)
        else:
            left, op, right = split(s)
            left_res = evaluate(left)
            right_res = evaluate(right)
            if left_res == False or right_res == False:
                return False
            
            res = eval(str(left_res) + op + str(right_res))
            if not res.is_integer() or res < 0:
                return False

            return res

    return evaluate(st)

# 面试题：
# 我没有见过这道题啊，不知道leetcode上有没有原题：
# 一个可以横竖无限扩张的棋盘，两个玩游戏的人分别用red 和blue。
# api是这样：
# insert(column, color) 可以在棋盘对应的列下放自己的颜色。
# 赢的条件：棋盘连续（行或者列）有k个同样的颜色，则该颜色赢。
# 每次insert要判断有没有赢家，如有就返回赢家。有赢家后游戏停止不会继续。

# 解法：
# 用hashmap来储存每列的棋子顺序（一个list）不可以用2d array因为可能出现第一次在第-1列玩，第二次去1000000列玩。
# 判断有没有vertical k个连续：从最后一个元素开始判断有没有k个同样颜色就行。
# 判断有没有horizontal k个连续，反向双指针从所在column出发，判断两个方向有几个同样颜色。



# -------------------------------------------
# 要求设计以下游戏，有两个player，R和B
# 某一个状态：
#                  R
#                R B
# --------------------
# ... -2 -1 0 1 2 ...

# player B 选择 column 1 之后，B放在column 1上方：

#                B R
#                R B
# --------------------
# ... -2 -1 0 1 2 ...

# 横轴是无限长的。 设计数据结构来initialize这个game，并且实现insert() 这个function。

from collections import defaultdict
from itertools import groupby
class Game:
    def initialize(self, k):
        self.grid = defaultdict(list)
        self.k = k
        
    
    def insert(self, column, color):
        self.grid[column].append(color)
        row = len(self.grid[column])
        res = self.check(column, row, color):
        return res 

    def check(self, col, row, color):
        # check verticle
        lst = self.grid[col]
        cnt = 0
        for i in range(row-1, -1, -1):
            if lst[i] == color:
                cnt += 1
        if cnt >= k:
            return color 
            
        # grouped = list(groupby(self.grid[col]))
        # for player, count in grouped: 
        #     if count >= k:
        #         return player

        # check horizontal

        cnt = 0
        curr = col
        
        while len(self.grid[curr]) > row and self.grid[curr][row] == color:
            curr += 1
            cnt += 1
        
        curr = col-1
        while len(self.grid[curr]) > row and self.grid[curr][row] == color:
            curr -= 1
            cnt += 1
        
        if cnt >= k:
            return color 
        
        return None


# leetcode 443
# 第一问：LC 443，不用改input，直接输出List<Tuple<char, int>>

# 第二问：新的这个function会被call很多次，每次还是给一个string，比如第一次aaabbb，
# 第二次bbccd，第三次ee，对应的输出分别是(a - 3)，(b - 5, c - 2)，(d - 1)，
# 也就是不输出每个string最后一个tuple的结果，而是要等下一次输入看还有没有一样的char相连，然后一起输出结果；
# 比如如果有一次的输入是kkk，那就什么都不输出

# 第三问：新的function的输入有一个sequence number和一个string，
# 比如(2, ccc)，(1, bbc)，(0, aa)，(3, cdd)，那么在接受前两个输入的时候不用输出什么东西，
# 但在第三个输入出现的时候，因为我们已经有了从0到2的所有输入，所以输出整合的string对应的压缩结果，
# 也就是aabbcccc对应的(a - 2, b - 2)；注意我们不输出c的结果，而是在接收3对应的string以后，
# 继续输出(c - 5)；整体的意思就是一旦有了从头开始的一段连续的string，就输出它对应的结果，
# 然后等下一段连续的string出现
from collections import defaultdict

class Solution:
    def compress(self, chars: List[str]) -> int:
        curr = chars[0]
        cnt = 0
        res = []
        for c in chars:
            if c == curr:
                cnt += 1
            else:
                res += [curr, str(cnt)]
                curr = c
                cnt = 1
        res += [curr, str(cnt)]
        return res

    def second(self, s):
        res = self.compress(s)
        if self.leftover:
            tmp = res[-1]
            res = [self.leftover] + res[:-1]
            self.leftover = tmp
            return res
        else:
            self.leftover = res[-1]
            return res[:-1]

    def third(self, num, s):
        if not self.seq:
            self.seq = {}
            self.max_num = 0
            self.start = 0
        self.max_num = max(self.max_num, num)
        self.seq[num] = s

        if len(self.seq) == self.max_num + 1:
            #output
            res = []
            for key in range(self.start, self.max_num+1):
                res += self.second(self.seq[key])
            self.start = self.max_num+1
            return res


    
