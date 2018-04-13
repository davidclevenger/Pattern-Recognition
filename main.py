from models import kmeans, winner_take_all, meanshift
from utility import Image, convert, performance
import sys

def main():
    ncolors = [256, 128, 64, 32, 16, 8, 4] #number of clusters
    bw = [1, 2, 5, 10, 15, 40] #bandwidth values
    img = Image()
    img.read_img('/Users/davidclevenger/PycharmProjects/Pattern-Recognition/flowers120.ppm')
    orig = img.pix

    #k_means
    print 'kmeans'
    for i in ncolors:
        tmp = convert(kmeans(i, orig))
        img.pix = tmp
        performance(i, orig, tmp)
        img.write_img('/Users/davidclevenger/PycharmProjects/Pattern-Recognition/kmeans' + str(i) + '.ppm')

    #winner_take_all
    print 'winner_take_all'
    for i in ncolors:
        tmp = convert(winner_take_all(i, 0.1, orig))
        img.pix = tmp
        performance(i, orig, tmp)
        img.write_img('/Users/davidclevenger/PycharmProjects/Pattern-Recognition/wta' + str(i) + '.ppm')

    #mean_shift
    print 'mean_shift'
    for i in bw:
        tmp = convert(meanshift(i, orig))
        img.pix = tmp
        performance(i, orig, tmp)
        img.write_img('/Users/davidclevenger/PycharmProjects/Pattern-Recognition/ms' + str(i) + '.ppm')

    return 0

if __name__ == "__main__":
    sys.exit(main())