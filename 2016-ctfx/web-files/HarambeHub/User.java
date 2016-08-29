import java.util.ArrayList;
import java.util.List;

/**
 * Created by aashish on 8/26/16.
 */
public class User {
    static List<User> users = new ArrayList<>();

    private String username;
    private String master;
    private String realName;
    public User(String username, String password, String realName) {
        this.username = username;
        this.master = password;
        this.realName = realName;
        users.add(this);
    }

    public String getRealName() {
        return this.realName;
    }

    public boolean verify(String username, String password) {
        return this.username.equals(username) && this.master.matches(password);
    }

    public String getUsername() {
        return username;
    }

    @Override
    public String toString() {
        return username;
    }
}
