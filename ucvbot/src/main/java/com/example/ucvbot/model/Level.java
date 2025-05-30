package com.example.ucvbot.model;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
public class Level {
    // Se quito la v_ de los atributos
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // Básico, Intermedio, Avanzado
    @Column(nullable = false, unique = true, length = 50)
    private String name;

    // Se agrego getter and setters (el lommbok no sta ejecutando correctamente)
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
