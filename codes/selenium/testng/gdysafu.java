// ----------------------------------------------------------------------------------------------------
// Title          : How to generate Extent Reports in Selenium WebDriver
// File Name      : gdysafu.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.io.IOException;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.Status;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import com.aventstack.extentreports.reporter.configuration.Theme;

public class GD 
{
    WebDriver driver;
    
    @BeforeClass
    public void SetBrowser() 
    {
    	System.setProperty("webdriver.chrome.driver", "/home/godarda/drivers/chromedriver");
        driver = new ChromeDriver();
    }
    
    @Test
    public void VerifyTitle() throws IOException, InterruptedException 
    {
    	ExtentSparkReporter esr = new ExtentSparkReporter("/home/godarda/ExtentReport.html");
        ExtentReports er = new ExtentReports();
        er.attachReporter(esr);
        
        esr.config().setDocumentTitle("Extent Report");
        esr.config().setTheme(Theme.DARK);
        
        ExtentTest et = er.createTest("VerifyHomePageTitle");
        et.log(Status.INFO, "Chrome Browser Launched");
        
        driver.navigate().to("https://godarda.github.io/testapp/");
        et.log(Status.INFO,"Successfully Navigated to the URL");
        
        String actual = driver.getTitle();
        String expected = "GoDarda's TestApp";
        
        et.log(Status.INFO, "Actual Title: " +actual);
        et.log(Status.INFO, "Expected Title: "+expected);
        if(actual.equals(expected))
        {
            et.log(Status.PASS, "Test Passed");
        }
        else
        {
            et.log(Status.FAIL, "Test Failed");
        }
        
        Assert.assertEquals(actual,expected);
        er.flush();
    }
    @AfterClass
    public void CloseDriver() 
    {
        driver.close();
    }
}
