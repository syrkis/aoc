inp = [l for l in "hxbxwxba"]

class Password:
    def __init__(self, pswd):
        self.pswd = pswd
    
    def next(self):
        pswd = self.pswd
        while not self.check(pswd):
            pswd = inc(pswd)
        self.pswd = pswd
    
    def check(self, pswd).
        alpha = 'abcdefghijklmnopqrstuvxyz'
        three = set([alpha[i:i+3] for i in range(len(alpha) -3)])
        ambug = set('i', 'o', 'l')
         

    def inc(self, pswd):
        
