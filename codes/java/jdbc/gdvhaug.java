// ----------------------------------------------------------------------------------------------------
// Title          : Java MongoDB to create database and collection
// File Name      : gdvhaug.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.List;
import java.util.Set;

import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.MongoClient;
import com.mongodb.client.MongoDatabase;

class GD
{
    @SuppressWarnings("deprecation")
    public static void main(String[] args)
    {
        try
        {
            MongoClient mc = new MongoClient("localhost", 27017);
            System.out.println("Connection Established Successfully");
            
            List<String> dbs = mc.getDatabaseNames();
            System.out.println("Databases "+dbs);
            
            DB db = mc.getDB(dbs.get(0));
            Set<String> collections = db.getCollectionNames();
            System.out.println("Collections "+collections);
            
            MongoDatabase md = mc.getDatabase("DB");
            md.createCollection("holders");
            System.out.println("\nCollection Created");

            db = mc.getDB("DB");
            DBCollection collection = db.getCollection("holders");
            System.out.println(collection.toString());

            mc.close();
            System.out.println("Connection Released Successfully");
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
