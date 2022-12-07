package reflect;

public class reflect {
    // 1. 通过对象调用 getClass() 方法获取 Person 的 Class;
    // 通常用于传入一个 Object 对象, 但是不知道具体是什么类, 通过 getClass() 方法获取 Class 对象;
    public void by_getClass(){
        System.out.println("1. 通过对象调用 getClass() 方法获取 Person 的 Class;");
        Person person1 = new Person();
        Class c1 = person1.getClass();
        System.out.println(c1.getName());
    }

    // 2.直接通过 类名.class 的方式得到,该方法最为安全可靠，程序性能更高
    //   这说明每个类都有一个隐含的静态成员变量 class
    public void by_class(){
        System.out.println("2.直接通过 类名.class 的方式得到,该方法最为安全可靠，程序性能更高");
        Class c2 = Person.class;
        System.out.println(c2.getName());
    }

    // 3.通过 Class 类的静态方法 forName(String className) 得到
    //   该方法将类的全名（包括包名）作为参数，返回对应的 Class 对象
    //   用的最多, 但可能抛出 ClassNotFoundException 异常
    public void by_forName() throws ClassNotFoundException{
        System.out.println("3.通过 Class 类的静态方法 forName(String className) 得到");
        Class c3 = Class.forName("reflect.Person");
        System.out.println(c3.getName());
    }

}
