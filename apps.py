class Car:
    def __init__(self,lisence_plate):
        self.lisence_plate=lisence_plate
    def park(self,Parking_lot,spot_no)->str:
        counter=0
        total_size=Parking_lot.total_size
        for i in range(Parking_lot.row):
            for j in range(Parking_lot.column):
                if counter is spot_no:                   
                    if Parking_lot.array[i][j]=='P':
                        return "Car was not parked successfully"
                    else:
                        Parking_lot.array[i][j]                        
                        return "Car was successfuly Parked("+self.lisence_plate+")"+"Spot #"+str(spot_no)
            counter=counter+1
        return "Parking lot is full"
    def __str__()->str:
        return self.lisence_plate
    
        
        

            



class Parking_lot:
    PARKING_SPOT_ROW=8
    PARKING_SPOT_COLUMN=8
    def __init__(self,parking_lot_row,parking_lot_column):
        self.row=parking_lot_row
        self.column=parking_lot_column
        self.array=[["NP"] * parking_lot_row] * parking_lot_column
        self.total_size=parking_lot_row*parking_lot_column
        self.Total_cars=self.total_size//(self.PARKING_SPOT_ROW*self.PARKING_SPOT_COLUMN)
    
def main():
    list = []
    parking_lot_row=10
    parking_lot_column=20
    x=Parking_lot(parking_lot_row,parking_lot_column)
    list.append(Car('OR 02 AX 4567'))
    list.append(Car('OR 02 AX 8567'))
    x=list[0].park(x,3)
    if x=="Parking lot is full":
        exit
    del x
    if len(list) == 0:
        exit


if __name__ == "__main__":
    main()



