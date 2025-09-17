
// UF1289 - Diseño de componentes (Java)
public interface AuthService {
    boolean login(String user, String password);
    void logout(String user);
}

public class SimpleAuthService implements AuthService {
    @Override
    public boolean login(String user, String password) {
        return "admin".equals(user) && "1234".equals(password);
    }

    @Override
    public void logout(String user) {
        System.out.println(user + " logged out.");
    }
}
