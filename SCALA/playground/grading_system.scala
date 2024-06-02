import scala.io.StdIn.readLine

object Main {
    def main(args: Array[String]): Unit = {
        var mark = 0
        var correct_input = false
        var x = ""
        while (!correct_input) {
        val x = readLine("Please write your mark: ")
        try {
            mark = x.toInt
            if (mark >= 0 && mark <= 100) {
            correct_input = true
            } else {
            println("Wrong input value! Please enter a value from 0 to 100.")
            }
        } catch {
            case _: NumberFormatException => 
            println("Invalid input. Please enter a numeric value.")
        }
        }

        if (mark > 90) {
            println("Your grade is A")
        } else if (mark > 70) {
            println("Your grade is B")
        } else if (mark > 60) {
            println("Your grade is C")
        } else if (mark > 50) {
            println("Your grade is D")
        } else {
            println("Your grade is F")
        }
    }
}
