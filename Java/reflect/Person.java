package reflect;

public class Person {
    private String name = "Jacob";
    public int age = 20;
    public Person(){
        System.out.println("Person()");
    }
    private void say(){
        System.out.println("Hello World!");
    }
    public void work(){
        System.out.println("I'm working!");
    }

    public static void main(String[] args) {
        Person p = new Person();
        p.say();
        p.work();
    }
}
