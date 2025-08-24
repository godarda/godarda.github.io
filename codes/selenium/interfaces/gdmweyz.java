// ----------------------------------------------------------------------------------------------------
// Title          : Selenium Java to get domain name, URL, and page title using JavascriptExecutor
// File Name      : gdmweyz.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

class GD
{
    public static void main(String[] args) 
    {   
        System.setProperty("webdriver.chrome.driver", "/home/godarda/drivers/chromedriver");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://godarda.github.io/testapp/");
        
        JavascriptExecutor jse = (JavascriptExecutor)driver;
        String domain = jse.executeScript("return document.domain;").toString();
        System.out.println("Domain Name - "+domain);
        
        String url = jse.executeScript("return document.URL;").toString();
        System.out.println("URL - "+url);
        
        String title = jse.executeScript("return document.title;").toString();
        System.out.println("Page Title - "+title);
        
        //driver.close();
    }
}
