import numpy as np
def rotate_image(image, angle_degrees):
    image = np.asarray(image)
    H,W = image.shape
    Cy = (H-1)/2
    Cx = (W-1)/2
    matrix = np.zeros((H,W))
    for i in range(H):
        for j in range(W):
            scr_y =int(round( Cy + (i - Cy)* np.cos(np.deg2rad(angle_degrees)) + (j - Cx)*np.sin(np.deg2rad(angle_degrees))))
            scr_x = int(round(Cx - (i - Cy)* np.sin(np.deg2rad(angle_degrees)) +(j- Cx)* np.cos(np.deg2rad(angle_degrees))))
            if scr_y > H or scr_x > W:
                matrix[i][j]=0
            else:
                matrix[i][j] = image[scr_y][scr_x]
    return matrix.tolist()
            
            