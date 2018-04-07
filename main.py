from sklearn.cluster import KMeans

class Pixel:
    def set(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

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




img = Image()
img.read_img('/Users/davidclevenger/PycharmProjects/Pattern-Recognition/flowers.ppm')
#print img.t, img.max

#model = KMeans(8,n_jobs=-1)
#y = model.fit_transform(img.data)
#print y
img.write_img('/Users/davidclevenger/PycharmProjects/Pattern-Recognition/flowers-comp.ppm')


