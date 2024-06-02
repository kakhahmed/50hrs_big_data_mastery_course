import scala.io.StdIn.readLine


object Main {
    def main(args: Array[String]): Unit = {
        var add = (x:Int, y:Int) => x + y;
        var div = (x:Int, y:Int) => x / y;
        var mul = (x:Int, y:Int) => x * y;

        println(mul(div(add(5, 3), 4), 5))
    }
}