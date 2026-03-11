public class Worker
{
    private String name;
    private int age;
    private double salary;

    static int numOfWorkers;

    public Worker(String name, int age, double salary)
    {
        this.name = name;
        this.age = age;
        this.salary = salary;
        numOfWorkers ++;

    }

    public String getName()  {return name;}
    public int getAge()  {return age;}
    public double getSalary()  {return salary;}

    public void setName(String name)  {this.name = name;}
    public void setAge(int age)  {this.age = age;}
    public void setSalary(double salary)  {this.salary = salary;}

    @Override
    public String toString()
    {
        return "Name: " + name + ", Age: " + age + ", Salary: " + salary;
    }

}
