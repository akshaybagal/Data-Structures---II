class TrieNode:
    def __init__(self,ch, EndOfWordFlag):
        self.char = ch;
        self.endofWord = EndOfWordFlag;
        self.lst = []

class Trie:
    def __init__(self):
        self.root = TrieNode("", False)
    
    def insert(self, s):
        base = self.root
        for i in range(len(s)):
            flag = False
            for j in range(len(base.lst)):
                if base.lst[j].char == s[i]:
                    flag = True
                    base = base.lst[j]
                    break
            if(flag == False):
                if(i == len(s)-1):
                    EndOfWordFlag = True
                else:
                    EndOfWordFlag = False
                n = TrieNode(s[i], EndOfWordFlag)
                base.lst.append(n)
                base = n
                
                    
    
    def Exists(self,s):
        base = self.root
        EndOfWordFlag = False
        for i in range(len(s)):
            flag = False
            for j in range(len(base.lst)):
                if(base.lst[j].char==s[i]):
                    EndOfWordFlag = base.lst[j].endofWord
                    base = base.lst[j]
                    flag = True
                    break
            if(flag == False):
                return "Does Not Exist!"
        if(EndOfWordFlag != True):
            return "Does Not Exist!";
        return "Exists!"

trie = Trie();
ch = 'Y'
while(ch == 'Y'):
    print("\n========================================")
    print('\nStart entering dictionary words:')
    print('\nEnter 0 when done')
    mdict = []
    ind = '1'
    while(ind != '0'):
        ind = str(input())
        mdict.append(ind);
    contn = '1'
    for i in range(len(mdict)):
        trie.insert(mdict[i])
    while(contn == '1'):
        print("Enter word to search:")
        toSearch = str(input())
        print("\n"+trie.Exists(toSearch));
        print("\nContinue 1. Search Word: Enter 1 \n\t 2. Start new Dictionary: Enter 2 \n\t 3. Exit: Enter 9");
        contn = str(input())
    if(contn == '2'):
        ch = 'Y';
    elif(contn != '2'):
        ch = 'N'
    
