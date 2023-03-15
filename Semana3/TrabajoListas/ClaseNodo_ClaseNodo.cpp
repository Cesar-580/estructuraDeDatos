#include <iostream>
using namespace std;

class Nodo {
    public: 
        int datos;
        Nodo *siguientePtr;
};

class Lista{
    private:
        Nodo *primeroPtr;       //P, apuntador al inicio de la lista 
        bool estaVacia();

    public:
        Lista();                //Constructor
        ~Lista();               //Destructor
        void insertarAlInicio(int valor); //inserta el nodo al inicio
        void recorrerIterativo(); // muestra el contenido de la lista
};

// definición de funciones dela clase Lista

// verifica si la lista está vacía

bool Lista::estaVacia()
{
    return primeroPtr == NULL;
}

// constructor predeterminado

Lista::Lista()
{
    primeroPtr = NULL;
}

// destructor predeterminado

Lista::~Lista()
{
    if(!estaVacia() )
    {
        cout<<"\n\n Destruyendo nodos ... \n\n";

        Nodo *actualPtr = primeroPtr;
        Nodo *tempPtr;

        // elimina los nodos restantes

        while( actualPtr != NULL)
        {
            tempPtr = actualPtr;
            cout<<tempPtr -> datos << ' ';
            actualPtr = actualPtr -> siguientePtr;
            delete tempPtr;
        }

    }
    cout<<"\n\nSe destruyeron todos los nodos \n\n";
}

// Insertar al inicio

void Lista::insertarAlInicio( int valor)
{
    Nodo *nuevoPtr = new Nodo();    // Q, var
    nuevoPtr -> datos = valor;      // Dato

    if (estaVacia())
    {
        nuevoPtr->siguientePtr = NULL;
    }else{
        nuevoPtr -> siguientePtr = primeroPtr;
    }

    primeroPtr = nuevoPtr; // Apunta el primero

}


void Lista::eliminarPrimero()
{
    if( estaVacia())
    {
        cout<<"\n La lista está vacia \n\n";
    }

    cout<<"\n Destruyendo el nodo\n\n"<< primeroPtr -> datos<< "\n";
    Nodo *tempPtr = primeroPtr;
    primeroPtr = primeroPtr -> siguientePTr;
    delete tempPtr;
}

void Lista::eliminarNodo( int referencia)
{

    if (actualPtr -> datos = referencia)
    {
        Nodo *tempPtr = actualPtr;

        if( primeroPtr == actualPtr )
        {
            primeroPtr = primeroPtr -> siguientePTr;
        }else{
            previoPtr -> siguientePTr = actualPtr -> siguientePTr;
        }
        cout<<"\n Destruyendo el nodo\n\n"<< tempPtr -> datos<< "\n";
        delete tempPtr;
    }else{
        cout<<"\n El nodo dado como referencia no se encuentra en la lista \n\n";
    }
}








void Lista ::recorrerIterativo()
{
    if( estaVacia() )       // la lista esta vacia
    {
        cout<<"\n La lista esta vacia \n\n";
        system("pause");
        return;
    }

    Nodo *actualPtr = primeroPtr; // definición del inicio de la lista

    cout << "\n Los elementos de la lista son: "; 

    while (actualPtr != NULL)   // obtiene los datos del elemento
    {
        cout<< actualPtr -> datos << "- >";   // Se imprime el valor de la posición actual
        actualPtr = actualPtr -> siguientePtr;  // Se pasa al siguiente Nodo
    }

    cout<<"\n\n";
    system("pause");
}

// definición de funciones de la clase Lista

// imprime las instrucciones

void menu()
{
    system("cls");
    cout << "\n ..[ LISTA SIMPLEMENTE LIGADA ]..";
    cout << "\n ..[ Erika Meneses Rico ]..\n\n";
    cout << "[1] Insertar elemento al inicio \n";
    cout << "[2] Imprimir los valores de la lista \n";
    cout << "[3] Salir \n";
    cout << "\n Ingrese opción: \n";
}

// rutina principal

int main()
{
    int opcion;
    int valor;

    Lista listaEnteros;

    system("color 1F");

    do
    {
        menu();
        cin>> opcion;
        Lista listaEnteros;
        
        switch (opcion)
        {
        case 1:
            cout<<"\n Ingrese valor entero: ";
            cin>> valor;
            listaEnteros.insertarAlInicio( valor);
            listaEnteros.recorrerIterativo();
            break;
        
        case 2:
            listaEnteros.recorrerIterativo();
            break;
        }
    } while (opcion != 3);
    
    return 0;
}






