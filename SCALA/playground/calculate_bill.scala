import scala.io.StdIn.readLine


object Main {
    def main(args: Array[String]): Unit = {
    }
    val a = get_bill_amount()

    val b = get_discount_amount()

    var c = apply_discount(a, b)

    print_bill(a, c)

    def get_bill_amount() : Float = {
        val x = readLine("Please enter the total bill: ");
        return x.toFloat
    }
    def get_discount_amount() : Float = {
        val x = readLine("Please enter the discount amount: ");
        var discount = x.toFloat
        if discount < 10 then discount = 10
        return discount
    }
    def apply_discount(bill: Float, discount: Float = 10) : Float = {
        return bill * (1 - (discount / 100))
    }
    def print_bill(total_bill: Float, discounted_bill: Float) = {
        println("Your bill was discounted from " + total_bill + " to " + discounted_bill + " .")
    }
} 