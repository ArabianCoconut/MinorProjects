/**
 * @Author ArabianCoconut
 * @Version V1.0 Final
 * @Date 2022-09-03
 * @Description This is a simple web reader made in java using ready made libraries.
 **/

import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;

public class WebReader {
    //read from website and write to a file
    public static void main(String[] args) {
        // throw exception if website is not found
        try {
            // input website url by user
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Enter website url: ");
            String url = br.readLine();
            // create a URL object
            URL u = new URL(url);
            // create a URLConnection object
            URLConnection urlConnection = u.openConnection();
            // create a BufferedReader object
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
            // create a FileOutputStream object
            FileOutputStream fileOutputStream = new FileOutputStream("website_out.txt",true);
            // create a String variable
            String line;
            // read from the BufferedReader object
            while ((line = bufferedReader.readLine()) != null) {
                // HTML processing and outputting only the text to the file in .txt format
                //Select html tags to be written to file
                if (line.contains("<title>") || line.contains("<h1>") || line.contains("<h2>") || line.contains("<h3>") || line.contains("<h4>") || line.contains("<h5>") || line.contains("<h6>") || line.contains("<p>") || line.contains("<a>") || line.contains("<li>") || line.contains("<ul>") || line.contains("<ol>")) {
                    // remove HTML tags
                    line = line.replaceAll("<[^>]*>", "");
                    //remove HTML closing tags
                    line = line.replaceAll("</[^>]*>", "");
                    // remove white spaces
                    line = line.replaceAll("\\s+", " ");
                    // write to the FileOutputStream object
                    fileOutputStream.write(line.getBytes());
                }
            }
            // close the BufferedReader object
            bufferedReader.close();
            // close the FileOutputStream object
            fileOutputStream.close();
            System.out.println("Fetched and written to file successfully!");
        } catch (Exception e) {
            System.out.println("Error: Website not found and did not write to file.");
        }

    }
}
