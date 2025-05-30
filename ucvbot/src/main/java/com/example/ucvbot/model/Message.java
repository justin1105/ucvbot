package com.example.ucvbot.model;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonManagedReference;
import jakarta.persistence.*;
// import lombok.Data;

import java.util.List;

// @Data
@Entity
public class Message {
// Se quito la v_ de los atributos
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(columnDefinition = "TEXT", nullable = false)
    private String statement;

    @Column(nullable = false, length = 10)
    private String role;

    @Column(nullable = false)
    private Long unixTime;

    @OneToMany(mappedBy = "message", cascade = CascadeType.ALL, orphanRemoval = true)
    @JsonManagedReference
    private List<Alternative> alternatives;

    @Column(nullable = true)
    private Integer answer;

    @Column(nullable = true)
    private Boolean answered;

    @ManyToOne
    @JoinColumn(name = "chat_id", nullable = false, foreignKey = @ForeignKey(name = "FK_Message_Chat"))
    @JsonBackReference
    private Chat chat;

    // Agregue getter and setter (Falla Lombok - VS Code)
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getStatement() { return statement; }
    public void setStatement(String statement) { this.statement = statement; }

    public String getRole() { return role; }
    public void setRole(String role) { this.role = role; }

    public Long getUnixTime() { return unixTime; }
    public void setUnixTime(Long unixTime) { this.unixTime = unixTime; }

    public List<Alternative> getAlternatives() { return alternatives; }
    public void setAlternatives(List<Alternative> alternatives) { this.alternatives = alternatives; }

    public Integer getAnswer() { return answer; }
    public void setAnswer(Integer answer) { this.answer = answer; }

    public Boolean getAnswered() { return answered; }
    public void setAnswered(Boolean answered) { this.answered = answered; }

    public Chat getChat() { return chat; }
    public void setChat(Chat chat) { this.chat = chat; }
}
