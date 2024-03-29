import java.lang.reflect.Method;

public class CMDExec {

  public void CMDExecWin() throws Exception {
    // 正常写法
    java.lang.Runtime.getRuntime()
        .exec("cmd /c type nul > out/success233-1");

    // 反射写法
    try {
      Class<?> cls = Class.forName("java.lang.Runtime");
      Method method = cls.getMethod("getRuntime");
      Runtime runtime = (Runtime) method.invoke(null);
      runtime.exec("cmd /c type nul > out/success233-2");
    } catch (Exception e) {
      e.printStackTrace();
    }

    // 将反射写法写为一行
    ((Runtime) Class.forName("java.lang.Runtime").getMethod("getRuntime").invoke(null))
        .exec("cmd /c type nul > out/success233-3");

    // 另一种将反射写法写为一行的方式
    Class.forName("java.lang.Runtime").getMethod("exec", String.class).invoke(
        Class.forName("java.lang.Runtime").getMethod("getRuntime").invoke(null), "cmd /c type nul > out/success233-4");

    "va".getClass().forName("java.lang.Runtime").getMethod("exec", String.class).invoke(
        "va".getClass().forName("java.lang.Runtime").getMethod("getRuntime").invoke(null),
        "cmd /c type nul > out/success233-5");

    // 一行反射, 尝试拆分字符串
    Class.forName("java" + ".lang.Runtime").getMethod("exec", String.class)
        .invoke(Class.forName("java.la" + "ng.Runtime").getMethod("getRuntime").invoke(null),
            "cmd /c type nul > out/success233-6");

    "va".getClass().forName("java.lan" + "g.Runtime").getMethod("exec", String.class).invoke(
        "va".getClass().forName("java.l" + "ang.Runtime").getMethod("getRuntime").invoke(null),
        "cmd /c type nul > out/success233-7");
  }

  public void CMDExecLinux() throws Exception {
    // 正常写法
    java.lang.Runtime.getRuntime().exec("touch out/success233-1");

    // 反射写法
    try {
      Class<?> cls = Class.forName("java.lang.Runtime");
      Method method = cls.getMethod("getRuntime");
      Runtime runtime = (Runtime) method.invoke(null);
      runtime.exec("touch out/success233-2");
    } catch (Exception e) {
      e.printStackTrace();
    }

    // 将反射写法写为一行
    ((Runtime) Class.forName("java.lang.Runtime").getMethod("getRuntime").invoke(null)).exec("touch out/success233-3");

    // 另一种将反射写法写为一行的方式
    Class
        .forName("java.lang.Runtime")
        .getMethod("exec", String.class)
        .invoke(
            Class.forName("java.lang.Runtime").getMethod("getRuntime").invoke(null),
            "touch /tmp/success233-4");

    "va".getClass().forName("java.lang.Runtime").getMethod("exec", String.class).invoke(
        "va".getClass().forName("java.lang.Runtime").getMethod("getRuntime").invoke(null), "touch out/success233-5");

    // 一行反射, 尝试拆分字符串
    Class.forName("java" + ".lang.Runtime").getMethod("exec", String.class).invoke(
        Class.forName("java.la" + "ng.Runtime").getMethod("getRuntime").invoke(null),
        "touch out/success233-6");

    "va".getClass().forName("java.lan" + "g.Runtime").getMethod("exec", String.class).invoke(
        "va".getClass().forName("java.l" + "ang.Runtime").getMethod("getRuntime").invoke(null),
        "touch out/success233-7");
  }

  public static void main(String[] args) throws Exception {
    CMDExec cmdExec = new CMDExec();
    cmdExec.CMDExecWin();
    // cmdExec.CMDExecLinux();
  }
}
