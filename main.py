
"""zeilen = [[4],
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
"""

zeilen =[[15],
         [10, 2],
         [1, 7, 1],
         [1, 1, 1],
         [1],
         [1, 3, 1],
         [1, 5, 2],
         [2, 6, 3],
         [3, 5, 3],
         [4, 3],
         [6, 1, 3, 2],
         [6, 1, 5],
         [5, 4],
         [15],
         [15]
         ]

spalten = [[15],
           [2, 8],
           [3, 7],
           [3, 6],
           [3, 2, 5],
           [3, 3, 2, 2],
           [3, 3, 2],
           [3, 4, 2, 2],
           [3, 4, 2],
           [2, 3, 2, 2],
           [1, 2, 2],
           [1, 6],
           [1, 1, 3, 4],
           [2, 9],
           [4, 4, 1, 3]]

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


def grosseZahlen(orientation, height):
    if orientation == "zeilen":
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
                for j in range(len(spalten) - length[anzahl-1] + length_before, length[i]):

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
                for j in range(len(zeilen) - length[anzahl - 1] + length_before, length[i]):
                    pic_matrix[j][height] = "[]"


def zahlenVomRand (orientation, height):
    if orientation == "zeilen":
        abstand_vorne = 0
        abstand_hinten = 0
        for i in range(0, len(spalten)):
            abstand_vorne += 1
            if pic_matrix[height][i] == "[]":
                abstand_vorne -= 1
                break
        for i in range(0, len(spalten)):
            abstand_hinten += 1
            if pic_matrix[height][len(spalten) - i - 1] == "[]":
                abstand_hinten -= 1
                break

        if zeilen[height][0] > abstand_vorne + 1:
            for i in range(abstand_vorne, zeilen[height][0] - 1):
                pic_matrix[height][i] = "[]"

        if zeilen[height][0] > abstand_hinten + 1:
            for i in range(len(spalten) - zeilen[height][-1], len(spalten) - abstand_hinten ):
                pic_matrix[height][i] = "[]"

    if orientation == "spalten":
        abstand_vorne = 0
        abstand_hinten = 0
        for i in range(0, len(zeilen)):
            abstand_vorne += 1
            if pic_matrix[i][height] == "[]":
                abstand_vorne -= 1
                break
        for i in range(0, len(zeilen)):
            abstand_hinten += 1
            if pic_matrix[len(spalten) - i - 1][height] == "[]":
                abstand_hinten -= 1
                break

        if spalten[height][0] > abstand_vorne + 1:
            for i in range(abstand_vorne, spalten[height][0] - 1):
                pic_matrix[i][height] = "[]"

        if spalten[height][0] > abstand_hinten + 1:
            for i in range(len(spalten) - spalten[height][-1], len(spalten) - abstand_hinten ):
                pic_matrix[i][height] = "[]"


#def punkteSetzen (orientation, height):
    #if orientation == "zeilen":

def main():
    prepare()

    for i in range(0,len(zeilen),1):
        grosseZahlen("zeilen", i)
    for i in range(0,len(zeilen),1):
        grosseZahlen("spalten", i)
    for i in range(0, len(zeilen),1):
        zahlenVomRand("zeilen", i)
    for i in range(0, len(zeilen), 1):
        zahlenVomRand("spalten", i)
    printThePicture()


main()
