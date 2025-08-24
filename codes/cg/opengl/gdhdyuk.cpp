// ----------------------------------------------------------------------------------------------------
// Title          : C++ program for Bresenham's line drawing algorithm using OpenGL
// File Name      : gdhdyuk.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <GL/glut.h>
#include <iostream>
using namespace std;

static float x1, y1, x2, y2;

void Bresenham()
{
    float x, y, p, xinc, yinc, step, dx, dy;
    dx = abs(x2 - x1);
    dy = abs(y2 - y1);
    p = 2 * dy - dx;
    if (x1 > x2)
    {
        x = x2;
        y = y2;
        x2 = x1;
    }
    else
    {
        x = x1;
        y = y1;
    }
    glBegin(GL_POINTS);
        glVertex2i(x, y);
    glEnd();
    while (x < x2)
    {
        x++;
        if (p < 0)
        {
            p += 2 * dy;
        }
        else
        {
            y++;
            p = p + (2 * dy) - (2 * dx);
        }
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
    glutCreateWindow("Bresenham's Line Algorithm");
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(0, 640, 480, 0);
    glutDisplayFunc(Bresenham);
    glutMainLoop();
}
