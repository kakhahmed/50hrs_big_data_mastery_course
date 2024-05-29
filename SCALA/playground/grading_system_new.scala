import scala.io.StdIn.readLine

object Main {
    def main(args: Array[String]): Unit = {
        var mark = 0;
        var done = false;
        var num_courses = 0;
        var grades_sum = 0;
        var _ = readLine("Please write the grade for each course one at a time. when you finish please write: finished, ok? ");
        while (!done) {
            var input = readLine("Please write the grade for subject number " + (num_courses + 1) + " : ");
            try {
                var grade = input.toInt;
                if (grade >= 0 && grade <= 100) {
                    num_courses += 1;
                    grades_sum += grade;
                } else {
                    println("Wrong input value! Please enter a value from 0 to 100.");
                }
            } catch {
                case _: NumberFormatException =>
                if (input == "finished") {
                    done = true;
                }
                input = readLine("Did you finish all grades? Y/N: ");
                if (input == "Y") {
                    done = true;
                }
            }
        }

        if (num_courses != 0) {
            mark = grades_sum / num_courses;
        }
        if (mark > 90) {
            println("Your grade is A");
        } else if (mark > 70) {
            println("Your grade is B");
        } else if (mark > 60) {
            println("Your grade is C");
        } else if (mark > 50) {
            println("Your grade is D");
        } else {
            println("Your grade is F");
        }
    }
}
