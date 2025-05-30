package com.example.ucvbot.services;

import com.example.ucvbot.model.Admin;
import com.example.ucvbot.repository.AdminRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
// @RequiredArgsConstructor
public class AdminService {

    private final AdminRepository v_adminRepository;

    public AdminService(AdminRepository v_adminRepository) {
        this.v_adminRepository = v_adminRepository;
    }

    public Admin getAdminById(UUID id) {
        return v_adminRepository.findById(id).orElseThrow(() -> new RuntimeException("ID NOT FOUND: " + id));
    }

    public Admin saveAdmin(Admin admin) {
        return v_adminRepository.save(admin);
    }

    public Admin updateAdmin(Admin admin, UUID id) {
        getAdminById(id);
        return v_adminRepository.save(admin);
    }

    public List<Admin> getAll() {
        return v_adminRepository.findAll();
    }

    public Optional<Admin> login(String useerName, String password) {
        return v_adminRepository.findByUserNameAndPassword(useerName, password);
    }

    @Transactional
    public boolean resetPassword(String userName, String email, String newPassword) {
        int updated = v_adminRepository.resetPasswordByUserNameAndEmail(userName, email, newPassword);
        return updated > 0;
    }
}
