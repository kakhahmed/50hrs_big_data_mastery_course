import scala.io.StdIn.readLine
import scala.util.Random

object Main {
    def main(args: Array[String]): Unit = {
        println("Welcome in Fortune$");
        val random = new Random();
        val fortune = random.nextInt(101);
        var tries = 0;
        var done = false;
        val max_tries = 5;
        var x = readLine("You have " + max_tries + " tries. Please pick a number between 0-100: ");
        var input = 0

        while (!done) {
            try {
                input = x.toInt

                if (input == fortune) {
                    println("Ding Ding Ding!!! Winner! you got the correct number `" + fortune + "` after " + tries + " tries.")
                    done = true
                }
                else if (input > fortune) {
                    println("Your guess is greater than the correct number.")
                }
                else {
                    println("Your guess is less than the correct number.")
                }
                tries += 1
            } catch {
                case _: NumberFormatException =>
                printf("Integer numbers are expected. Try again.\n");
            }
            if (tries == 5) {
                done = true;
                println("You finished your " + max_tries + " maximum number of tries.")
                println("The correct number was "+ fortune + " .")
            }
            else {
                x = readLine("You have " + (max_tries - tries) + " tries lefty. Please pick a number between 0-100: ");
            }

        }
  
    }
}
