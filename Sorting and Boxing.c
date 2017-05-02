#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

int main() {

}

int boxAnalysis() {
    // Create variables
bool storage [4][13];
int translation [4] = {1, 2, 4, 8}, set [13], row = 0, column = 0,  
        satellite = 0, number = 0, year = 0, dayOfYear = 0, hour = 0, min = 0, 
        sec = 0, station = 0;

//Initialize set to be all 0
for (int i = 0; i < 14; i++)
    set[i] = 0;

//Initial storage to be all false
for (int i = 0; i < 4; i++)
	for (int j = 0; j < 13; j++)
		storage [i][j] = false;

// Populate array
do {
    //Prompt user for position
    printf("Please insert metadata (row column), enter -1 -1 to exit: ");
    scanf("%d %d", &row, &column);
    
    //Check bounds
    if (row < 5 && row >= 0 && column < 14 && column >= 0) 
            storage[row-1][column-1] = true;
        
    else
        printf("Out of bounds.\n");

    
} while (row != -1 && column!= -1);
 
// Analyze array
for (int k = 0; k < 13; k++){
    for (int l = 0; l < 4; l++) {
        if (storage[l][k] == true)
            set[k] += translation[l];
    }
    return 0;
}

satellite = set [0];
year = set[1];
dayOfYear = set[2]*100 + set[3]*10 + set[4];
hour = set [5]*10 + set[6];
min = set [7]*10 + set [8];
sec = set[9]*10 + set[10];
station = set[11]*10 + set[12];

printf("Alouette-%d 196%d DOY: %d Time: %d:%d:%d UTC Station %d", satellite, 
        year, dayOfYear, hour, min, sec, station);

}

int whatBoxAmIIn(int xGiven, int yGiven, bool storage[4][13]) {

    bool isIn;
    //Figure out
    int boxWidth = 352;
    int boxHeight = 87;
    int x[15], y[5];

    for(int i = 0; i < 15; i++)
        x[i] = boxWidth*i;

    for(int j = 0; j < 5; j++)
        y[j] = boxHeight*j;

    while (isIn == false) {
        int i = 0;
        int j = 0;
        bool xIn, yIn;

        if (xGiven >= x[i])
            i++;
        else
            xIn = true;
        if (yGiven > y[j])
            j++;
        else
            yIn = true;

        if (yIn == true && xIn == true) {
            isIn = true;
            storage[i][j] = 1;
        }
    }
    //Offset
    int offsetX = 301;
    int offsetY = 87;
    

    
    for(int i = 0; i < 15; i++)
        x[i] += offsetX;
    
    for(int j = 0; j < 5; j++)
        y[j] = offsetY;

    
    return 0;
}

    int determineBottom (int yOfTopLeft) {
        //yOfRandom can be 1, 2, 4, 8
        //Probabilistically determine, assume lowest is 
        //or Detect Number
        
    }
    
    //1962 first dots