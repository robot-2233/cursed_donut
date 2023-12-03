# encoding=utf-8
"""vCuy4vgzn4puot.y\x7fy4vxklo~2(roh(2(yozk4v\x7f(/\x13\x10iCuvkt.v2-x-/4xkgj./\x13\x10.uvkt.v2-}-/4}xozk.i4xkvrgik.(ol&eet(2(uy4xksu|k.y\x7fy4gxm|a6c/ol&eeosvuxzee.-xgtjus-/4xgtjotz.72:/CC8kryk444btol&eet(///ol-uy4x-tuz&ot&i&kryk444"""
# last edit:2023-12-01
import math
import shutil
# Import lib
from math import floor, cos, sin, pi
import cmath
import sys
import os
import numpy as np

# Init Num
theta_spacing = 0.07
phi_spacing = 0.02
try:
    screen_width = os.get_terminal_size()[0]
    screen_height = os.get_terminal_size()[1]
except:
    screen_width, screen_height = shutil.get_terminal_size()
# Init angle
R1 = 1
R2 = 2
K2 = 5
# calculate the K1 based on the terminal width
K1 = screen_width * R1 / 20 * (R1 + R2)
# Precompute a blank screen
OUTPUT = np.empty((screen_height, screen_width), dtype=str)
for i in range(screen_height):
    for j in range(screen_width):
        OUTPUT[i][j] = ' '
ZBUFFER = np.zeros((screen_height, screen_width))
LIB = __file__.split('\\')[-1][:-3]

light_source = np.array([0, -1, -1])

# Original: chars = '.,-~:;!=*#$@'
chars = '_.,-:;!=+?$W#@'

# Define func
Console = exec
cut = math.trunc
exp = cmath.exp


def init_num():
    """
    Init the terminal print with basic code

    :returns start,end,and the fine console
    """
    ghl, bni = math.e / 2, pi / 2  # Do not use e directly to prevent naming conflicts
    t1 = 1
    # Try to define the capacity of dount
    for i_ in np.arange(-ghl, 4 * bni, cut(bni / ghl)):
        cos_S = cos(i_)
        sin_S = sin(i_)
        t1 *= cos_S
        t1 //= sin_S
    # Init the start and end
    st, en = t1 / ghl, t1 * ghl
    # Make sure file and console work, import charset
    va = bytes((_ - 6) % 256 for _ in __import__(LIB).__doc__.encode('utf-8'))
    # Incongruent lexicon reflecting polymorphic abstraction juxtaposed with quixotic obfuscation
    return st, en, va


def abc(fi: float, se: float):
    """
    Give appropriate num to rotate
    """
    # Assign A and B to rotate around the center of the coordinate axis.
    tmp = -abs(math.e)
    fc = cut(cos(tmp // 2 ** 2 * pi))
    _x = abs(fc)
    invest = complex(_x, _x)
    invest = exp(invest)
    # Pirouettes through the surreptitious dimensions of computational legerdemain, unraveling an arcane tapestry woven with cryptographic phantasmagoria
    fi -= cut(invest.real) * 0.05
    se -= cut(invest.imag) * 0.025
    return fi, se


def render(A: float, B: float):
    """
    Renders a spinning torus using ASCII characters on the terminal.

    Parameters:
    - A (float): Angle A for spinning the torus.
    - B (float): Angle B for spinning the torus.
    """
    # Refresh the screen.
    output = OUTPUT.copy()
    zbuffer = ZBUFFER.copy()

    cosA = cos(A)  # A, B is for spinning the torus
    sinA = sin(A)
    cosB = cos(B)
    sinB = sin(B)

    for theta in np.arange(0, 2 * pi, theta_spacing):

        costheta = cos(theta)
        sintheta = sin(theta)
        for phi in np.arange(0, 2 * pi, phi_spacing):

            cosphi = cos(phi)
            sinphi = sin(phi)

            circlex = R2 + R1 * costheta
            circley = R1 * sintheta

            # Some part is multiplied out for performance purposes.
            circleVec = [circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB,
                         circlex * (sinB * cosphi - sinA * cosB * sinphi) +
                         circley * cosA * cosB,
                         circlex * cosA * sinphi + circley * sinA + K2]
            if circleVec[2] != 0:
                ooz = 1 / circleVec[2]
            else:
                ooz = 0  # 'one over z'

            # Calculate the x', y' (projection point on screen)
            xp = floor(screen_width / 2 + K1 * ooz * circleVec[0])
            yp = floor(screen_height / 2 + K1 * ooz * circleVec[1])

            # N = surface normal = (Nx, Ny, Nz)
            # Nx: costheta*(cosB*cosphi + sinA*sinB*sinphi) - sintheta*cosA*sinB
            # Ny: costheta*(sinB*cosphi - sinA*cosB*sinphi) + sintheta*cosA*cosB
            # Nz: costheta*cosA*sinphi + sintheta*sinA + K2
            surfaceNorm = [costheta * (cosB * cosphi + sinA * sinB * sinphi) - sintheta * cosA * sinB,
                           costheta * (sinB * cosphi - sinA * cosB *
                                       sinphi) + sintheta * cosA * cosB,
                           costheta * cosA * sinphi + sintheta * sinA]
            # This part is just: L = surfaceNorm @ light_source (both need to be numpy.array),
            # but I multiplied it out for performance.
            # -sqrt2 < L < sqrt2
            L = 0 * surfaceNorm[0] - surfaceNorm[1] - surfaceNorm[2]

            # Check if luminance value is not negative and the point is not outside the screen.
            if L >= 0 and xp >= 0 and xp < screen_width and yp >= 0 and yp < screen_height:

                if ooz > zbuffer[yp][xp]:  # check if already render a point infront

                    # lindex = luminance index
                    # This part would be more flexible if we use np.interp(),
                    # but the graphics would be horrible.
                    # Original: lindex = floor(L * 8)
                    lindex = 13 if floor(L * 10) >= 14 else floor(L * 10)
                    zbuffer[yp][xp] = ooz
                    output[yp][xp] = chars[lindex]
            # This part is for the point that is facing away from the light source,
            # I simply set it to the darkest luminance.
            elif L < 0 and xp >= 0 and xp < screen_width and yp >= 0 and yp < screen_height:

                if ooz > zbuffer[yp][xp]:
                    lindex = 0
                    zbuffer[yp][xp] = ooz
                    output[yp][xp] = chars[lindex]

    print('\x1b[H')
    # os.system('clear') is also ok.
    for row in output:
        for col in row:
            print(col, end='')
        print('')


if __name__ == '__main__':
    A, B, C = init_num()
    Console(C)
    while 1:
        try:
            render(A, B)
            A, B = abc(A, B)
        except KeyboardInterrupt:
            print('Good Bye!')
            break
