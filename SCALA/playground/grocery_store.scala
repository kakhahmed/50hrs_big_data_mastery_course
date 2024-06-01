import scala.io.StdIn.readLine
import scala.collection.mutable.ListBuffer
import scala.collection.immutable.List

case class Product(name: String, price: Double, count: Int) {
    def totalValue: Double = price * count;

    def displayInfo(): Unit = {
        println(s"Name: ${name}, Price: ${price}, Count: ${count}");
    }
}

object Main {
    def main(args: Array[String]): Unit = {
        // Enter production Information or quit the program
        println("Welcome to our grocery.");

        var quit = false;
        var products = ListBuffer[Product]();
        while (!quit) {
            var x = readLine("Please type the product name or type Q for quitting: ");
            if (x.toLowerCase == "q") {
                quit = true;
            } else {
                // option (1)
                // What is the item name? price? count?
                var name = x;
                var price = readLine("Please provide the price: ").toDouble;
                var count = readLine("Please provide the count: ").toInt;
                val p = Product(name, price, count);
                products += p;
            }
        }
        //Display the user entered products.
        println("Entered products:");
        var totalPrice = 0.0;
        for (p <- products) {
            totalPrice += p.totalValue
            p.displayInfo();
        }
        println(s"The total bill is: ${totalPrice}");

    }
}