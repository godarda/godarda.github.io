// ----------------------------------------------------------------------------------------------------
// Title          : Selenium Java to get the browser details using Capabilities
// File Name      : gdspasn.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import org.openqa.selenium.Capabilities;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver; 
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.edge.EdgeOptions;

class GD
{
    static WebDriver driver;
    public static void NameVersionOS()
    {
        Capabilities c = ((RemoteWebDriver)driver).getCapabilities();
        System.out.println("Browser Name: "+c.getBrowserName());
        System.out.println("Browser Version: "+c.getBrowserVersion());
        System.out.println("Platform: "+c.getPlatformName());
        System.out.println("___________________________________________");
        driver.close();
    }
    
    public static void main(String[] args) 
    {   
        System.out.println("Operating System: "+System.getProperty("os.name"));
        System.out.println("OS Version: "+System.getProperty("os.version"));
        System.out.println("OS Architecture: "+System.getProperty("os.arch"));
        System.out.println("___________________________________________");
        
        ChromeOptions co = new ChromeOptions();
        FirefoxOptions fo = new FirefoxOptions();
        EdgeOptions eo = new EdgeOptions();
                
        System.setProperty("webdriver.chrome.driver", "/home/godarda/drivers/chromedriver");
        driver = new ChromeDriver(co);
        NameVersionOS();
        
        System.setProperty("webdriver.gecko.driver", "/home/godarda/drivers/geckodriver");
        driver = new FirefoxDriver(fo);
        NameVersionOS();
        
        System.setProperty("webdriver.edge.driver", "/home/godarda/drivers/msedgedriver");
        driver = new EdgeDriver(eo);
        NameVersionOS();
    }
}
