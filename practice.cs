using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SoloLearn
{
    class Program
    {
        static void Main(string[] args)
        {
            const double pi = 3.14;
            double radius = 5;
            radius = Double.Parse(Console.ReadLine());
            double area = pi * (radius*radius);
         
            Console.WriteLine(area);           
            
        }
    }
}

//using System;
//using System.Collections.Generic;


namespace SoloLearn
{
    class Program
    {
        static void Main(string[] args)
        {
            int number = Convert.ToInt32(Console.ReadLine());
            
            //your code goes here           
            for(int i=1; i<=number; i++)
            {                            
            if(i % 3==0)
                {
                     Console.WriteLine("*"); 
                }
                else
                {                  
                    Console.WriteLine(i);
                }
                 
             }                 
        }  
                                     
    }
}

//using System;
//using System.Collections.Generic;

namespace SoloLearn
{
    class Program
    {
        static void Main(string[] args)
        {
              int levels = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine(Points(levels));
        }
        

        
        static int Points(int levels)
        {
     
           if (levels == 1)
                  return 1;
              return levels + Points(levels - 1);
        }

    }

}

//using System;
//using System.Collections.Generic;

namespace Code_Coach_Challenge
{
    class Program
    {
        static void Main(string[] args)
        {
            string postText = Console.ReadLine();

            Post post = new Post();
            post.Text = postText;
            post.ShowPost();

        }
    }

    class Post
    {
        private string text;
        //write a constructor here
        public Post()
        {
            Console.WriteLine("New post");
        }        

        public void ShowPost()
        {
            Console.WriteLine(text);
        }
        //write a property for member text
        public string Text
        {
            get{return text;}
            set{text = value;}
        }
    }
}


//using System;
//using System.Collections.Generic;

namespace Code_Coach_Challenge
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = {
                "home",
                "programming",
                "victory",
                "C#",
                "football",
                "sport",
                "book",
                "learn",
                "dream",
                "fun"
            };

            string letter = Console.ReadLine();

            int count = 0;
            int y =1;
            while (
count < 9)
            {
              if(words[count].Contains(letter))
              {
               Console.WriteLine(words[count]);
               y += count;
              }
              count ++;
            }
             if(y == 0 || y == 1)
             {
                 Console.WriteLine("No match");
             }
            
        }
    }
}


//using System;
//using System.Collections.Generic;

namespace Code_Coach_Challenge
{
    class Program
    {
        static void Main(string[] args)
        {
            string name1 = Console.ReadLine();
            int points1 = Convert.ToInt32(Console.ReadLine());
            string name2 = Console.ReadLine();
            int points2 = Convert.ToInt32(Console.ReadLine());

            DancerPoints dancer1 = new DancerPoints(name1, points1);
            DancerPoints dancer2 = new DancerPoints(name2, points2);

            DancerPoints total = dancer1 + dancer2;
            Console.WriteLine(total.name);
            Console.WriteLine(total.points);
        }
    }

    class DancerPoints
    {
        public string name;
        public int points;
        public DancerPoints(string name, int points)
        {
            this.name = name;
            this.points = points;
        }

        //overload the + operator
           public static DancerPoints operator+ (DancerPoints a, DancerPoints b) {
            string name = a.name +" "+"&"+" "+ b.name ;
            int points = a.points + b.points ;
            DancerPoints total = new DancerPoints (name, points);
            return total ;
        }

    }
}
    

namespace Code_Coach_Challenge
{
    class Program
    {
        static void Main(string[] args)
        {
            Draw pencil = new Draw();
            Draw brush = new Brush();
            Draw spray = new Spray();

            pencil.StartDraw();
            brush.StartDraw();
            spray.StartDraw();

        }
    }

    /*
    Draw => "Using pencil"
    Brush => "Using brush"
    Spray => "Using spray"
    */

    public interface IDraw
    {
        void StartDraw();
    }

    class Draw : IDraw
    {
        public virtual void StartDraw()
        {
            Console.WriteLine("Using pencil");
        }
    }

    //inherit this class from the class Draw
    class Brush:Draw
    {
        //implement the StartDraw() method
            public override  void StartDraw()
        {
            Console.WriteLine("Using brush");
        }
    }

    //inherit this class from the class Draw
    class Spray:Draw
    {
        //implement the StartDraw() method
          public override void StartDraw()
        {
            Console.WriteLine("Using spray");
        }
    }
}

//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

namespace SoloLearn
{
    class Program
    {
        static void Main(string[] args)
        {
           

          
try {
  int drinks = Convert.ToInt32(Console.ReadLine());
  int shelves = Convert.ToInt32(Console.ReadLine());
  Console.WriteLine(drinks / shelves);
}
catch (DivideByZeroException e) {
  Console.WriteLine("At least 1 shelf");
}


catch(Exception e) {
  Console.WriteLine("Please insert an integer");
}

         
        }
    }
}

static void Swap(ref int a, ref int b) {
  int temp = a;
  a = b;
  b = temp;
}
static void Swap<T>(ref T a, ref T b) {
  T temp = a;
  a = b;
  b = temp;
}

//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;
namespace SoloLearn
{
    class Program
    {
        static void Swap<T>(ref T a, ref T b) {
            T temp = a;
            a = b;
            b = temp;
        }
        static void Main(string[] args)
        {
            int a = 4, b = 9;
            Swap<int>(ref a, ref b);
            Console.WriteLine(a+" "+b);
            
            string x = "Hello";
            string y = "World";
            Swap<string>(ref x, ref y);
            Console.WriteLine(x+" "+y);
        }
    }
}
class Stack<T> {
  int index=0;
  T[] innerArray = new T[100];
  public void Push(T item) {
    innerArray[index++] = item; 
  }
  public T Pop() {
    return innerArray[--index]; 
  }
  public T Get(int k) { return innerArray[k]; }
}

Stack<int> intStack = new Stack<int>();
Stack<string> strStack = new Stack<string>();
Stack<Person> PersonStack = new Stack<Person>();


namespace SoloLearn
{
    class Program
    {
        class Stack<T> {
            int index=0;
            T[] innerArray = new T[100];
            public void Push(T item) {
                innerArray[index++] = item; 
            }
            public T Pop() {
                return innerArray[--index]; 
            }
            public T Get(int k) { return innerArray[k]; }
        }
        static void Main(string[] args)
        {
            Stack<int> intStack = new Stack<int>();
            intStack.Push(3);
            intStack.Push(6);
            intStack.Push(7);
            
            Console.WriteLine(intStack.Get(1));
        }
    }
}

namespace SoloLearn
{
	class Program
	{
		static void Main(string[] args)
		{
		    List<int> li = new List<int>();
            li.Add(59);
            li.Add(72);
            li.Add(95);
            li.Add(5);
            li.Add(9);
            li.RemoveAt(1); // remove 72
            
            Console.Write("\nList: ");
            for (int x = 0; x < li.Count; x++)
                Console.Write(li[x] + " "); // 59  95  5  9
            li.Sort();
            Console.Write("\nSorted: ");
            for (int x = 0; x < li.Count; x++)
                Console.Write(li[x] + " "); // 5  9  59  95
		}
	}
}



namespace SoloLearn
{
	class Program
	{
		static void Main(string[] args)
		{
		    SortedList<string, int> sl = new SortedList<string, int>();

		    sl.Add("Solo", 59);
		    sl.Add("A", 95);
		    sl.Add("Learn", 72);
		    sl.Remove("A");
            
		    Console.WriteLine("Sorted List: ");
		    foreach (string s in sl.Keys)
		        Console.WriteLine(s + ": " + sl[s]);  // Learn: 72  Solo: 59
		    Console.WriteLine("\nCount: " + sl.Count);  // 2
		}
	}
}


namespace SoloLearn
{
	class Program
	{
		static void Main(string[] args)
		{
		    Stack<int> s = new Stack<int>();
            
		    s.Push(59);
		    s.Push(72);
		    s.Push(65);

		    Console.Write("Stack: ");
		    foreach (int i in s)
		        Console.Write(i + " ");  // 65  72  59
		    Console.Write("\nCount: " + s.Count);  // 3
            
		    Console.Write("\nTop: " + s.Peek());  // 65
		    Console.Write("\nPop: " + s.Pop());  // 65
            
		    Console.Write("\nStack: ");
		    foreach (int i in s)
		        Console.Write(i + " ");  // 72  59
		    Console.Write("\nCount: " + s.Count);  // 2
		}
	}
}


namespace SoloLearn
{
	class Program
	{
		static void Main(string[] args)
		{
            Queue<int> q = new Queue<int>();
            
            q.Enqueue(5);
            q.Enqueue(10);
            q.Enqueue(15);
            Console.Write("Queue: ");
            foreach (int i in q)
                Console.Write(i + " ");  // 5  10  15
            Console.Write("\nCount: " + q.Count);  // 3
            
            Console.Write("\nDequeue: " + q.Dequeue()); // 5
            
            Console.Write("\nQueue: ");
            foreach (int i in q)
                Console.Write(i + " ");  // 10  15
            Console.Write("\nCount: " + q.Count);  // 2
		}
	}
}


namespace SoloLearn
{
	class Program
	{
		static void Main(string[] args)
		{
            HashSet<int> hs = new HashSet<int>();
            
            hs.Add(5);
            hs.Add(10);
            hs.Add(15);
            hs.Add(20);
            Console.Write("\nHashSet: ");
            foreach (int i in hs)
                Console.Write(i + " ");  // 5  10  15  20  *elements may be in any order
            Console.Write("\nCount: " + hs.Count);  // 4
            
            HashSet<int> hs2 = new HashSet<int>();
            hs2.Add(15);
            hs2.Add(20);
            Console.Write("\n{15, 20} is a subset of {5, 10, 15, 20}: " + hs2.IsSubsetOf(hs)); // True 
		}
	}
}

namespace SoloLearn
{
    class Program
    {
        static void Main(string[] args)
        {
            int discount = Convert.ToInt32(Console.ReadLine());

            Dictionary<string, int> coffee = new Dictionary<string, int>();
            coffee.Add("Americano", 50);
            coffee.Add("Latte", 70);
            coffee.Add("Flat White", 60);
            coffee.Add("Espresso", 60);
            coffee.Add("Cappuccino", 80);
            coffee.Add("Mocha", 90);


            //your code goes here
foreach (KeyValuePair<string, int> entry in coffee)
            {
                Console.WriteLine(entry.Key + ": " + (entry.Value - entry.Value * discount / 100));
            }


        }
    }
}


