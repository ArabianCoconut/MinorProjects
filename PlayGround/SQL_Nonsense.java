package MinorProjects.PlayGround;
/*
  Created by ArabianCoconut.
  Date: 2022-09-01
  About: This is a program that will create python file to run SQL queries in python file.
 */
import java.io.*;
import java.nio.charset.Charset;
public class SQL_Nonsense {
 
    public static void main(String[] args) {
        String file= "somebody.py";
        String username="username = 'Somebody_CodeWars'\n";
        String password="password = 'Somebody_CodeWars'\n";
        String sql="print(\"SELECT * FROM users WHERE \" \"username=\"'{}' \" AND password=\"'{}'\"\".format(username, password))";
        String finalMessage = "File Created and Somebody is Salty!";
       try(FileWriter python = new FileWriter(file, Charset.defaultCharset(), true)){
           python.write(username);
           python.write(password);
           python.write(sql);
       } catch (IOException e) {
           e.printStackTrace();
       }
        String cmd ="python somebody.py";
         try {
              Process p = new ProcessBuilder("cmd", "/c", cmd).start();
              BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
              BufferedReader stdError = new BufferedReader(new InputStreamReader(p.getErrorStream()));
                String s;
              while ((s = stdInput.readLine()) != null) {
                System.out.println(s);
              }
              while ((s = stdError.readLine()) != null) {
                System.out.println(s);
              }
         } catch (IOException e) {
              e.printStackTrace();
         }
       System.out.println(finalMessage);
       
    }
}
