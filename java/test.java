import reflect.reflect;

public class test {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        reflect r = new reflect();
        r.by_getClass();
        r.by_class();
        try {
            r.by_forName();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}