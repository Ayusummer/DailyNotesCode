import java.io.IOException;
import java.net.Socket;

public class Port {

  public static boolean check_port(String ip_or_domain, int port) {
    try (Socket server = new Socket(ip_or_domain, port)) {
      System.out.println("Port " + port + " is OPEN on " + ip_or_domain);
      return true;
    } catch (IOException ignored) {
      System.out.println("Port " + port + " is CLOSED on " + ip_or_domain);
      return false;
    }
  }

  public static void main(String[] args) {
    boolean is_open = check_port("127.0.0.1", 443);
  }
}
