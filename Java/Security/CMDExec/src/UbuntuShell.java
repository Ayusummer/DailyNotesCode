

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class UbuntuShell {

  public void shell_exec(String shell_type, String command) {
    try {
      // 创建一个 ProcessBuilder 对象，指定要执行的命令和参数
      // -c 表示从后面的字符串中读取命令
      ProcessBuilder pb = new ProcessBuilder(shell_type, "-c", command);
      // 启动一个进程，执行命令
      Process process = pb.start();
      // 获取进程的输出流
      BufferedReader reader = new BufferedReader(
        new InputStreamReader(process.getInputStream())
      );
      // 读取输出流的内容，并打印到控制台
      String line;
      while ((line = reader.readLine()) != null) {
        System.out.println(line);
      }
      // 等待进程结束，获取退出码
      int exitCode = process.waitFor();
      System.out.println("Exit code: " + exitCode);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  // // 一句话写法(不try catch) 
  // public void OneLineBash(){
  //     "".getClass().forName("java.lang.Runtime").getMethod("getRuntime",null).invoke(null,null).exec("ls");
  // }

  public static void main(String[] args) {
    UbuntuShell shell_test = new UbuntuShell();

    System.out.println("bash");
    shell_test.shell_exec("bash","echo hello world");

    System.out.println("sh");
    shell_test.shell_exec("sh","echo hello world");

    

    // System.out.println("一句话写法:");
    // bashTest.OneLineBash();
  }
}
