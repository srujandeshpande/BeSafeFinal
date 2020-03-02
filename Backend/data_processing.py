
def analysis(leg):
    coords = leg[:]
    #declaring the initial variables
    pointer = 1
    tolerance = 0.00005
    
    for array_decoded in coords:
        lat_ref = array_decoded[0][0]
        lng_ref = array_decoded[0][1]
        while pointer < len(array_decoded)-1:
            if abs(lat_ref - array_decoded[pointer+1][0]) < tolerance or abs(lng_ref - array_decoded[pointer+1][1]) < tolerance:
                del array_decoded[pointer+1]   
            else:
                lat_ref = array_decoded[pointer+1][0]
                lng_ref = array_decoded[pointer+1][1]
                pointer += 1
        
    return coords






