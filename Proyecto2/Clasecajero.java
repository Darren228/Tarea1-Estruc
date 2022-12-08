
package colasupi;



public class Clasecajero {
    
    // Atributos
    private static final int MAXTAM = 10; // variable constante
    private static int frente;
    private static int ultimo;
    private int []cajero;
    
 public Clasecajero()
 {
    frente = 0;
    ultimo = -1;
    cajero = new int [MAXTAM];
 }   
 
 public void insertar(int elemento)throws Exception
 {
     if (!Cajerolleno())
         cajero[++ultimo] = elemento;
    else
         throw new Exception("La caja está llena");
 }
 
  public int eliminar()throws Exception
 {
     if (!CajeroVacio())
       return cajero[frente++];
    else
      throw new Exception("No hay nadie en la caja");
 }

  public void Borrartodo()
  {
     frente = 0;
     ultimo = -1;
  }
  
  public int frente() throws Exception
  {
      if (!CajeroVacio()) 
          return cajero[frente];
      else
     throw new Exception("LA COLA ESTA VACIA");
  }
  
  
 public boolean Cajerolleno()
 {
   return ultimo == MAXTAM - 1;
 }
 
 public boolean CajeroVacio()
 {
   return frente > ultimo;
 }
}
