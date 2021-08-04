
public class Program {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int days = scanner.nextInt();
		
		//your code goes here
		int hours = days * 24;
		int minutes = hours * 60;
		int seconds = minutes * 60;
		System.out.print(seconds);
		
	}
}


public class Program
{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int amount = scanner.nextInt();
		 for (int x = 0; x <3; x++){
			int actual_amount = (amount * 10)/100;
            amount = amount - actual_amount; 
        }
		System.out.println(amount);       		
	}
}


public class Program
{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String text = scanner.nextLine();
		char[] arr = text.toCharArray();
		
		//your code goes here
		int n=arr.length;
		String str="";
       for(int i=n-1 ; i>-1 ; i--){
		   str=str+arr[i];
	   }		 
	   System.out.println(str);
	}
}

public class Converter {
    public static String toBinary(int num) {
      String binary="";
      while(num > 0) {
          binary = (num%2)+binary;
          num /= 2;
          }
       return binary;
    } 
  }
  
  
  public class Program {
      public static void main(String[ ] args) {
          Scanner sc = new Scanner(System.in);
          int x = sc.nextInt();
          System.out.print(Converter.toBinary(x));
      }
  }


  import java.util.Scanner;

abstract class Shape {
    int width;
    abstract void area();
}
//your code goes here
class Square extends Shape {
    public Square(int w){
        width = w;
    }
    public void area(){
        width = width*width;
        System.out.println(width);
    }
}

class Circle extends Shape {
    public Circle(int w){
        width = w;
    }
    public void area() {
        double areaCircle = (double)Math.PI*(int)width*(int)width;
        System.out.println(areaCircle);
    }
}


public class Program {
    public static void main(String[ ] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        
        Square a = new Square(x);
        Circle b = new Circle(y);
        a.area();
        b.area();
    }
}


public class MyClass {
    public static void main(String[ ] args) {
        try {
            int a[ ] = new int[2];
            System.out.println(a[5]);
        } catch (Exception e) {
            System.out.println("An error occurred");
        }
    }
}

public class Program {

    static int div(int a, int b) throws ArithmeticException {
        if(b == 0) {
            throw new ArithmeticException("Division by Zero");
        } else {
            return a / b;
        }
    }

    public static void main(String[] args) {
        System.out.println(div(42, 0));
    }

}

class Loader extends Thread {
    public void run() {
        System.out.println("Hello");
    }
}

class MyClass {
    public static void main(String[ ] args) {
        Loader obj = new Loader();
        obj.start();
    }
}

class Loader implements Runnable {
    public void run() {
        System.out.println("Hello");
    }
}

class MyClass {
    public static void main(String[ ] args) {
        Thread t = new Thread(new Loader());
        t.start();
    }
}


public class MyClass {
    public static void main(String[ ] args) {
      try {
        Thread.sleep(1000);
      } catch (InterruptedException e) {
        //some code
      }
    }
  }
public class MyClass {
    public static void main(String[ ] args) {
        int value = 7;
        value = value / 0;
    }
}

import java.util.ArrayList;
//...
ArrayList colors = new ArrayList();
ArrayList<String> colors = new ArrayList<String>(10);


import java.util.ArrayList;

public class MyClass {
    public static void main(String[ ] args) {
        ArrayList<String> colors = new ArrayList<String>();
        colors.add("Red");
        colors.add("Blue");
        colors.add("Green");
        colors.add("Orange");
        colors.remove("Green");
        
        System.out.println(colors);
    }
}

import java.util.LinkedList;

public class MyClass {
    public static void main(String[ ] args) {
        LinkedList<String> c = new LinkedList<String>();
        c.add("Red");
        c.add("Blue");
        c.add("Green");
        c.add("Orange");
        c.remove("Green");
        System.out.println(c);
    }
}

import java.util.HashMap;

public class MyClass {
    public static void main(String[ ] args) {
        HashMap<String, Integer> points = new HashMap<String, Integer>();
        points.put("Amy", 154);
        points.put("Dave", 42);
        points.put("Rob", 733);
        System.out.println(points.get("Dave")); 
    }
}

import java.util.HashSet;

public class MyClass {
    public static void main(String[ ] args) {
        HashSet<String> set = new HashSet<String>();
        set.add("A");
        set.add("B");
        set.add("C");
        System.out.println(set);
    }
}

import java.util.ArrayList;
import java.util.Collections;

public class MyClass {
    public static void main(String[ ] args) {
        ArrayList<String> animals = new ArrayList<String>();
        animals.add("tiger");
        animals.add("cat");
        animals.add("snake");
        animals.add("dog");
        
        Collections.sort(animals);
       
        System.out.println(animals);
    }
}

import java.util.Iterator;
import java.util.LinkedList;

public class MyClass {
    public static void main(String[ ] args) {
        LinkedList<String> animals = new LinkedList<String>();
        animals.add("fox");
        animals.add("cat");
        animals.add("dog");
        animals.add("rabbit");
        
        Iterator<String> it = animals.iterator();
        String value = it.next();
        System.out.println(value);
    }
}

import java.util.Iterator;
import java.util.LinkedList;

public class MyClass {
    public static void main(String[ ] args) {
        LinkedList<String> animals = new LinkedList<String>();
        animals.add("fox");
        animals.add("cat");
        animals.add("dog");
        animals.add("rabbit");
        
        Iterator<String> it = animals.iterator();
        while(it.hasNext()) {
            String value = it.next();
            System.out.println(value);   
        }
    }
}

import java.io.File;

public class MyClass {
  public static void main(String[ ] args) {
    File x = new File("C:\\sololearn\\test.txt");
    if(x.exists()) {
     System.out.println(x.getName() +  "exists!");
    }
    else { 
     System.out.println("The file does not exist");
    }
  }
}

try {
    File x = new File("C:\\sololearn\\test.txt");
    Scanner sc = new Scanner(x);      
  }
   catch (FileNotFoundException e) {
  
  }


  try {
    File x = new File("C:\\sololearn\\test.txt");
    Scanner sc = new Scanner(x);
    while(sc.hasNext()) {
      System.out.println(sc.next());
    }
    sc.close();
  } catch (FileNotFoundException e) {
    System.out.println("Error");
  }

  import java.util.Formatter;

public class MyClass {
   public static void main(String[ ] args) {
  try {
    Formatter f = new Formatter("C:\\sololearn\\test.txt");
  } catch (Exception e) {
      System.out.println("Error");
  }
  }
}

import java.io.File;
import java.util.Scanner;
import java.util.Formatter;

public class MyClass {
    public static void main(String[ ] args) {
        try {
            Formatter f = new Formatter("test.txt");
            f.format("%s %s %s", "1","John", "Smith \r\n");
            f.format("%s %s %s", "2","Amy", "Brown");
            f.close();

            File x = new File("test.txt");
            Scanner sc = new Scanner(x);
            while(sc.hasNext()) {
                System.out.println(sc.next());
            }
            sc.close();
        } catch (Exception e) {
        System.out.println("Error");
        }
    }
}




import java.util.*; 

public class Bowling {
    HashMap<String, Integer> players;
    Bowling() {
        players = new HashMap<String, Integer>();
    }
    public void addPlayer(String name, int p) {
        players.put(name, p);
    }
    public void getWinner(){
        String best="";
        Iterator<Map.Entry<String,Integer>> it =players.entrySet().iterator();
        int max=0;
        while(it.hasNext()){
        
         String playerName=it.next().getKey();
      Integer checkVal=players.get(playerName);
          if (checkVal>=max){
        
              max=checkVal;
              best=playerName;
          }
            
        }
        
       System.out.println(best);
    }
    
}

public class Program {
    public static void main(String[ ] args) {
        Bowling game = new Bowling();
        Scanner sc = new Scanner(System.in);

        for(int i=0;i<3;i++) {
            String input = sc.nextLine();
            String[] values = input.split(" ");
            String name = values[0];
            int points = Integer.parseInt(values[1]);
            game.addPlayer(name, points);
        }
        game.getWinner();
    }
}
