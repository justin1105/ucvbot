import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { StudentService } from 'src/app/providers/student/student.service';
import { UserCredential } from '@angular/fire/auth';
import { Student } from 'src/app/shared/interfaces/student.interface';
import { take } from 'rxjs/operators';

@Component({
  selector: 'auth-app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  constructor(
    private authService: AuthService,
    private router: Router,
    private studentService: StudentService
  ) {}

  ingresar() {
  console.log('[LOGIN] Iniciando sesión...');
  localStorage.removeItem('exercises');

  this.authService
    .login()
    .then((userCredential: UserCredential) => {
      console.log('[LOGIN ÉXITO]', userCredential);

      const uid = userCredential.user.uid;
      const email = userCredential.user.email ?? '';
      console.log('[UID]', uid);

      const result$ = this.studentService.getStudentByUserUID(uid);
      console.log('[DEBUG] Observable:', result$);

      result$
        .pipe(take(1))
        .subscribe(
          (student: Student | null) => {
            console.log('[SUBSCRIBE] Entró al subscribe');
            console.log('[STUDENT]', student);

            // 👇 Aquí está el manejo del resultado
            if (!student) {
              console.warn('[AVISO] No se encontró estudiante. Redirigiendo...');
              this.router.navigate(['/welcome']); // redirige aunque no exista
              return;
            }

            if (student.status === undefined) {
              console.log('[NAVEGAR] → /chat');
              this.router.navigate(['/chat']);
            } else {
              console.log('[NAVEGAR] → /welcome');
              this.router.navigate(['/welcome']);
            }
          },
          (err) => {
            console.error('[ERROR] al obtener estudiante:', err);
            this.router.navigate(['/welcome']); // redirige si hay error
          }
        );
    })
    .catch((error) => {
      console.error('[ERROR] Login fallido:', error);
    });
}
}