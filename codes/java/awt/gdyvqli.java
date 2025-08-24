// ----------------------------------------------------------------------------------------------------
// Title          : Java program to draw a Line using Graphics2D class
// File Name      : gdyvqli.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;
class GD extends Frame
{
    Line2D line=new Line2D.Double(0,0,200,200);
    public void paint(Graphics g) 
    {
        Graphics2D ga=(Graphics2D)g;
        ga.setPaint(Color.blue);
        ga.draw(line);
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
