
zeilen = [[4],
          [3, 1],
          [7],
          [8],
          [3, 7],
          [3, 6, 2],
          [2, 6, 2],
          [1, 3, 2, 2],
          [1, 3, 2, 1],
          [2, 2, 4, 1],
          [1, 2, 3, 1, 1],
          [1, 9, 1],
          [1, 3, 4, 1],
          [5, 1],
          [6, 1],
          [6, 4, 1],
          [5, 3, 2, 1],
          [1, 3, 7, 2],
          [4, 4],
          [12]]

spalten = [[3],
           [1, 2],
           [5, 5],
           [4, 7],
           [2, 6, 1],
           [1, 7, 1],
           [2, 8, 1],
           [1, 3, 1, 3, 1],
           [2, 3, 2, 1, 1, 1],
           [1, 3, 3, 3, 1],
           [5, 5, 1, 1, 1],
           [8, 2, 1, 1, 1],
           [7, 4, 3],
           [7, 2, 2],
           [6, 1],
           [1, 3, 2],
           [3, 2, 1],
           [2, 1],
           [2, 2],
           [11]]

pic_matrix = []


def prepare():
    for i in range(0,len(zeilen),1):
        pic_matrix.append([])
        for j in range (0, len(spalten), 1):
            pic_matrix[i].append("  ")


def printThePicture():
    print("|         ||        ||        ||         |")
    for i in range(0,len(zeilen),1):
        zeile = "|"
        for j in range(0, len(spalten), 1):
            zeile += str(pic_matrix[i][j])
        zeile+= "|"
        print (zeile)
    print("|         ||        ||        ||         |")

def grosseZahlen(orientierung, height):
    if orientierung == "zeile":
        anzahl = len(zeilen[height])
        length = [0] * anzahl
        for i in range(0, anzahl, 1):
            length[0] = zeilen[height][0]
            if i > 0:
                length[i] = length[i - 1] + 1 + zeilen[height][i]
        rest = len(spalten) - length[anzahl - 1]
        for i in range(0, anzahl, 1):
            if zeilen[height][i] > rest:
                length_before = 0
                if(i>0):
                    length_before = length[i - 1] + 1
                print(range(len(spalten) - length[anzahl-1] + length_before, length[i]))
                for j in range(len(spalten) - length[anzahl-1] + length_before, length[i]):
                    print("iterate")
                    pic_matrix[height][j] = "[]"
    else:
        anzahl = len(spalten[height])
        length = [0] * anzahl
        for i in range(0, anzahl, 1):
            length[0] = spalten[height][0]
            if i > 0:
                length[i] = length[i - 1] + 1 + spalten[height][i]
        rest = len(zeilen) - length[anzahl - 1]
        for i in range(0, anzahl, 1):
            if spalten[height][i] > rest:
                length_before = 0
                if (i > 0):
                    length_before = length[i - 1] + 1
                print("spalte" + str(height) + ": ")
                print(len(zeilen))
                print(length[anzahl - 1])
                print(length[-1])
                print(range(len(zeilen) - length[anzahl - 1] + length_before, length[i]))
                for j in range(len(zeilen) - length[anzahl - 1] + length_before, length[i]):
                    print("iterate")
                    pic_matrix[j][height] = "[]"

def main():
    prepare()

    for i in range(0,len(zeilen),1):
        grosseZahlen("zeile", i)
    for i in range(0,len(zeilen),1):
        grosseZahlen("spalten", i)
    #for i in range(0, len(zeilen),1):

    printThePicture()


main()
