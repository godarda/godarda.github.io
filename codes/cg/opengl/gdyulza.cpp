// ----------------------------------------------------------------------------------------------------
// Title          : C++ program for DDA line drawing algorithm using OpenGL
// File Name      : gdyulza.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <GL/glut.h>
#include <iostream>
using namespace std;

static float x1, y1, x2, y2;

void DDA()
{
    float x, y, k, xinc, yinc, step, dx, dy;
    dx = x2 - x1;
    dy = y2 - y1;
    if (dx > dy)
    {
        step = dx;
    }
    else
    {
        step = dy;
    }
    xinc = dx / step;
    yinc = dy / step;
    x = x1;
    y = y1;
    glBegin(GL_POINTS);
        glVertex2i(x, y);
    glEnd();
    for (int k = 0; k < step; k++)
    {
        x = x + xinc;
        y = y + yinc;
        glBegin(GL_POINTS);
            glVertex2i(x, y);
        glEnd();
    }
    glFlush();
}

int main(int agrc, char **argv)
{
    cout << "Enter the x1 coordinate ";
    cin >> x1;
    cout << "Enter the y1 coordinate ";
    cin >> y1;
    cout << "Enter the x2 coordinate ";
    cin >> x2;
    cout << "Enter the y2 coordinate ";
    cin >> y2;
    glutInit(&agrc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH);
    glutInitWindowSize(640, 480);
    glutCreateWindow("DDA Line Algorithm");
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(0, 640, 480, 0);
    glutDisplayFunc(DDA);
    glutMainLoop();
}
