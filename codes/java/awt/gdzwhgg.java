// ----------------------------------------------------------------------------------------------------
// Title          : Java program to create an empty frame as an instance
// File Name      : gdzwhgg.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import javax.swing.JFrame;
class GD
{
    public static void main(String args[])
    {
        JFrame frame=new JFrame("Frame");
        frame.setSize(300,300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
