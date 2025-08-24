// ----------------------------------------------------------------------------------------------------
// Title          : Java program to draw a Curve using Graphics2D class
// File Name      : gdpgzzw.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;
class GD extends Frame
{
    Stroke s=new BasicStroke(5);
    QuadCurve2D curve=new QuadCurve2D.Double(320,50,200,500,50,50);
    public void paint(Graphics g) 
    {
        Graphics2D ga=(Graphics2D)g;
        ga.setStroke(s);
        ga.setPaint(Color.blue);
        ga.draw(curve);
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
        frame.setSize(400,300);
        frame.setVisible(true);
    }
}
