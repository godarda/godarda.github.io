// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a rhombus using OpenGL
// File Name      : gddcivl.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <GL/glut.h>

int main(int agrc, char **argv)
{
    glutInit(&agrc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH);
    glutInitWindowSize(500, 500);
    glutCreateWindow("Rhombus");
    glBegin(GL_POLYGON);
        glColor3f(1, 1, 1);
        glVertex2f(0, 1);
        glVertex2f(1, 0);
        glVertex2f(0, -1);
        glVertex2f(-1, 0);
    glEnd();
    glFlush();
    glutMainLoop();
}
