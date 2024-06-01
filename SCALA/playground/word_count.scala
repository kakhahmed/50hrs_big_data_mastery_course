import scala.io.StdIn.readLine
import scala.collection.mutable.Map

object Main {
    def main(args: Array[String]): Unit = {
        var numWords = readLine("How many words do you want to enter? -> ").toInt;
        var words = Map[String, Int]()
        for (n <- 1 to numWords) {
            var w = readLine(s"Please enter word number ${n}: ").toLowerCase().trim;
            println(w)
            if words.contains(w) then words(w) += 1 else words(w) = 1;
        }

        println("Enter a word to check how much it was entered.");
        var w = readLine("-> ").toLowerCase().trim

        val n = words.getOrElse(w, 0)

        println(s" The word ${w} was added ${n} times.");
    }
}