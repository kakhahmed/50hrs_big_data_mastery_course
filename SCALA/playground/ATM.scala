import scala.io.StdIn.readLine


object Main {
    def main(args: Array[String]): Unit = {
        var correct_credentials = false;
        var continue = true;
        val max_tries = 5
        var tries = 0
        var balance = 2000;
        var tries_finished = false;
        // Mocking the check_credentials function.
        def check_credentials(cardNumber: String, pin: String): Boolean = {
            return (cardNumber == "12345" && pin == "6789")
        }
        def check_balance() = {
            println("You have a balance of " + balance + " Euros.")
        }
        def withdraw_amount(x: Int) = {
            if (x > balance) {
                println("Operation is not possible you don't have enough money to withdraw " + x + " Euros")
            }
            else {
                println("Withdrawing " + x + " for your " + balance + " Euros balance.")
                println("You now have a total balance of " + (balance - x) + " Euros.")
                balance -= x
            }
        }
        def deposit_amount(x: Int) = {
            println("Depositing " + x + " to your " + balance + " Euros balance.")
            println("You now have a total balance of " + (x + balance) + " Euros.")
            balance += x
        }
        def quit() = {
            println("Bye!")
        }
        while (!tries_finished && !correct_credentials) {
            var x = readLine("Please write the 5 digit card number: ");
            var y = readLine("Please write the 4 digit pin: ");
            correct_credentials = check_credentials(x, y);
            if (correct_credentials) {
                while (continue){
                    var z = readLine(
                        "Choose your preferred action (1) Check Balance, (2) Withdraw, (3) Deposit, or (4) Quit: ");
                    if (z == "1" || z == "Check Balance") {
                        check_balance();
                    }
                    else if (z == "2" || z == "Withdraw") {
                        var w = readLine("How much to withdraw?: ")
                        withdraw_amount(w.toInt)
                    }
                    else if (z == "3" || z == "Deposit") {
                        var w = readLine("How much to deposit?: ")
                        deposit_amount(w.toInt)
                    }
                    else if (z == "4" || z == "Quit") {
                        quit()
                        continue = false
                    }
                    else {
                        println("Wrong input.")
                    }
                }
            }
            else {
                println("Wrong credentials are given. Please try again.")
                tries += 1
            }
            if (tries > 5) {
                tries_finished = true
            }
        }
    }
}