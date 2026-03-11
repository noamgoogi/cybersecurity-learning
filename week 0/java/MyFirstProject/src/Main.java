public class Main {
    public static void main(String[] args) {

        /* lesson
        System.out.println("Hello and welcome!");
        System.out.print("Hello and welcome!");
         */

        /* lesson
        int num;
        num = 5;
        double num2 = 2.0;
        char ch = 'a';
        boolean bool = true;
        String name = "Noam";
         */


        /*
        // import java.util.Scanner;
        /*
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello " + name);

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        scanner.nextLine();
        System.out.println("Your age is " + age);

        System.out.print("Enter your gpa: ");
        double gpa = scanner.nextDouble();
        System.out.println("Your gpa is " + gpa);

        System.out.print("Enter if you are a student (True/False): ");
        boolean isStudent = scanner.nextBoolean();
        System.out.println("Your student is " + isStudent);

        scanner.close();
         */

        //Calculate area of a tringle
        /*
        System.out.println(4/3);
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the base: ");
        double base = scanner.nextDouble();
        System.out.println("Enter the height: ");
        double height = scanner.nextDouble();
        double area = (base * height) / 2.0;
        System.out.println("The area of the tringle is " + area);
         */

        // SHOPPING CART PROGRAM
        /*
        String item;
        double price;
        int amount;
        double total;
        Scanner scanner = new Scanner(System.in);

        System.out.print("Please enter the item name: ");
        item = scanner.nextLine();

        System.out.print("Please enter the item price: ");
        price = scanner.nextDouble();

        System.out.print("Please enter the item amount: ");
        amount = scanner.nextInt();

        total = price * amount;
        System.out.println("You buy " + item + ", price = $" + price + ", total = $" + total)ף
         */


        /* lesson
        Random random = new Random();
        int num = random.nextInt(1,6);
        double d = random.nextDouble();
        boolean bool = random.nextBoolean();
        System.out.println(bool);
         */

        /*
        Scanner scanner = new Scanner(System.in);
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = Math.sqrt(a*a+b*b);
        System.out.println(c);
         */

        /*
        String name = "Noam";
        char firstLetter = name.charAt(0);
        int age = 30;
        double height = 1080;

        System.out.printf("Hello %s\n", name);
        System.out.printf("Your name starts with a %c\n", firstLetter);
        System.out.printf("Your age is %d\n", age);
        System.out.printf("Your height is %.3f\n", height);
        System.out.printf("Your height is %,.3f\n", height);
         */

        //WEIGHT CONVERTER
//        Scanner scanner = new Scanner(System.in);
//
//        double weight;
//        String type;
//
//
//        System.out.print("Enter weight: ");
//        weight = scanner.nextDouble();
//        scanner.nextLine();
//
//        System.out.print("Enter type: ");
//        type = scanner.nextLine();
//
//        if (type.equals("kg")) System.out.printf("%.2f lbs", weight*2.2);
//        else if (type.equals("lbs")) System.out.printf("%.2f kg", weight/2.2);
//        else System.out.println("not a valid type");


            //System.out.println(add(1,2,3,4,5,6,7,8,9));


        Worker w1 = new Worker("Noam", 32, 2000);
        Worker w2 = new Worker("Noam", 32, 2000);
        Worker w3 = new Worker("Noam", 32, 2000);


        System.out.println(w1.getAge());
        System.out.println(w2.getName());
        System.out.println(w3.getSalary());
        System.out.println(Worker.numOfWorkers);

        System.out.println(w1);



    }

    /*
    public static int add(int... nums)
    {
        int sum = 0;
        for (int num : nums)
        {
            sum += num;
        }
        return sum;
    }
     */

}