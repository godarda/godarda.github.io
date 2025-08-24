// ----------------------------------------------------------------------------------------------------
// Title          : Java program to create an input field on a frame
// File Name      : gdqoivp.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import javax.swing.*;
import java.awt.FlowLayout;
class GD
{
    public static void main(String args[])
    {
        JPanel p=new JPanel();
        FlowLayout fl=new FlowLayout();
        p.setLayout(fl);
        JLabel l=new JLabel("Enter the name ");
        JTextField tf=new JTextField(10);
        p.add(l);
        p.add(tf);
        JFrame f=new JFrame("Frame");
        f.setContentPane(p);
        f.setSize(300,300);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
