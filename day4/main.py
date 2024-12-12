class Day4:
    def __init__(self):
        self.ws =[]
        with open('input.txt','r') as f:
            for line in f.readlines():
                self.ws.append([x for x in line if x != '\n'])
        self.part1 = ['XMAS','SAMX']
        self.part2 = ['MAS','SAM']
        self.m = len(self.ws)
        self.n = len(self.ws[0])
        self.p1 = 0
        self.p2 = 0
    
    def search(self):
        self.rowsearch()
        self.colsearch()
        self.diagsearch()
    
    def rowsearch(self):
        for row in self.ws:
            for i in range(self.n - 3):
                self.p1 += ''.join(row[i:i+4]) in self.part1 # x in part1?
    
    def colsearch(self):
        for col in zip(*self.ws): # Transpose the matrix/Col and row swap
            for i in range(self.n - 3):
                # join is building the string from individual words in mat
                self.p1 += ''.join(col[i:i+4]) in self.part1 # x in part1

    def diagsearch(self):
        for row in range(self.m - 3):
            for col in range(self.n - 3):
                diag1 = ''.join([self.ws[row][col],
                                self.ws[row+1][col+1],
                                self.ws[row+2][col+2],
                                self.ws[row+3][col+3]])

                diag2 = ''.join([self.ws[row+3][col],
                                self.ws[row+2][col+1],
                                self.ws[row+1][col+2],
                                self.ws[row][col+3]])
                self.p1 += diag1 in self.part1
                self.p1 += diag2 in self.part1
    def mas(self):
        for row in range(self.m - 2):
            for col in range(self.n - 2):
                diag1 = ''.join([self.ws[row][col],
                                self.ws[row+1][col+1],
                                self.ws[row+2][col+2]])
                diag2 = ''.join([self.ws[row+2][col],
                                self.ws[row+1][col+1],
                                self.ws[row][col+2]])
                self.p2 += diag1 in self.part2 and diag2 in self.part2

if __name__ == "__main__":
    day = Day4()
    day.search()
    day.mas()
    print(day.p2)
