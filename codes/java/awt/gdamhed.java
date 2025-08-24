// ----------------------------------------------------------------------------------------------------
// Title          : Java program to draw a Circle using Graphics2D class
// File Name      : gdamhed.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;
class GD extends Frame 
{
    Shape circle=new Ellipse2D.Float(100.0f,100.0f,100.0f,100.0f);
    public void paint(Graphics g) 
    {
        Graphics2D ga=(Graphics2D)g;
        ga.draw(circle);
        ga.setPaint(Color.blue);
        ga.fill(circle);
    }
    public static void main(String args[]) 
    {
        Frame frame=new GD();
        frame.addWindowListener(new WindowAdapter()
        {
            public void windowClosing(WindowEvent we)
            {
                System.exit(0);
            }
        });
        frame.setSize(300,300);
        frame.setVisible(true);
    }
}
