import scala.io.StdIn.readLine


object Main {
    def main(args: Array[String]): Unit = {
    }
    val a = take_input()

    var b = calculate_factorial(a)

    show_results(a, b)

    def take_input() : Int = {
        val x = readLine("Please give a number: ");
        return x.toInt
    }
    def calculate_factorial(a: Int) : Int = {
        var x = 1
        for (i <- 1 to a){
            x *= i
        }
        return x
    }
    def show_results(a: Int, b: Int) = {
        println("Factorial for " + a + " is " + b + ".")
    }
} 