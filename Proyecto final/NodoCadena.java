/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejemploprofe;

/**
 *
 * @author Darren
 */
public class NodoCadena {
    private String dato;
    private String genero;
    private NodoCadena izquierda, derecha;

    public NodoCadena(String dato, String genero) {
        this.dato = dato;
        this.genero= genero;
        this.izquierda = this.derecha = null;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }
    


    public String getDato() {
        return dato;
    }

    public NodoCadena getIzquierda() {
        return izquierda;
    }

    public void setIzquierda(NodoCadena izquierda) {
        this.izquierda = izquierda;
    }

    public NodoCadena getDerecha() {
        return derecha;
    }

    public void setDerecha(NodoCadena derecha) {
        this.derecha = derecha;
    }

    public void imprimirDato() {
        System.out.println(this.getDato()+""+this.getGenero());
    }
    public void imprimirfemeninas(){
         System.out.println(this.getDato()+"F"+this.getGenero());
        
    }
   
    
}


