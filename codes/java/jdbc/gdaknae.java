// ----------------------------------------------------------------------------------------------------
// Title          : Java MongoDB to insert and retrieve the documents from a collection
// File Name      : gdaknae.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.ArrayList;
import org.bson.Document;
import com.mongodb.MongoClient;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;

class GD
{
    public static void main(String[] args)
    {
        try
        {
            MongoClient mc = new MongoClient("localhost", 27017);
            MongoDatabase md = mc.getDatabase("DB");
            MongoCollection<Document> collection = md.getCollection("holders");
            
            String document1,document2,document3,document4;
            document1="{ 'account_no' : 2562348989, 'name' : 'James Moore', 'city' : 'Phoenix', 'DOB' : ISODate('1985-05-26T00:00:00Z'), 'bank' : 'Barclays', 'amount' : 5000, 'loan' : [ { 'Personal' : 5660, 'Home' : 15000 } ] }";
            document2="{ 'account_no' : 2562348990, 'name' : 'Donald Taylor', 'city' : 'Irvine', 'DOB' : ISODate('1990-08-20T00:00:00Z'), 'bank' : 'Citi', 'amount' : 7000, 'loan' : [ { 'Home' : 10000, 'Car' : 20000 } ] }";
            document3="{ 'account_no' : 2562348991, 'name' : 'Edward Parkar', 'city' : 'Irvine', 'DOB' : ISODate('1994-01-29T00:00:00Z'), 'bank' : 'ICICI', 'amount' : 95000, 'loan' : [ { 'Personal' : 25000, 'Home' : 450000, 'Car' : 10000 } ] }";   
            document4="{ 'account_no' : 2562348992, 'name' : 'Ryan Bakshi', 'city' : 'Mumbai', 'DOB' : ISODate('1982-01-14T00:00:00Z'), 'bank' : 'Citi', 'amount' : 50000, 'loan' : [ { 'Personal' : null, 'Home' : null, 'Car' : null } ] }";
            
            Document d1,d2,d3,d4;
            d1=Document.parse(document1);
            d2=Document.parse(document2);
            d3=Document.parse(document3);
            d4=Document.parse(document4);
            
            collection.insertOne(d1);
            System.out.println("A document inserted successfully");
            
            ArrayList<Document> docs=new ArrayList<Document>();
            docs.add(d2);
            docs.add(d3);
            docs.add(d4);
            collection.insertMany(docs);
            System.out.println("Multiple documents inserted successfully");
            
            FindIterable<Document> fi=collection.find();
            MongoCursor<Document> cursor=fi.iterator();
            while(cursor.hasNext()) 
            {
                System.out.println(cursor.next());
            }
            mc.close();
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
