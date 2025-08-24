// ----------------------------------------------------------------------------------------------------
// Title          : Selenium Java Page Object Model Example 2
// File Name      : gddyzek.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

package pageObjects;

import org.openqa.selenium.*;

public class HomePage
{
    WebDriver driver;
    public HomePage(WebDriver driver)
    {
        this.driver = driver;
    }

    public void title()
    {
        String actualTitle, expectedTitle;
        actualTitle = driver.getTitle();
        expectedTitle = "Welcome: Mercury Tours";
        if (actualTitle.equalsIgnoreCase(expectedTitle))
        {
            System.out.println("Page Title Matched");
        }
        else
        {
            System.out.println("Page Title Not Matched");
        }
    }
}
