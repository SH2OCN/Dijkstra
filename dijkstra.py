# -*- coding: utf-8 -*-
"""
【 Dijkstra算法 in Python3.6】
2018/9/4
@author: SH2OCN
"""

def show_routes(pre,k):
    '''Return the shortest routes from source 'k' to all points.
       (sub-function of dijkstra() )
    Input:
        pre: store the previous point of each point
        k: the source point
    Output:
        ans: store the dijkstra routes
    '''
    ans = [[i] for i in range(len(pre))] #initialize ans    
    for i in range(len(pre)):
        r = ans[i]                       #current route
        while r[-1] != k:                #while this route not finished
            r.append(pre[r[-1]])         #append the previous point to r
        r.reverse()                      #reverse r sothat start from 'k'
    print('The Dijkstra routes are:')
    [print(item) for item in ans]
    return ans

def dijkstra(n,k,e):
    '''Return shortest routes from k to all n points by dijkstra method.
    Input:
        n: number of points
        k: the source point
        e: edge matrix
    Output:
        ans: the dijkstra routes
    '''
    #initialize:
    pre = [k for _ in range(n)]   #记录路径中每一个点的上一个点
    dis = e[k][:]                 #记录每条预估最短路径的长度
    s = [0 for _ in range(n)]     #s集合包含所有已被选中的点（置为1）
    s[k] = 1                      #初始只有源点k
        
    for i in range(n-1): #一共进行n-1次大循环，每次往s集合中添加一个选中的点u
        
        min_dis = z
        for j in range(n):  #选出当前dis中最小值对应的点u
            if s[j] == 0 and dis[j] < min_dis:
                min_dis = dis[j]
                u = j    
        s[u] = 1            #把u加入s集合中
        
        for j in range(n): #尝试用刚加入的u更新dis
            if s[j] == 0 and e[u][j] < z and dis[u] + e[u][j] < dis[j] :
                dis[j] = dis[u] + e[u][j]
                pre[j] = u
    
    ans = show_routes(pre,k) 
    print('\nThe distances are:',dis)  
    return ans   
            
           
if __name__ == '__main__':
    n = 6   #number of points
    k = 0   #source point
    z = 1e5 # infinity
    e = [[0,1,12,z,z,z], #test case 1
         [z,0,9,3,z,z],
         [z,z,0,z,5,z],
         [z,z,4,0,13,15],
         [z,z,z,z,0,4],
         [z,z,z,z,z,0]
        ]
    '''
    e = [[0,6,3,z,z,z], #test case 2
         [6,0,2,5,z,z],
         [3,2,0,3,4,z],
         [z,5,3,0,2,3],
         [z,z,4,2,0,5],
         [z,z,z,3,5,0]
        ]
    '''
    ans = dijkstra(n,k,e)
            
'''
【tips】
1 邻接矩阵e的表达方式，是以列表为元素的列表
2 e[i][j]的值代表从i点到j点的弧的权重
3 要在函数外预设好一个代表无穷大的值，如 z=1e5 (用来表示邻接矩阵中的无穷大)
4 图中各点的标号从0开始，而不是1
'''            
            
            
            
            
            
            
