// ----------------------------------------------------------------------------------------------------
// Title          : Selenium Java Page Object Model Example 1
// File Name      : gdvadve.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

package pageObjects;

import org.openqa.selenium.*;

public class HomePage
{
    static String actualTitle, expectedTitle;
    static WebElement logout = null;
    
    public static String title(WebDriver driver)
    {
        actualTitle = driver.getTitle();
        expectedTitle = "Welcome: Mercury Tours";
        if(actualTitle.equalsIgnoreCase(expectedTitle))
        {
            System.out.println("Page Title Matched");
        }
        else
        {
            System.out.println("Page Title Not Matched");
        }
        return actualTitle;
    }
}
