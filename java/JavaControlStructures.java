import java.util.Scanner;

public class JavaControlStructures {
    
    public static void main(String[] args) {
        
        // User Input

        System.out.println("Enter the temperature in Fahrenheit : ");

        Scanner tempInput = new Scanner(System.in);

        int temperature = tempInput.nextInt();

        System.out.println("The input temperature is : " + temperature);
        
        // Base If-Else Statement:-

        // if (temperature >= 84) {
        //     System.out.println("It's a hot day! Remember to stay hydrated.");
        // }

        // else {
        //     System.out.println("A t-shirt and shorts may not be the best option today.");
        // }
        // System.out.println("Have a nice day!!!!");
        
        // If-Else Statement with Turnary code
        // Turnary code is a short hand for If-Else Statement that can be used when the operation can be consicely expressed
        // (i.e.using ? and : to use If-Else Statement. Value before : is executed when true, otherwise value after : is executed)
        String result = (temperature >= 84) ? "hot" : "not so hot" ;

        // Because of the turnary statement, the variable 'result' will either be 'hot' if temperature >= 84 or 'not so hot' if it is not
        System.out.println("The weather today is " + result);

        Scanner nameInput = new Scanner(System.in);

        System.out.println("Enter a name : ");
        
        String name = nameInput.next();
        
        System.out.println("The name entered is : " + name);

    }

}