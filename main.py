from models import kmeans, winner_take_all  #my class
from utility import Image, convert

if __name__ == "__main__":
    img = Image()
    img.read_img('/Users/davidclevenger/PycharmProjects/Pattern-Recognition/flowers.ppm')
    new = convert(winner_take_all(4,0.01,img.pix))#convert(kmeans(2,img.pix))

    img.pix = new
    img.write_img('/Users/davidclevenger/PycharmProjects/Pattern-Recognition/flowers-comp.ppm')


