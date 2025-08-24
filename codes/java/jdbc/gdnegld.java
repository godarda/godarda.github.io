// ----------------------------------------------------------------------------------------------------
// Title          : Java MongoDB to insert the JSON file documents into a collection
// File Name      : gdnegld.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.io.BufferedReader;
import java.io.FileReader;

import org.bson.Document;
import com.mongodb.MongoClient;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;

class GD
{
    @SuppressWarnings("resource")
    public static void main(String[] args)
    {
        try
        {
            MongoClient mc = new MongoClient("localhost", 27017);
            MongoDatabase md = mc.getDatabase("DB");
            MongoCollection<Document> collection = md.getCollection("holders");
            
            BufferedReader br = new BufferedReader(new FileReader("gd.json"));
            String docs=null;
            while((docs=br.readLine())!=null)
            {
                collection.insertOne(Document.parse(docs));
            }
            System.out.println("Documents inserted successfully");
            
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
