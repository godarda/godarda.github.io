// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of C# method overriding
// File Name      : gdrswzv.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Tickets t = new Tickets();
double fair = t.Fair(400, 1.5);
Console.WriteLine("Approximate Fair " + fair);

t = new TrainTicket();
fair = t.Fair(400, 1.2);
Console.WriteLine("Train Ticket {0}", fair);

t = new BusTicket();
fair = t.Fair(400, 1.5);
Console.WriteLine("Bus Ticket {0}", fair);

class Tickets
{
    public virtual double Fair(double distance, double rate)
    {
        return distance * rate;
    }
}
class TrainTicket : Tickets
{
    public override double Fair(double distance, double rate)
    {
        return distance * rate + 30;
    }
}
class BusTicket : Tickets
{
    public override double Fair(double distance, double rate)
    {
        return distance * rate + 60;
    }
}
