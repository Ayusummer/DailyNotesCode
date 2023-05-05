package reflect;

// BufferedReader 是缓冲字符输入流。它继承于Reader。
import java.io.BufferedReader;
import java.io.IOException;
// InputStreamReader 是字节流通向字符流的桥梁。它读取字节，并使用指定的charset将其解码为字符。
import java.io.InputStreamReader;

public class shell {

    public void shell_exec(String command) throws IOException {
        // 执行命令
        Process ShellProcess = Runtime.getRuntime().exec(command);
        // 获取结果
        ShellProcess.getOutputStream().close();
        String line;
        System.out.println("Standard Output:");
        BufferedReader stdout = new BufferedReader(new InputStreamReader(
                ShellProcess.getInputStream()));
        while ((line = stdout.readLine()) != null) {
            System.out.println(line);
        }
        stdout.close();
        System.out.println("Standard Error:");
        BufferedReader stderr = new BufferedReader(new InputStreamReader(
                ShellProcess.getErrorStream()));
        while ((line = stderr.readLine()) != null) {
            System.out.println(line);
        }
        stderr.close();
        System.out.println("Done");
    }

    public static void main(String args[]) throws IOException {
        System.out.println("Hello World");
        System.out.println("Powershell");
        shell s = new shell();
        s.shell_exec("powershell.exe $PSVersionTable.PSVersion");
        System.out.println("cmd");
        s.shell_exec("cmd.exe /c ver");
    }
}
