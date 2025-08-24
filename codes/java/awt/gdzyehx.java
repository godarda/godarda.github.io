// ----------------------------------------------------------------------------------------------------
// Title          : Java program to draw a Rectangle using Graphics2D class
// File Name      : gdzyehx.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;
class GD extends Frame 
{
    Rectangle2D rectangle=new Rectangle2D.Double(50,50,120,80);
    public void paint(Graphics g) 
    {
        Graphics2D ga=(Graphics2D)g;
        ga.draw(rectangle);
        ga.setPaint(Color.blue);
        ga.fill(rectangle);
        ga.fill(rectangle);
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
