
import scala.io.StdIn.readLine

object Main {
    def main(args: Array[String]): Unit = {
        val age = readLine("Please write your age: ");
        val height = readLine("Please write your height in ft: ");
        if ((age.toInt > 13) && (height.toInt >= 5)) {
            println("Welcome to PayLand");
            var special_card = readLine("Are you interested in the special card? (Y/N): ")
            if (special_card == "Y"){
                println("Great! Welcome to PayLand with special card granted :)")
            }
            else {
                println("Welcome to PayLand!");
            }
        }
        else {
            println("Unfortunately, entrance is not allowed for age under 13 or height under 5ft:(");
        }
    }
}