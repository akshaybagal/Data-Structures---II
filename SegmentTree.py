class SegmentTree:
    def __init__(self, n, arr):
        self.tree = [0]*(400005)
        self.arr = arr
        self.start = 0
        self.end = n-1
    
    def buildUtil(self, node, start, end):
        tree = self.tree
        if(start == end):
            tree[node] = arr[start]
        else:
            mid = (start + end)//2
            self.buildUtil(2*node+1, start, mid)
            self.buildUtil(2*node+2, mid+1, end)
            if(tree[2*node+1] < tree[2*node+2]):
                tree[node] = tree[2*node+1]
            else:
                tree[node] = tree[2*node+2]
    
    def build(self):
        self.buildUtil(0, self.start, self.end)
    
    def findminUtil(self, node, start, end, l, r):
        tree = self.tree
        if(end < l or r < start):
            return 100005;
        
        if(l <= start and end <= r):
            return tree[node]
            
        mid = (start + end)//2
        min1 = self.findminUtil(2*node+1, start, mid, l, r)
        min2 = self.findminUtil(2*node+2, mid+1, end, l, r)
        if(min1 < min2):
            return min1
        else:
            return min2
    
    def findmin(self, l, r):
        return self.findminUtil(0, self.start, self.end, l, r)
    
    def updateUtil(self, node, start, end, idx, val):
        tree = self.tree
        if(start == end):
            tree[node] = val
        else:
            mid = (start + end)//2
            if(idx <= mid):
                self.updateUtil(2*node+1, start, mid, idx, val)
            else:
                self.updateUtil(2*node+2, mid+1, end, idx, val)
            if(tree[2*node+1] < tree[2*node+2]):
                tree[node] = tree[2*node+1]
            else:
                tree[node] = tree[2*node+2]

    def update(self, idx, val):
        self.updateUtil(0, self.start, self.end, idx, val)

n,q = map(int,input().strip().split(' '))
arr = list(map(int, input().strip().split(' ')))
segtree = SegmentTree(n,arr)
segtree.build()
while(q > 0):
    q -= 1
    op,l,r = map(str,input().strip().split(' '))
    if(op == 'q'):
        print(segtree.findmin(int(l)-1, int(r)-1))
    else:
        segtree.update(int(l)-1, int(r))