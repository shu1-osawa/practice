package MTmain;

//import java.util.Random;
import java.io.File;
import java.io.FileWriter;

import mt_Random.MersenneTwister;

public class UsingMersenneTwister {
	 public static void main(String[] args){
		 File file = new File(file_name);
		 FileWriter filewriter = new FileWriter(file);
		 MersenneTwister rand = new MersenneTwister();
	        double minNum = Double.MAX_VALUE;
	        double maxNum = Double.MIN_VALUE;
	        for(int i = 0; i < 10000; i++)
	        {
	        	rand.setSeed(i);
	            double x = rand.nextDouble();
	            if(x > maxNum) maxNum = x;
	            if(x < minNum) minNum = x;
	        }
	        System.out.printf("MAX %.4f%n,MIN %.4f ", maxNum,minNum );
	    
	}
}
