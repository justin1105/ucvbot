package com.example.ucvbot.model;

import jakarta.persistence.*;
// import lombok.Data;

// @Data
@Entity
public class Student {
// Se elimino el v_ de las variables
    @Id
    @Column(length = 100)
    private String userUID;

    @Column(nullable = false, unique = true, length = 100)
    private String userName;

    @Column(nullable = false, unique = true, length = 100)
    private String email;

    @Column(nullable = false, unique = true, length = 200)
    private String photoURL;

    @ManyToOne
    @JoinColumn(name = "level_id", nullable = false, foreignKey = @ForeignKey(name = "FK_Student_Level"))
    private Level level;

    @Column(nullable = false)
    private Integer correctExercises;

    @Column(nullable = false)
    private Integer incorrectExercises;

    @Column(nullable = false)
    private Integer score;

    // Agregue getter and setter (Fallan Lombok - VS Code)
    public String getUserUID() { return userUID; }
    public void setUserUID(String userUID) { this.userUID = userUID; }

    public String getUserName() { return userName; }
    public void setUserName(String userName) { this.userName = userName; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getPhotoURL() { return photoURL; }
    public void setPhotoURL(String photoURL) { this.photoURL = photoURL; }

    public Level getLevel() { return level; }
    public void setLevel(Level level) { this.level = level; }

    public Integer getCorrectExercises() { return correctExercises; }
    public void setCorrectExercises(Integer correctExercises) { this.correctExercises = correctExercises; }

    public Integer getIncorrectExercises() { return incorrectExercises; }
    public void setIncorrectExercises(Integer incorrectExercises) { this.incorrectExercises = incorrectExercises; }

    public Integer getScore() { return score; }
    public void setScore(Integer score) { this.score = score; }
}
