from sklearn.cluster import KMeans

class Image:
    def read_img(self, path):
        f = open(path)
        x = 100
        self.t = f.readline() #type
        f.readline()
        self.r, self.c = f.readline().split(' ') #row, col
        self.max = f.readline() #max value
        self.data = f.readline() #img data

        self.pix = []
        for i in range(0,len(self.data)-2,3):
            self.pix.append(list(self.data[i:i+3]))

        self.data = [] # reset type
        for i in range(0,len(self.pix)):
            l = []
            for j in range(0,len(self.pix[i])):
                l.append(ord(self.pix[i][j]))
            self.data.append(l) #append converted values

    def write_img(self, path, m, pix):
        f = open(path, 'wr')
        f.write('P6\n')
        f.write('120') #new size
        f.write(' ')
        f.write('120')
        f.write('\n')
        f.write(str(m)) #max pixel value
        f.write('\n')

        #r zfill(3)
        #g zfill(3)
        #b zfill(2)
        for i in range(0, len(pix), 3):
            for j in range(0,3):
                if j == 0: #red
                    f.write(bin(pix[i+j])[2:].zfill(3))
                if j == 1: #green
                    f.write(bin(pix[i + j])[2:].zfill(3))
                if j == 2: #blue
                    f.write(bin(pix[i + j])[2:].zfill(2))
            #print bin(pix[i+j]).zfill(8)
            #f.write(bin(pix[i]))
        f.close()




img = Image()
img.read_img('/Users/davidclevenger/PycharmProjects/Pattern-Recognition/flowers.ppm')
print img.t, img.max

model = KMeans(8,n_jobs=-1)
y = model.fit(img.data)
print y.labels_
img.write_img('/Users/davidclevenger/PycharmProjects/Pattern-Recognition/8bit.ppm',3,y.labels_)


