/* #include <iostream>
using namespace std;

int main()
{ 
int passengers;
cout << "";
cin >> passengers ;

int left_passengers= passengers % 50;

if(left_passengers == 0){
    
    cout << "0 seats left";
}
else{
 int left_seats= 50 - left_passengers;
    
    cout << left_seats;
    cout << "";
}
    
	return 0;
} */

/* #include <iostream>
using namespace std;

int main() {
    int n;
    cout << "\n\n\t\tEnter the initial value: ";
    cin >> n;
    do{
      cout <<"\t" << n << endl;
   if(n%5==0) 
   {
     cout <<"\tBeep" << endl;
       }
      n--;
       } while(n>0);
     
         
         
         
   //your code goes here
    
    
    return 0;
} */

/* #include <iostream>
using namespace std;

int main() {
    int ages[5];
    cout << "\n\tEnter the ages of the customers: ";
    for (int i = 0; i < 5; ++i) 
    {
        cin >> ages[i];
    }
    
    double youngest = ages[0];
    for (int a = 0; a <5; ++a)
    {
        if(youngest>ages[a])
        {
            youngest = ages[a];
        }
    }
    
    double prezzo = 50 - (50*youngest/100);
    cout << prezzo;
    
    return 0;
} */


/* #include <iostream>
using namespace std;
int revDigit(int y){
    int rem,rev=0;
    while(y>0){
        rem=y%10;
        rev=rev*10+rem;
        y/=10;
        
    }return rev;
}

bool isPalindrome(int x) {
    //complete the function
    if(x==revDigit(x)){
        return true;
    }
    else{
        return false;
    }
        
    
}

int main() {
    int n;
    cin >>n;
    
    if(isPalindrome(n)) {
        cout <<n<<" is a palindrome";
    }
    else {
        cout << n<<" is NOT a palindrome";
    }
   
    return 0;
} */

/* #include <iostream>
using namespace std; 

class Queue { 
	int size; 
	int* queue; 
	
	public:
	Queue() {
		size = 0;
		queue = new int[100];
	}
	void remove() { 
		if (size == 0) { 
			cout << "Queue is empty"<<endl; 
			return; 
		} 
		else { 
			for (int i = 0; i < size - 1; i++) { 
				queue[i] = queue[i + 1]; 
			} 
			size--; 
		} 
	} 
 void print() { 
		if (size == 0) { 
			cout << "Queue is empty"<<endl; 
			return; 
		} 
		for (int i = 0; i < size; i++) { 
			cout<<queue[i]<<" <- ";
		} 
		cout <<endl;
	}
	//your code goes here
 void add( int newData ) {
  
     if( size != 0 || size != 100 ) {

          size++; //increment size
          queue[size-1] = newData; //make new element as the last element

      }

}
}; 

int main() { 
	Queue q; 
	q.add(42); q.add(2); q.add(8); q.add(1); 
	q.print();
	q.remove(); 
	q.add(128); 
	q.print(); 
	q.remove(); 
	q.remove(); 
	q.print(); 

	return 0; 
} */

/* #include <iostream>
using namespace std; 

class Queue { 
	
	int size; 
	int size1; 
	int size2; 
	int* queue; 
	int* q1;
	int* q2;
	public:
	Queue() { 
		

		size = 0;
		queue = new int[100];
	}
	void add(int data) { 
		queue[size] = data; 
		size++;
	}
	void remove() { 
		if (size == 0) { 
			cout << "Queue is empty"<<endl; 
			return; 
		} 
		else { 
			for (int i = 0; i < size - 1; i++) { 
				queue[i] = queue[i + 1]; 
			} 
			size--; 
		} 
	} 
	void print() { 
		if (size == 0) { 
			cout << "Queue is empty"<<endl; 
			return; 
		} 
		for (int i = 0; i < size; i++) { 
			cout<<queue[i]<<" <- ";
		} 
		cout << endl;
	}
//your code goes here
	Queue operator+(Queue &obj) {
        Queue res;
        for(int i=0;i<this->size;i++) {
            res.add(this->queue[i]);
        }
        for(int i=0;i<obj.size;i++) {
            res.add(obj.queue[i]);
        }
        return res; 
    }
	
}; 

int main() { 
	Queue q1; 
	q1.add(42); q1.add(2); q1.add(8);  q1.add(1);
	Queue q2;
	q2.add(3); q2.add(66); q2.add(128);  q2.add(5);
	Queue q3 = q1+q2;
	q3.print();

	return 0; 
} */


/* 
#include <iostream>
using namespace std; 

class Queue { 
	public:
	int size; 
	int* queue; 
	
	public:
	Queue() { 
		size = 0;
		queue = new int[100];
	}
	void add(int data) { 
		queue[size] = data; 
		size++;
	}
	void remove() { 
		if (size == 0) { 
			cout << "Queue is empty"<<endl; 
			return; 
		} 
		else { 
			for (int i = 0; i < size - 1; i++) { 
				queue[i] = queue[i + 1]; 
			} 
			size--; 
		} 
	} 
	void print() { 
		if (size == 0) { 
			cout << "Queue is empty"<<endl; 
			return; 
		} 
		for (int i = 0; i < size; i++) { 
			cout<<queue[i]<<" <- ";
		} 
		cout << endl;
	}
	Queue operator+(Queue &obj) {
        Queue res;
        for(int i=0;i<this->size;i++) {
            res.add(this->queue[i]);
        }
        for(int i=0;i<obj.size;i++) {
            res.add(obj.queue[i]);
        }
        return res; 
    }
}; 

//your code goes here
class Queue2: public Queue 
{
public: 
    Queue2 () {

	};
	void print() { 
		if (size == 0) { 
			cout << "Queue is empty"<<endl; 
			return; 
		} 
		for (int i = 0; i < size; i++) { 
			cout<<queue[i]<<"\n";
		} 
		cout << endl;
	}
};   


int main() { 
	Queue q1; 
	q1.add(42); q1.add(2); q1.add(8);  q1.add(1);
    q1.print();
    
	Queue2 q2;
	q2.add(3); q2.add(66); q2.add(128);  q2.add(5);q2.add(111);q2.add(77890);
	q2.print();

	return 0; 
} */

#include <iostream>
using namespace std; 
template <class T>
class Queue { 
    int size; 
    
    T* queue; 
    
    public:
    Queue() { 
        size = 0;
        queue = new T[100];
    }
    void add(T data) { 
        queue[size] = data; 
        size++;
    }
    void remove() { 
        if (size == 0) { 
            cout << "Queue is empty"<<endl; 
            return; 
        } 
        else { 
            for (int i = 0; i < size - 1; i++) { 
                queue[i] = queue[i + 1]; 
            } 
            size--; 
        } 
    } 
    void print() { 
        if (size == 0) { 
            cout << "Queue is empty"<<endl; 
            return; 
        } 
        for (int i = 0; i < size; i++) { 
            cout<<queue[i]<<" <- ";
        } 
        cout << endl;
    }
    Queue operator+(Queue &obj) {
        Queue res;
        for(int i=0;i<this->size;i++) {
            res.add(this->queue[i]);
        }
        for(int i=0;i<obj.size;i++) {
            res.add(obj.queue[i]);
        }
        return res; 
    }
    
}; 

int main() { 
    Queue<int> q1; 
    q1.add(42); q1.add(2); q1.add(8);  q1.add(1);
    q1.print();
    
    Queue<string> q2;
    q2.add("Dave"); q2.add("John"); q2.add("Amy");
    q2.print();

    return 0; 
}