minDistance = _  # Distancia desde el robot (medido con el laser) hasta la placa al final del panel a la cual, si el robot se mueve más, se cae del panel

numOfCellsToScan = 9

lastMovement = False
while True:
    
    # Stepper movement
    moveToCell1()  # Moves camera to center of first cell to scan
    
    numOfCellsToScan = 3*numOfMovementsDC
    
    for i in range(1, numOfCellsToScan+1):
        scanCell()
        storeToDatabase()
        if i == numOfCellsToScan:  # Última celda
            break
        moveToNextCell(i)
        
    if atEdge:
        break  # Exit main loop
        
    # DC Movement
    atEdge = False
    numOfMovementsDC = 0
    while (not atEdge) and (numOfMovementsDC < 3):
        numOfMovementsDC += 1
        moveDCMotorsOneCell()
        
        distanceToEdge = tof.getDistance()
        if distanceToEdge < minDistance:
            atEdge = True
            break