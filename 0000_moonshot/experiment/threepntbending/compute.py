import numpy as np
import utiltools.robotmath as rm

print(np.cos(np.radians(60)))
np.cos(np.radians(60))

print(np.sin(np.radians(57.74)) * 5)

print(np.cos(np.radians(75)) * np.cos(np.radians(57.74)) * 5)

print(np.cos(np.radians(15)) * np.cos(np.radians(57.74)) * 5)

# np.array([np.array([667.92059736,  64.37366592, 895.14553677]), np.array([[ 0.22607525,  0.6422402 ,  0.73240529],
#        [ 0.89017891,  0.16910765, -0.42306514],
#        [-0.39556478,  0.7476163 , -0.53347762]])])
#
# np.array([np.array([673.42927191,  58.85781235, 901.01760294]), np.array([[ 0.22599072,  0.64215128,  0.73250934],
#        [ 0.89023098,  0.16915285, -0.42293748],
#        [-0.39549589,  0.74768245, -0.53343599]])])

print(np.array([673.4588375 ,  59.16344549, 901.9421124] - np.array([676.61560077,  63.38334466, 900.08285113])))

# 674.5713478 ,  73.03139775, 899.48212794
print(np.array([673.51977056,  60.41268906, 903.00827277] - np.array([673.79876902,  55.11551349, 907.5051894])))

before = rm.homobuild(np.array([673.19317469,  60.81176012, 902.08560022]), np.array([[0.15771317, 0.66228295, 0.73246696],
       [0.86765792, 0.26121558, -0.42300845],
       [-0.47148307, 0.70224476, -0.53343791]]))

after = rm.homobuild(np.array([673.00725898,  59.52574216, 902.74192666]), np.array([[ 0.14603211,  0.6622587 ,  0.73490682],
       [ 0.87430874,  0.26118909, -0.40910206],
       [-0.46288104,  0.70227749, -0.54087657]]))

offset_b2a = np.dot(after, np.linalg.inv(before))
print(offset_b2a)


