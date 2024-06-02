import scala.io.StdIn.readLine
import scala.collection.mutable.Stack
import scala.util.control.Breaks.{break, breakable}

object Main {
    def main(args: Array[String]): Unit = {
        val expression = readLine("Please write your expression: ");
        val unvalid_expression_str = "This is not a valid expression!";
        var open_brackets = Stack[Char]();
        breakable {
            for (i <- expression){
                if (i == '('){
                    open_brackets.push(i);
                } else if (i == ')') {
                    if (open_brackets.isEmpty) {
                        println(unvalid_expression_str)
                        break;
                    }
                    open_brackets.pop();
                }
            }
        }
        if (!open_brackets.isEmpty) {
            println(unvalid_expression_str);
        }
        else {
            println("This is a valid expression :)")
        }
    }
}