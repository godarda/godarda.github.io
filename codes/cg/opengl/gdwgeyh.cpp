// ----------------------------------------------------------------------------------------------------
// Title          : C++ program for DDA circle drawing algorithm using OpenGL
// File Name      : gdwgeyh.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <GL/glut.h>
#include <iostream>
#include <cmath>
using namespace std;

static int r;

void DDA()
{
    float x, y, x1, y1, x2, y2, k, val, i = 0;
    x1 = r * cos(0);
    y1 = r * sin(0);
    x = x1;
    y = y1;
    do
    {
        val = pow(2, i);
        i++;
    } while (val < r);
    k = 1 / pow(2, i - 1);
    do
    {
        x2 = x1 + y1 * k;
        y2 = y1 - k * x2;
        glBegin(GL_POINTS);
            glVertex2i(200 + x2, 200 + y2);
        glEnd();
        x1 = x2;
        y1 = y2;
    } while ((y1 - y) < k || (x - x1) > k);
    glFlush();
}

int main(int agrc, char **argv)
{
    cout << "Enter the radius of circle ";
    cin >> r;
    glutInit(&agrc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH);
    glutInitWindowSize(640, 480);
    glutCreateWindow("DDA Circle Algorithm");
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(0, 640, 480, 0);
    glutDisplayFunc(DDA);
    glutMainLoop();
}
