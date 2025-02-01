package hellocucumber;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class StepDefinitions {
    
    @Given("an example scenario")
    public void anExampleScenario() {
        System.setProperty("webdriver.chrome.driver","D:\\VS_Space\\Driver\\chromedriver.exe");
        WebDriver driver= new ChromeDriver();
        driver.get("https://adapayuat.bankfab.com/PGRPTG/index.jsp");
        driver.manage().window().maximize();
    }


    @When("all step definitions are implemented")
    public void allStepDefinitionsAreImplemented() {
    }

    @Then("the scenario passes")
    public void theScenarioPasses() {
    }

}
