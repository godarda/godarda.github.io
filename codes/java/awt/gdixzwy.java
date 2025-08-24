// ----------------------------------------------------------------------------------------------------
// Title          : Java program to print Hello World on a frame
// File Name      : gdixzwy.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import javax.swing.*;
class GD
{
    public static void main(String args[])
    {
        JPanel p=new JPanel();
        JLabel l1=new JLabel("Hello, World!");
        JLabel l2=new JLabel("Welcome to GoDarda!");
        p.add(l1);
        p.add(l2);
        JFrame f=new JFrame("Frame");
        f.setContentPane(p);
        f.setSize(300,300);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
