#include <iostream>

#define SIZE 5

using namespace std; 
// define class queue with private attribute items, front and rear.
class Queue{
    private: 
    int items[SIZE], front, rear;

    public:

    Queue(){
        front = -1;
        rear  = -1;
    }
    // check queue is empty 
    bool isEmpty(){
        // queue structure is empty when having no elements, front is set to -1
        if (front == -1){
            return true;

        }else{
            return false;
        }
    }
    // check full if the temp size is equal to maxSize
    bool isFull(){
        //  check if front is set to first position and the index of rear is equal to max size -1 
        if( front == 0 && rear == SIZE -1 ){
            return true;
        }
        return false;
    }
    //  adding elements to queue 
    void enQueue(int element){
        // check is full
        if(isFull()){
            cout << "Queue is full";
            // return 0;
        }else{
            if(front == -1) front = 0;
            rear ++;
            items[rear] = element;
            cout << endl << "Insert: "<< element << endl; 
        }
    }
    int deQueue(){
        int element;
        // check empty 
        if(isEmpty()){
            cout << "Queue is empty";
            // return 0;
        }
        else{
            element = items[front];
            if(front >= rear){
                front = -1; 
                rear  = -1;
            }else{
                front ++ ;
            }
            cout <<endl;
            cout << "Delete -> "<< element << endl;
        }
        return (element);
    }
    void display(){
        int i; 
        if(isEmpty()){
            cout<<endl << "Queue is Empty" <<endl;
            // return 0;
        }else{
            cout << endl << "Front index-> " << front;
            cout << endl << "Items -> ";
            for (i = front; i <= rear; i++)
                cout << items[i] << "  ";
            cout << endl << "Rear index-> " << rear << endl;
        }

    }
};

int main(){
    Queue q;

    //deQueue is not possible on empty queue
    q.deQueue();

    //enQueue 5 elements
    q.enQueue(1);
    q.enQueue(2);
    q.enQueue(3);
    q.enQueue(4);
    q.enQueue(5);

    // 6th element can't be added to because the queue is full
    q.enQueue(6);

    q.display();

    //deQueue removes element entered first i.e. 1
    q.deQueue();

    //Now we have just 4 elements
    q.display();

    return 0;
}