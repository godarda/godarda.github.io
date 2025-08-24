// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of Java method chaining
// File Name      : gdklzdp.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class holders
{
    long haccno;
    String hname,hcity;
    public holders account_no(long haccno)
    {
        this.haccno=haccno;
        return this;
    }
    public holders name(String hname)
    {
        this.hname=hname;
        return this;
    }
    public holders city(String hcity)
    {
        this.hcity=hcity;
        return this;
    }
    public void showrecords()
    {
        System.out.println(haccno+" | "+hname+" | "+hcity);
    }
}
class GD
{
    public static void main(String[] args) 
    {
        holders insert=new holders();
        insert.account_no(25622348989L).name("James Moore").city("Phoenix").showrecords();
        insert.account_no(25622348992L).name("Ryan Bakshi").city("Mumbai").showrecords();
    }
}
