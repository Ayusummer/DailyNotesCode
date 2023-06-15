package rce;

import java.lang.reflect.Method;

public class CMDExec {
    public static void main(String[] args) throws Exception {
        // 正常写法
//        java.lang.Runtime.getRuntime().exec("calc");

        // 反射写法
//        try {
//            Class<?> cls = Class.forName("java.lang.Runtime");
//            Method method = cls.getMethod("getRuntime");
//            Runtime runtime = (Runtime) method.invoke(null);
//            runtime.exec("calc");
//        } catch (Exception e) {
//            e.printStackTrace();
//        }

        // 将反射写法写为一行
//        ((Runtime) Class.forName("java.lang.Runtime").getMethod("getRuntime").invoke(null)).exec("calc");

        // 另一种将反射写法写为一行的方式
        Class.forName("java.lang.Runtime").getMethod("exec", String.class).invoke(
                Class.forName("java.lang.Runtime").getMethod("getRuntime").invoke(null),
                "calc"
        );
//        "va".getClass().forName("java.lang.Runtime").getMethod("exec", String.class).invoke(
//                "va".getClass().forName("java.lang.Runtime").getMethod("getRuntime").invoke(null),
//                "calc"
//        );


        // 一行反射, 尝试拆分字符串
//        Class.forName("java"+".lang.Runtime").getMethod("exec", String.class).invoke(
//                Class.forName("java.la"+"ng.Runtime").getMethod("getRuntime").invoke(null),
//                "calc"
//        );
//        "va".getClass().forName("java.lan"+"g.Runtime").getMethod("exec", String.class).invoke(
//                "va".getClass().forName("java.l"+"ang.Runtime").getMethod("getRuntime").invoke(null),
//                "calc"
//        );

    }
}
