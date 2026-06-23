import numpy as np
up_right= np.full((6, 6), 1)
up_right[3:5,3:5] = 3
up_right[:,1] = 2
up_right[1,:] = 2
up_left = np.fliplr(up_right)
down_right = np.flipud(up_right)
down_left = np.fliplr(down_right)
up=np.hstack((up_right,[[2],[2],[2],[2],[2],[2]], up_left))
down=np.hstack((down_right,[[2],[2],[2],[2],[2],[2]], down_left))
mat= np.vstack((up,[2,2,2,2,2,2,2,2,2,2,2,2,2],down))
print(mat)