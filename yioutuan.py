def Anti_shake(index, coord):
    global tmp_coord
    MPT = 3.14159265358979323846
    MINCUTOFF = 0.01
    BETA = 0.01
    FREQUENCY = 30
    if index == 0:
        tmp_coord = coord
    else:
        tmp2_coord = []
        for indx in range(3660):
            dcutoff_x,dcutoff_y = MINCUTOFF + BETA*abs(coord[indx][0] - tmp_coord[indx][0]),\
                                  MINCUTOFF + BETA*abs(coord[indx][1] - tmp_coord[indx][1])
            tao_x,tao_y = 1./(2*MPT*dcutoff_x), 1./(2*MPT*dcutoff_y)
            alpha_x,alpha_y = 1./(1+tao_x*FREQUENCY), 1./(1+tao_y*FREQUENCY)
            new_coord_x,new_coord_y = alpha_x*coord[indx][0]+(1-alpha_x)*tmp_coord[indx][0],\
                                      alpha_y*coord[indx][1]+(1-alpha_y)*tmp_coord[indx][1]
            tmp2_coord.append([new_coord_x, new_coord_y])
        tmp_coord = tmp2_coord
    return tmp_coord
