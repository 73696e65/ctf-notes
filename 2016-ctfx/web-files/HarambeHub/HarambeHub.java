import java.util.ArrayList;
import java.util.List;

import static spark.Spark.*;

/**
 * Created by aashish on 8/26/16.
 */
public class HarambeHub {
    public static void main(String[] args) {
        post("/users", (req, res) -> {
            String username = req.queryParams("username");
            String password = req.queryParams("password");
            String realName = req.queryParams("real_name");
            if(username == null || password == null) {
                return "FAILED";
            }
            for(User user : User.users) {
                if(user.getUsername().matches(username)) {
                    return "FAILED: User with that name already exists!";
                }
            }
            new User("[Member] " + username, password, realName);
            return "OK: Your username is \"" + "[Member] " + username + "\"";
        });
        get("/name", (req, res) -> {
            String username = req.queryParams("username");
            String password = req.queryParams("password");
            if(username == null || password == null) {
                return "FAILED";
            }
            for(User user : User.users) {
                if(user.verify(username, password)) {
                    return user.getRealName();
                }
            }
            return "FAILED";
        });
    }
}
