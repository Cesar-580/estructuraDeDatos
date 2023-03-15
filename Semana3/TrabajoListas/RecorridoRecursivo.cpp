#include <iostream>

void Lista::recorreRecursivo( Nodo *actualPtr )
{
    if( actualPtr != NULL)
    {
        cout<< actualPtr -> datos << ' ';
        recorreRecursivo( actualPtr -> siguientePtr );
    }
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