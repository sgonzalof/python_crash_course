
// UF1290 - Implementación e integración (Java)
public class UserComponent {
    private String username;

    public UserComponent(String username) {
        this.username = username;
    }

    public String getUsername() {
        return username;
    }
}

public class UserService {
    public void register(UserComponent user) {
        System.out.println("User registered: " + user.getUsername());
    }
}
