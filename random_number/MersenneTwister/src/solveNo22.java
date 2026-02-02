import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;

public class solveNo22 {
	public static void main(String[] args) throws Exception {
        // TODO Auto-generated method stub

        ArrayList<String> names = new ArrayList<String>();

        BufferedReader numReader = new BufferedReader(new FileReader("src/names.txt"));
        String line = "";

        while ((line = numReader.readLine()) != null) {
            String[] dataNames = line.split(",");

            for (String item : dataNames) {
                String newItem = item.substring(1, item.length() - 1);
                names.add(newItem);
            }
        }
        numReader.close();

        Collections.sort(names);

        long bigSum = 0;
        int mult = 1;
        for (int i = 0; i < names.size(); i++) {
            int x = valueOfName(names.get(i));
            mult = x * i;

            bigSum += mult;
        }

        System.out.println("Sum: " + bigSum);
    }

    public static int valueOfName(String s) {
        char[] ABC = {'1', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

        char[] tempName = s.toCharArray();

        int sum = 0;
        for (char c : tempName) {
            for (int j = 0; j < ABC.length; j++) {
                if (c == ABC[j])
                    sum += j;
            }
        }
        return sum;
    }
}