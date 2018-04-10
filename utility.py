class Pixel:
    def set(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __getitem__(self, item): #overload [] operator for easier indexing
        if item == 0:
            return self.r
        elif item == 1:
            return self.g
        elif item == 2:
            return self.b

class Image:
    def read_img(self, path):
        f = open(path)
        x = 100
        self.t = f.readline() #type
        f.readline()
        self.r, self.c = f.readline().split(' ') #row, col
        self.max = f.readline() #max value
        self.max = int(self.max)
        self.raw = f.readline() #raw image data

        self.pix = []
        for i in range(0,len(self.raw)-2,3):
            p = Pixel()
            Pixel.set(p,ord(self.raw[i]), ord(self.raw[i+1]), ord(self.raw[i+2]))
            self.pix.append(p)

    def write_img(self, path):
        f = open(path, 'wr')
        f.write('P6\n')
        f.write(self.r)
        f.write(' ')
        f.write(self.c)
        f.write('\n')
        f.write(str(self.max))
        f.write('\n')

        for i in range(0, len(self.pix)):
            f.write(chr(self.pix[i].r))
            f.write(chr(self.pix[i].g))
            f.write(chr(self.pix[i].b))

        f.close()

#ndarray to pixel list
def convert(arrays):
    out = []
    for i in range(len(arrays)):
        p = Pixel()
        p.set(int(arrays[i][0]),int(arrays[i][1]),int(arrays[i][2]))
        out.append(p)
    return out