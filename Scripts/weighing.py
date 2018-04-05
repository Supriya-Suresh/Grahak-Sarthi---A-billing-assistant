import serial
def weighing_machine_output():
    list_price = []
    #################################
    ser = serial.Serial('COM16', 9600)
    # ser.timeout = 2 # try ser.timeout = 2
    # print("Starting.... ")
    numOfLines = 0

    # while 1:
    #    if (ser.inWaiting()>0):
    ext_weight = str(ser.readline(), 'utf-8')[5:-2]
    return ext_weight
    #print("Weight obtained: %s Kg\n" % ext_weight)
    numOfLines = numOfLines + 1
    if numOfLines == 1:
        ser.close()
    
#weighing_machine_output()