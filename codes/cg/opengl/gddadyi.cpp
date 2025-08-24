// ----------------------------------------------------------------------------------------------------
// Title          : C++ program for Bresenham's circle drawing algorithm using OpenGL
// File Name      : gddadyi.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <GL/glut.h>
#include <iostream>
#include <cmath>
using namespace std;

static int xc = 200, yc = 200, r;

void Bresenham()
{
    float d;
    int x = 0, y = r;
    d = (3 - 2) * r;
    do
    {
        glBegin(GL_POINTS);
        glVertex2i(yc + x, xc + y);
        glVertex2i(xc + y, yc + x);
        glVertex2i(xc + y, yc - x);
        glVertex2i(yc + x, xc - y);
        glVertex2i(yc - x, xc - y);
        glVertex2i(xc - y, yc - x);
        glVertex2i(xc - y, yc + x);
        glVertex2i(yc - x, xc + y);
        glEnd();
        if (d <= 0)
        {
            d = d + (4 * x) + 6;
        }
        else
        {
            d = d + 4 * (x - y) + 10;
            y = y - 1;
        }
        x = x + 1;
    } while (x < y);
    glFlush();
}

int main(int agrc, char **argv)
{
    cout << "Enter the radius of circle ";
    cin >> r;
    glutInit(&agrc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH);
    glutInitWindowSize(640, 480);
    glutCreateWindow("Bresenham's Circle Algorithm");
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(0, 640, 480, 0);
    glutDisplayFunc(Bresenham);
    glutMainLoop();
}
