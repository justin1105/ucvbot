package com.example.ucvbot.model;

import jakarta.persistence.*;
import lombok.Data;
import org.hibernate.annotations.Check;

import java.util.UUID;

@Data
@Entity
public class Admin {
    // Se quito la v_ de los atributos
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;

    @Column(nullable = false, unique = true, length = 20)
    private String userName;

    @Check(constraints = "password LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'", name = "CK_Password_Admin")
    @Column(nullable = false, length = 8)
    private String password;

    @Column(nullable = false, unique = true, length = 100)
    private String email;

    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

}